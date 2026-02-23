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
    def load(cls, path: str):
    
        with open(path,"r", encoding="utf-8") as f:
            data=json.load(f)

        required=["base_url", "endpoint", "timeout",  "retry_count", "raw_dir", "clean_dir", "csv_fields"]
        for key in required:
            if key not in data:
                raise ConfigError (f"Missing config key: {key}")
        return cls(
            base_url=data["base_url"],
            endpoint=data["endpoint"],
            timeout=data["timeout"],
            retry_count=data["retry_count"],
            raw_dir=data["raw_dir"],
            clean_dir=data["clean_dir"],
            csv_fields=data["csv_fields"]
        )
            

    
        