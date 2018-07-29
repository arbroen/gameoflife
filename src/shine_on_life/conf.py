# -*- coding: utf8 -*-
import os

from pathlib import Path
from decouple import AutoConfig


_HERE = Path(__file__).absolute()

# Override regular config to be able to set search path for .env/.ini files.
config = AutoConfig(
    search_path=os.environ.get("ENV_FILE_PATH", default=_HERE))


class _Settings:
    DEBUG = config("DEBUG", default=False, cast=bool)

    # Default board settings
    MINIMAL_BOARD_WIDTH = \
        config("MINIMAL_BOARD_WIDTH", default=10, cast=int)
    MINIMAL_BOARD_HEIGHT = \
        config("MINIMAL_BOARD_HEIGHT", default=10, cast=int)
    DEFAULT_BOARD_WIDTH = \
        config("DEFAULT_BOARD_WIDTH", default=MINIMAL_BOARD_WIDTH, cast=int)
    DEFAULT_BOARD_HEIGHT = \
        config("DEFAULT_BOARD_HEIGHT", default=MINIMAL_BOARD_HEIGHT, cast=int)
    DEFAULT_REFRESH_TIME = \
        config("DEFAULT_REFRESH_TIME", default=.25, cast=float)


settings = _Settings()
print('\033[33m{msg}\033[0m'.format(msg=settings.DEBUG), flush=True)