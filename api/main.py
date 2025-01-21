from datetime import datetime
import os

from api.utils.config import load_config
from api.context.scraper import Scraper
from api.strategies.selenium_investing import SeleniumInvestingStrategy
from api.strategies.requests_investing import RequestsInvestingStrategy
from api.targets.cloud_storage import CloudStorage

from fastapi import FastAPI, APIRouter, Depends

scraper = APIRouter()

@scraper.get("/")
def root():
    config = load_config()

    today = datetime.now().strftime('%Y-%m-%d')

    selenium = SeleniumInvestingStrategy()

    selenium.url = f"https://api.investing.com/api/financialdata/historical/948434?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    bloomberg = Scraper(scraper_strategy=selenium)
    bloomberg_data = bloomberg.data()
    CloudStorage(config).upload_json(bloomberg_data, "bloomberg.json")

    selenium.url = f"https://api.investing.com/api/financialdata/historical/2111?start-date=1991-01-01&end-date={today}&time-frame=Monthly&add-missing-rows=false"
    usc_cny = Scraper(scraper_strategy=selenium)
    usc_cny_data = usc_cny.data()
    CloudStorage(config).upload_json(usc_cny_data, "usc_cny.json")

    requests = RequestsInvestingStrategy()

    requests.url = "https://sbcharts.investing.com/events_charts/eu/596.json"
    china_index = Scraper(scraper_strategy=requests)
    china_index_data = china_index.data()
    CloudStorage(config).upload_json(china_index_data, "china_index.json")

    return {"text": "Data saved at Storage"}

app = FastAPI()

app.include_router(scraper, prefix="/scraper")


