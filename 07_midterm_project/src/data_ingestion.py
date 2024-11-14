# src/data_ingestion.py
import gdown
import pandas as pd
import logging
from src.logger import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_data(file_id: str, output_path: str):
    logging.info(f"Downloading data from Google Drive with file ID: {file_id}")
    gdown.download(id=file_id, output=output_path, quiet=False)
    logging.info(f"Data downloaded to: {output_path}")

def load_data(file_path: str) -> pd.DataFrame:
    logging.info(f"Loading data from file: {file_path}")
    df = pd.read_csv(file_path, low_memory=False)
    logging.info(f"Data loaded successfully with shape: {df.shape}")
    return df

