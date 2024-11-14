# data_ingestion.py
import pandas as pd
import logging
import os

from src.utils import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
        logger.info("Data loaded successfully")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise e
