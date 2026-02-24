from dataclasses import dataclass
import json


class ConfigError(Exception):
    pass


@dataclass
class Config:
    base_url: str
    endpoint: str
    timeout: int
    retry_count: int
    raw_dir: str
    clean_dir: str
    csv_fields: list[str]

    @classmethod
    def load(cls, path: str) -> "Config":
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise ConfigError(f"Config file not found: {path}") from e
        except json.JSONDecodeError as e:
            raise ConfigError(f"Invalid JSON in config file: {path}") from e

        required = [
            "base_url",
            "endpoint",
            "timeout",
            "retry_count",
            "raw_dir",
            "clean_dir",
            "csv_fields",
        ]

        for key in required:
            if key not in data:
                raise ConfigError(f"Missing config key: {key}")

        if not isinstance(data["csv_fields"], list):
            raise ConfigError("csv_fields must be a list")

        return cls(
            base_url=data["base_url"],
            endpoint=data["endpoint"],
            timeout=data["timeout"],
            retry_count=data["retry_count"],
            raw_dir=data["raw_dir"],
            clean_dir=data["clean_dir"],
            csv_fields=data["csv_fields"],
        )
