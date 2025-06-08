from dotenv import load_dotenv
import pandas as pd
import requests
import os
from datetime import datetime
from utils.logger import get_logger

logger=get_logger(__name__)

load_dotenv()
from typing import List, Optional

def extract_exchange_rates(
    base_currency: str = 'USD',
    target_currencies: Optional[List[str]] = None) -> pd.DataFrame:

    #Loading API key
    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        logger.error(("Missing EXCHANGE_API_KEY in environment"))
        raise EnvironmentError("Key is missing")
    
    #Prepare API key requesr params
    symbols= ','.join(target_currencies)
    url = f"https://api.exchangeratesapi.io/v1/latest"
    params={
        "access_key":api_key,
        "base":base_currency,
        "symbols":symbols
    }

    try:
        logger.info(f'Fetching exchange rates for {base_currency}->{target_currencies}')
        response=requests.get(url,params=params)
        data= response.json()

        if not data.get("success", False):
            msg=data.get("error",{}).get("info", 'Unknown error')
            logger.error(f'API returned a error : {msg}')
            raise RuntimeError (f'API fetching error : {msg}')
        
        date, rates=data["date"], data["rates"]

        records=[
            {
                "base_currency":base_currency,
                "target_currency": tc,
                "rate": rates,
                "date":date
            }
            for tc, rates in rates.items()
        ]

        df=pd.DataFrame(records)
        logger.info(f'Extrached {len(df)} rates for {date}')
        return df
    
    except Exception as e:
        logger.exception(f"Failed to extract exchange rates from exchangeratesapi.io: {e}")
        raise
