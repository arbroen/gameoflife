import logging
import os
import sys
from pathlib import Path

from decouple import AutoConfig

_HERE = Path(__file__).absolute()

# Override regular config to be able to set search path for .env/.ini files.
config = AutoConfig(search_path=os.environ.get("GOL_ENV_FILE_PATH", default=_HERE))


class _Settings:
    DEBUG = config("DEBUG", default=False, cast=bool)
    PRESET_DIR = _HERE.parents[1] / "presets"

    # Default board settings
    MINIMAL_BOARD_WIDTH = config("MINIMAL_BOARD_WIDTH", default=10, cast=int)
    MINIMAL_BOARD_HEIGHT = config("MINIMAL_BOARD_HEIGHT", default=10, cast=int)
    DEFAULT_BOARD_WIDTH = config(
        "DEFAULT_BOARD_WIDTH", default=MINIMAL_BOARD_WIDTH, cast=int
    )
    DEFAULT_BOARD_HEIGHT = config(
        "DEFAULT_BOARD_HEIGHT", default=MINIMAL_BOARD_HEIGHT, cast=int
    )
    DEFAULT_REFRESH_TIME = config("DEFAULT_REFRESH_TIME", default=0.5, cast=float)
    DEFAULT_GENERATION_COUNT = config("DEFAULT_GENERATIONS", default=25, cast=int)
    # Numpy specifics
    NUMPY_DATA_TYPE = "int8"
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "advanced": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
            },
            "message_only": {"format": "%(message)s"},
        },
        "handlers": {
            "normal": {
                "class": "logging.StreamHandler",
                "formatter": "advanced",
                "level": logging.DEBUG,
            },
            "printer": {
                "class": "logging.StreamHandler",
                "formatter": "message_only",
                "level": logging.INFO,
                "stream": sys.stdout,
            },
        },
        "printer": {"handlers": ["printer"], "level": logging.INFO},
        "root": {"handlers": ["printer"], "level": logging.DEBUG},
    }


settings = _Settings()
