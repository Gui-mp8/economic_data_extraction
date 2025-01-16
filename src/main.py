from datetime import datetime

from context.extraction import Extraction
from strategies.investing import InvestingStrategy

def main():
    today = datetime.now().strftime('%Y-%m-%d')

    bloomberg = InvestingStrategy()
    bloomberg.url = f"https://api.investing.com/api/financialdata/historical/948434?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    extraction = Extraction(scraper_strategy=bloomberg)
    extraction.data()

    # usc_cny = InvestingStrategy()
    # usc_cny.url = f"https://api.investing.com/api/financialdata/historical/2111?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    # extraction = Extraction(scraper_strategy=usc_cny)
    # extraction.data()

if __name__ == "__main__":
    main()
