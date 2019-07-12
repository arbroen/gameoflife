# -*- coding: utf8 -*-
from typing import Dict
from pathlib import Path

from gol.conf import settings


def load_presets() -> Dict[str, Path]:
    return {path.stem: path for path in settings.PRESET_DIR.glob("*.csv")}


PRESETS = load_presets()
