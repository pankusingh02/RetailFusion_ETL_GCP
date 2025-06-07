import os
import pandas as pd
from datetime import datetime

from utils.logger import get_logger

logger= get_logger(__name__)

def extract_csv(file_path:str)->pd.DataFrame:
    try:
        logger.info(f"Starting CSV extraction from {file_path}")
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")  # Log error if file is missing
            raise FileNotFoundError(f"File not found: {file_path}")
        
        df=pd.read_csv(file_path)
        logger.info(f"CSV file successfully loaded. Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    
    except Exception as e:
        logger.exception("Error occurred during CSV extraction.")
        raise e
