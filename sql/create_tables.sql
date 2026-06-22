CREATE TABLE IF NOT EXISTS crypto_prices (
    id SERIAL PRIMARY KEY,
    coin_id VARCHAR(50),
    symbol VARCHAR(10),
    name VARCHAR(50),
    current_price FLOAT,
    market_cap BIGINT,
    total_volume BIGINT,
    price_change_24h FLOAT,
    retrieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

