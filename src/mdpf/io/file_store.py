from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
import json
import csv


@dataclass
class FileStore:
    raw_dir: str
    clean_dir: str

    def save_raw_json(self, obj, prefix: str):
        raw_path = Path(self.raw_dir)
        raw_path.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = raw_path / f"{prefix}_{ts}.json"

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)

        return file_path

    def write_clean_csv(self, rows, prefix: str, fieldnames):
        clean_path = Path(self.clean_dir)
        clean_path.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = clean_path / f"{prefix}_{ts}.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        return file_path