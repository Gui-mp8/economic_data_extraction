from api.interfaces.investing_strategy_interface import InvestingSI

class Scraper:
    def __init__(self, scraper_strategy: InvestingSI):
        self._scraper = scraper_strategy

    def data(self):
        return self._scraper.get_data()