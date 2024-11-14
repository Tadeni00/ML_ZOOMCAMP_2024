# data_preprocessing.py
import pandas as pd
import logging

from src.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def preprocess_data(df: pd.DataFrame):
    try:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.drop_duplicates(inplace=True)
        logger.info("Data preprocessing completed successfully")
        return df
    except Exception as e:
        logger.error(f"Error in data preprocessing: {e}")
        raise e
