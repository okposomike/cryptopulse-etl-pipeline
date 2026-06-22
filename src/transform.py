import json
import pandas as pd
import os
from datetime import datetime



def transform_data(raw_file_path):

    with open(raw_file_path, "r") as file:
        data = json.load(file)

    df = pd.DataFrame(data)
    df["loaded_at"] = datetime.now()
    df = df[
        [
            "id",
            "symbol",
            "name",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h",
            "loaded_at"
        ]
    
    ]
  

    df.rename(
        columns={
            "id": "coin_id",
            "price_change_percentage_24h": "price_change_24h"
        },
        inplace=True
    )

    df.fillna(0, inplace=True)

    os.makedirs("/opt/airflow/data/silver", exist_ok=True)

    output_file = (
        "/opt/airflow/data/silver/crypto_processed.csv"
    )

    df.to_csv(output_file, index=False)

    return output_file