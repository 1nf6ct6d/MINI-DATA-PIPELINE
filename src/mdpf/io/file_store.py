from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class FileStore:
    raw_dir: str

    def save_raw_json(self, obj: Any, prefix: str) -> Path:
        raw_path = Path(self.raw_dir)
        raw_path.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = raw_path / f"{prefix}_{ts}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)

        return file_path