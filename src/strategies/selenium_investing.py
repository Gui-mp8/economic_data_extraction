from typing import List, Dict, Any
import json

from interfaces.selenium_investing_strategy_interface import SeleniumInvestingSI

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SeleniumInvestingStrategy(SeleniumInvestingSI):

    def _get_remote_webdriver(self) -> webdriver.Remote:
        options = Options()
        driver = webdriver.Remote(
            command_executor="http://172.17.0.1:4444",
            options=options
        )
        driver.get("https://www.investing.com")
        WebDriverWait(driver, 20).until(EC.url_contains("investing.com"))

        return driver

    def get_data(self) -> List[Dict[str, Any]]:

        script = f"""
        return fetch('{self.url}', {{
            method: "GET",
            headers: {{
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "content-type": "application/json",
                "domain-id": "www",
                "origin": "https://www.investing.com",
                "referer": "https://www.investing.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0"
            }}
        }})
        .then(response => response.json())
        .then(data => JSON.stringify(data))
        .catch((error) => JSON.stringify({{"error": error.message}}));
        """
        try:
            driver = self._get_remote_webdriver()
            json_data = json.loads(driver.execute_script(script))
        finally:
            driver.quit()

        if "data" in json_data:
            return json_data["data"]
        else:
            print("Expected key 'data' not found in the response.")