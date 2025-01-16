from interfaces.scraper_investing_strategy_interface import ScraperInvestingSI

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Extraction:
    def __init__(self, scraper_strategy: ScraperInvestingSI):
        self._scraper = scraper_strategy

    def data(self):

        options = Options()
        driver = webdriver.Remote(
            command_executor="http://172.17.0.1:4444",
            options=options
        )
        driver.get("https://www.investing.com")
        WebDriverWait(driver, 20).until(EC.url_contains("investing.com"))

        return self._scraper.get_data(driver)