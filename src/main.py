from datetime import datetime

from context.extraction import Extraction
from strategies.bloomberg_commodity import BloombergCommodityStrategy

def main():
    result = BloombergCommodityStrategy().get_data()
    
    print(result)
    # today = datetime.now().strftime('%Y-%m-%d')

    # bloomberg = BloombergCommodityStrategy()
    # bloomberg.url = f"https://api.investing.com/api/financialdata/historical/948434?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"

    # extraction = Extraction(scraper_strategy=BloombergCommodityStrategy())
    # data = extraction.data()
