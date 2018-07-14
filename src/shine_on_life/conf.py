#!/usr/bin/python
# -*- coding: utf8 -*-
from decouple import config


class _Settings:
    DEBUG = config("DEBUG", default=False, cast=bool)

    # Default board settings
    DEFAULT_BOARD_WIDTH = 10
    DEFAULT_BOARD_HEIGHT = 10


settings = _Settings()
