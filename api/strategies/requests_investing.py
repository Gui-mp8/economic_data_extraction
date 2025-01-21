from typing import List, Dict, Any

from api.interfaces.investing_strategy_interface import InvestingSI

import requests

class RequestsInvestingStrategy(InvestingSI):

    def get_data(self) -> List[Dict[str, Any]]:
        # url = "https://sbcharts.investing.com/events_charts/eu/596.json"
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
