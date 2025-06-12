import os
import pandas as pd
from google.cloud import storage
from google.oauth2 import service_account
from utils.logger import get_logger

logger= get_logger(__name__)


def load_to_gcs(df: pd.DataFrame, format='csv') -> None:
    try:
        bucket_name = os.getenv("GCS_BUCKET_NAME")
        destination_blob = os.getenv("GCS_DEST_PATH",'output/orders_normalized.csv')
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        client=storage.Client(credentials=credentials)

        bucket=client.bucket(bucket_name)
        blob= bucket.blob(destination_blob)

        # Save DataFrame to local temp file
        local_temp="temp_file."+ format

        if format=='csv':
            df.to_csv(local_temp, index=False)
        elif format=='parquet':
            df.to_parquet(local_temp, index=False)
        else:
            raise ValueError("Unsupported file format")

        #Upload to GCS
        blob.upload_from_filename(local_temp)
        logger.info(f"Uploaded {local_temp} to gs://{bucket_name}/{destination_blob}")

        # Optional: remove temp file
        os.remove(local_temp)

    except Exception as e:
        logger.exception("Failed to load data to GCS")
        raise e