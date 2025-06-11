import pandas as pd
from utils.logger import get_logger


logger = get_logger(__name__)


def normalize_orders_currency(order_df: pd.DataFrame, fx_df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting currency normalization transformation...")

    # 1. Ensure lowercase column match
    fx_df = fx_df.rename(columns={"target_currency": "currency"})

    # 2. Merge both DataFrames on 'currency'
    merged_df = order_df.merge(
        fx_df[["currency", "rate"]], on='currency', how='left')

    # 3. Handle missing exchange rates (edge cases)
    if merged_df['rate'].isnull().any():
        logger.warning("Some currencies do not have matching exchange rates.")
        merged_df['rate'] = merged_df['rate'].fillna(1.0)

    # 4. Add normalized USD amount column
    merged_df['amount_EUR'] = merged_df['amount']/merged_df['rate']

    logger.info(f"Transformed {len(merged_df)} order records into USD equivalent.")
    return round(merged_df)
