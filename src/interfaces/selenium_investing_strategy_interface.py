from abc import ABC, abstractmethod
from typing import List, Dict, Any

class SeleniumInvestingSI(ABC):
    def __init__(self):
        self._url = None

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, endpoint: str) -> None:
        self._url = endpoint

    @abstractmethod
    def get_data(self) -> List[Dict[str, Any]]:
        pass

