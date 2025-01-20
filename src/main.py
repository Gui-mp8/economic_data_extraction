from datetime import datetime
import os

from src.utils.config import load_config
from src.context.scraper import Scraper
from src.strategies.selenium_investing import SeleniumInvestingStrategy
from src.targets.cloud_storage import CloudStorage

from fastapi import FastAPI, APIRouter, Depends

scraper = APIRouter()

@scraper.get("/")
def root():
    config = load_config()

    today = datetime.now().strftime('%Y-%m-%d')

    investing = SeleniumInvestingStrategy()

    investing.url = f"https://api.investing.com/api/financialdata/historical/948434?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    bloomberg = Scraper(scraper_strategy=investing)
    bloomberg_data = bloomberg.data()
    CloudStorage(config).upload_json(bloomberg_data, "bloomberg.json")

    return {"text": "Data saved at Storage"}

app = FastAPI()

# Include the scraper router with a prefix
app.include_router(scraper, prefix="/scraper")


    # config = load_config()
    # print("Hello World")
    
    # today = datetime.now().strftime('%Y-%m-%d')

    # investing = SeleniumInvestingStrategy()

    # investing.url = f"https://api.investing.com/api/financialdata/historical/948434?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    # bloomberg = Scraper(scraper_strategy=investing)
    # bloomberg_data = bloomberg.data()
    
    # CloudStorage(config).upload_json(bloomberg_data, "bloomberg.json")

    # investing.url = f"https://api.investing.com/api/financialdata/historical/2111?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    # usc_cny = Scraper(scraper_strategy=investing)
    # usc_cny_data = usc_cny.data()
    # CloudStorage(config).upload_json(usc_cny_data, "usc_cny.json")

# if __name__ == "__main__":
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./suzano-challenge.json"
    # config = load_config()
    # main(config)

