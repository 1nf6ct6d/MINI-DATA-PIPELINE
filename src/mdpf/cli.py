from .config import Config
from .http.api_client import ApiClient
from .io.file_store import FileStore


def main() -> None:
    config = Config.load("config.json")

    client = ApiClient(config.base_url, config.timeout, config.retry_count)
    data = client.get_json(config.endpoint)

    store = FileStore(config.raw_dir)
    saved_path = store.save_raw_json(data, prefix=config.endpoint)

    print(saved_path)
    print(len(data))