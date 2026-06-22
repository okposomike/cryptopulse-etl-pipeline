import requests
import json
import os
from datetime import datetime

from src.config import COINGECKO_URL


def extract_data():

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": "false"
    }

    headers = {
        "User-Agent": "CryptoPulse"
    }

    response = requests.get(
        COINGECKO_URL,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    os.makedirs("/opt/airflow/data/bronze", exist_ok=True)

    file_path = (
        f"/opt/airflow/data/bronze/"
        f"crypto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    return file_path