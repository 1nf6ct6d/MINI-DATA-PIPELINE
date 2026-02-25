from __future__ import annotations

from dataclasses import dataclass

from ..config import Config, ConfigError
from ..http.api_client import ApiClient, ApiRequestError
from ..io.file_store import FileStore
from ..transform.json_to_csv import JsonTransformer


@dataclass
class PipelineRunner:
    config_path: str = "config.json"

    def run(self) -> int:
        try:
            config = Config.load(self.config_path)

            client = ApiClient(config.base_url, config.timeout, config.retry_count)
            data = client.get_json(config.endpoint)

            store = FileStore(config.raw_dir, config.clean_dir)
            store.save_raw_json(data, prefix=config.endpoint)

            transformer = JsonTransformer(config.csv_fields)
            clean_rows = transformer.transform(data)

            store.write_clean_csv(clean_rows, prefix=config.endpoint, fieldnames=config.csv_fields)

            return 0

        except ConfigError:
            return 2

        except ApiRequestError:
            return 3

        except ValueError:
            return 4

        except OSError:
            return 5