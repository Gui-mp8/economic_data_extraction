from interfaces.scraper_strategy_interface import ScraperSI

class Extraction:
    def __init__(self, scraper_strategy: ScraperSI):
        self._scraper = scraper_strategy

    def data(self):
        return self._scraper.get_data()