import os
import pandas as pd
from utils.logger import get_logger
from google.cloud import bigquery
from google.oauth2 import service_account

logger = get_logger(__name__)


def load_to_bigquery(df: pd.DataFrame) -> None:
    try:
        project_id = os.getenv("GCP_PROJECT_ID")
        dataset = os.getenv("BQ_DATASET", "reatail")
        table = os.getenv("BQ_TABLE", "orders_usd")

        full_table_id = f'{project_id}.{dataset}.{table}'

        logger.info(f'Loading data to Bigquery table: {full_table_id}')

        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not credentials_path:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")
        
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path)

        # The df.to_gbq() function is a pandas method that writes a DataFrame directly to Google BigQuery
        df.to_gbq(
            destination_table=full_table_id,
            project_id=project_id,
            credentials=credentials,
            if_exists='replace'
        )

        logger.info(f'Loaded {len(df)} rows to {full_table_id} successfully')

    except Exception as e:
        logger.exception("Error while loading the bigQuery")
        raise e
