from .config import Config
from .http.api_client import ApiClient
from .io.file_store import FileStore
from .transform.json_to_csv import JsonTransformer


def main() -> None:
    config = Config.load("config.json")

    client = ApiClient(config.base_url, config.timeout, config.retry_count)
    data = client.get_json(config.endpoint)

    store = FileStore(config.raw_dir, config.clean_dir)
    raw_path = store.save_raw_json(data, prefix=config.endpoint)

    transformer = JsonTransformer(config.csv_fields)
    clean_rows = transformer.transform(data)

    csv_path = store.write_clean_csv(clean_rows, prefix=config.endpoint, fieldnames=config.csv_fields)

    print(raw_path)
    print(csv_path)
    print(len(data))