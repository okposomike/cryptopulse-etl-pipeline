import os
from airflow.decorators import dag, task
from datetime import datetime
import sys

sys.path.insert(0, "/opt/airflow")
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


@dag(
    dag_id="crypto_pipeline",
    start_date=datetime(2026, 6, 18),
    schedule="@daily",
    catchup=False,
    tags=["crypto", "etl"]
)
def crypto_pipeline():

    @task
    def extract():
        return extract_data()

    @task
    def transform(file_path):
        return transform_data(file_path)

    @task
    def load(processed_file):
        return load_data(processed_file)

    raw_file = extract()

    processed_file = transform(raw_file)

    load(processed_file)


crypto_pipeline()