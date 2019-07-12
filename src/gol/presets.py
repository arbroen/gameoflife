# -*- coding: utf8 -*-
from pathlib import Path
from typing import Dict

from gol.conf import settings


def load_presets() -> Dict[str, Path]:
    return {path.stem: path for path in settings.PRESET_DIR.glob("*.csv")}


PRESETS = load_presets()
