from .config import Config 
from .http.api_client import ApiClient
def main():
    config = Config.load("config.json")
    print(config)
    
    client = ApiClient(config.base_url, config.timeout, config.retry_count)
    data = client.get_json(config.endpoint)
    print(len(data))