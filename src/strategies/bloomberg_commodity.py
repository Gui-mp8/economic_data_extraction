import json
from datetime import datetime

# from interfaces.scraper_strategy_interface import ScraperSI

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# import pandas as pd

class BloombergCommodityStrategy():
    def selenium_instance(self):

        options = Options()
        driver = webdriver.Remote(
            command_executor="http://172.17.0.1:4444",
            options=options
        )
        driver.get("https://www.investing.com")
        WebDriverWait(driver, 20).until(EC.url_contains("investing.com"))
        return driver

    def get_data(self):
        today = datetime.now().strftime('%Y-%m-%d')

        print("Getting data")
        script = f"""
        return fetch("https://api.investing.com/api/financialdata/historical/2111?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false", {{
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
        driver = self.selenium_instance()
        try:
            data = json.loads(driver.execute_script(script))
        finally:
            driver.quit()

        if "data" in data:
            print(data)
        #     df = pd.DataFrame(data['data'])

        #     colunas_relevantes = {
        #         'rowDate': 'date',
        #         'last_close': 'close',
        #         'last_open': 'open',
        #         'last_max': 'high',
        #         'last_min': 'low',
        #         'volume': 'volume'
        #     }

        #     df_filtrado = df[list(colunas_relevantes.keys())].rename(columns=colunas_relevantes)

        #     df_filtrado.to_csv('bloomberg.csv', index=False)
        #     print("Dados filtrados e salvos com sucesso.")
        # else:
        #     print("Erro: Dados não encontrados.")

