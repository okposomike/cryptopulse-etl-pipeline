import pandas as pd

from src.database import get_engine


def load_data(processed_file):

    df = pd.read_csv(processed_file)

    engine = get_engine()

    df.to_sql(
        "crypto_prices",
        con=engine,
        if_exists="append",
        index=False
    )

    return f"{len(df)} rows inserted"