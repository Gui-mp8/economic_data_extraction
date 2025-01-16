from abc import ABC, abstractmethod
from typing import List, Dict, Any

from selenium import webdriver

class ScraperInvestingSI(ABC):
    def __init__(self):
        self._url = None

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, endpoint: str) -> None:
        self._url = endpoint

    @abstractmethod
    def get_data(self, driver: webdriver.Remote) -> List[Dict[str, Any]]:
        pass

