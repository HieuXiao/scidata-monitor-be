from abc import ABC, abstractmethod
from typing import Any


class BaseAPIClient(ABC):
    def __init__(self, base_url: str, api_key: str | None = None):
        self.base_url = base_url
        self.api_key = api_key

    @abstractmethod
    async def fetch_batch(self, from_date: str, limit: int = 100) -> list[dict[str, Any]]:
        pass
