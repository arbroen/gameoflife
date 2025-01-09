ARG PYTHON_BASE_IMAGE=python:3.10-slim

FROM $PYTHON_BASE_IMAGE as base

ENV APP_DIR=/opt/gol \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV VENV_DIR="${APP_DIR}/.venv"
ENV VENV_BINARIES="${VENV_DIR}/bin"

# Ensure paths are created (for WORKDIR instructions)
RUN mkdir ${APP_DIR}
# Ensure we're working from application perspective
WORKDIR ${APP_DIR}

FROM base as poetry_installer

ENV POETRY_VENV=/opt/poetry-venv \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VERSION=2.0.0 \
    POETRY_CACHE_DIR=/opt/.cache

# Install pip and poetry inside a separate poetry environment.
RUN python3 -m venv $POETRY_VENV \
    && ${POETRY_VENV}/bin/pip install -U pip setuptools \
    && ${POETRY_VENV}/bin/pip install poetry==${POETRY_VERSION}

# Append poetry binary to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
COPY poetry.lock pyproject.toml ./

# Installs only what is necessary for production
FROM poetry_installer as minimal_build

ENV PATH="${VENV_BINARIES}:${PATH}"

# Project installation
RUN poetry install --only main --no-root
COPY . .
RUN poetry install --only-root

# Installs everything necessary for development
FROM minimal_build as dev_build

RUN poetry install --only=dev --no-root

### FINAL STAGES
FROM base as production

COPY --from=minimal_build $APP_DIR $APP_DIR
ENV PATH="${VENV_BINARIES}:${PATH}"

ENTRYPOINT ["gol", "preset", "oscilator"]
