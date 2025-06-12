from extract.extract_sql import extract_orders_from_postgres
from extract.extract_api import extract_exchange_rates
from transform.transform_order_data import normalize_orders_currency
from load.load_to_bigquery import load_to_bigquery
from load.load_to_gcs import load_to_gcs

# 1. Extract both data sources
orders_df = extract_orders_from_postgres()
fx_df = extract_exchange_rates("USD", ["USD", "EUR", "INR"])

print(f'===========>{fx_df}')

# 2. Apply transformation
normalized_df = normalize_orders_currency(orders_df, fx_df)

print(normalized_df)

# load to Bigquery
load_to_bigquery(normalized_df)

# Load to GCS (CSV or parquet)
load_to_gcs(normalized_df, format="csv")
