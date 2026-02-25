from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class JsonTransformer:
    fields: list[str]

    def transform(self, data: Any) -> list[dict]:
        if not isinstance(data, list):
            raise ValueError("Data must be a list of dicts")

        clean_rows: list[dict] = []
        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Each item must be a dict")
            row = {field: item.get(field) for field in self.fields}
            clean_rows.append(row)

        return clean_rows