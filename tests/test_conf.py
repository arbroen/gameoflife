# -*- coding: utf8 -*-
from gol.conf import _Settings, settings


class TestSettings:
    def test_cls_instantiation(self):
        sett = _Settings()

        assert hasattr(sett, "DEBUG")

    def test_cast_debug(self):
        assert isinstance(settings.DEBUG, bool)
