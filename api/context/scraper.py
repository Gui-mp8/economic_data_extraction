from api.interfaces.selenium_investing_strategy_interface import SeleniumInvestingSI

class Scraper:
    def __init__(self, scraper_strategy: SeleniumInvestingSI):
        self._scraper = scraper_strategy

    def data(self):
        return self._scraper.get_data()