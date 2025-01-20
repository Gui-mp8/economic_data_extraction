from typing import List, Dict, Any
import json

from api.interfaces.selenium_investing_strategy_interface import SeleniumInvestingSI

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumInvestingStrategy(SeleniumInvestingSI):

    def _setup_driver(self):
        # Configurar opções para o Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # Novo modo headless
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            # "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        # Inicializar o WebDriver
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(driver_version="132.0.6834.83").install()
            ),  # driver_version="132.0.6834.83"
            options=chrome_options,
        )
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
            driver = self._setup_driver()
            json_data = json.loads(driver.execute_script(script))
        finally:
            driver.quit()

        if "data" in json_data:
            return json_data["data"]
        else:
            print("Expected key 'data' not found in the response.")