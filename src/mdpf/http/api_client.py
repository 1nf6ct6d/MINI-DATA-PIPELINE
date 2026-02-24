import requests
from requests.exceptions import RequestException


class ApiRequestError(Exception):
    pass


class ApiClient:
    def __init__(self, base_url: str, timeout: int, retry_count: int) -> None:
        self.base_url = base_url.rstrip("/")   
        self.timeout = timeout
        self.retry_count = retry_count

    def get_json(self, endpoint: str):
        endpoint = endpoint.lstrip("/")        
        url = f"{self.base_url}/{endpoint}"

        last_error: Exception | None = None

        for attempt in range(self.retry_count):
            try:
                response = requests.get(url, timeout=self.timeout)
                response.raise_for_status()
                return response.json()
            except RequestException as e:
                last_error = e
                if attempt == self.retry_count - 1:
                    raise ApiRequestError(f"GET failed after {self.retry_count} attempts: {url}") from e

        raise ApiRequestError(f"GET failed: {url}") from last_error