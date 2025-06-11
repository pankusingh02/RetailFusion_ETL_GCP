import os
import pandas as pd
import psycopg2
from psycopg2 import Error
from utils.logger import get_logger

logger = get_logger(__name__)

DATABASE_NAME_WITH_ORDERS_TABLE = "SQL"


def extract_orders_from_postgres() -> pd.DataFrame:
    try:
        # Load credentials from environment variables
        db_config = {
            "host": os.getenv("PG_HOST", "localhost"),
            "port": int(os.getenv("PG_PORT", 5432)),
            "user": os.getenv("PG_USER", "postgres"),
            "password": int(os.getenv("PG_PASSWORD",1234)),
            "database": DATABASE_NAME_WITH_ORDERS_TABLE
        }

        logger.info(
            f"Connecting to PostgreSQL on {db_config['host']}:{db_config['port']}/{db_config['database']}")

        # Establish a connection to the PostgreSQL database
        # ** =  the dictionary unpacking operator
        connection = psycopg2.connect(**db_config)

        if connection:
            logger.info("Connection successful ")

            query = "select * from orders"

            df = pd.read_sql(query, con=connection)
            return df
    except Error as e:
        logger.exception(f"Error while connecting to PostgreSQL or fetching data: {e}")
        raise e
    
    finally:
        if 'connection' in locals() and connection:
            connection.close()
            logger.info("PostgreSQL connection closed.")
