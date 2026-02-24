import requests
from requests.exceptions import RequestException
from typing import Any
class ApiRequestError(Exception):
    pass


class ApiClient:
    def __init__(self, base_url: str, timeout: int, retry_count: int):
        self.base_url=base_url
        self.timeout=timeout
        self.retry_count=retry_count
        
    def get_json(self,endpoint: str):
        for attempt in range(self.retry_count):
            try:
                response=requests.get(f"{self.base_url}/{endpoint}",timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except RequestException:
                if attempt == self.retry_count - 1:
                    raise ApiRequestError(f"GET failed: {self.base_url}/{endpoint}") from e
        