import json

from interfaces.scraper_investing_strategy_interface import ScraperInvestingSI

from selenium import webdriver

class InvestingStrategy(ScraperInvestingSI):
    def get_data(self, driver: webdriver.Remote) -> None:

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
            data = json.loads(driver.execute_script(script))
        finally:
            driver.quit()

        if "data" in data:
            print(data)
            # Write the fetched data to output.json
            with open("output.json", "w") as outfile:
                json.dump(data, outfile, indent=4)
        else:
            print("Expected key 'data' not found in the response.")