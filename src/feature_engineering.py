# feature_engineering.py
import pandas as pd
import numpy as np
import logging

from src.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def feature_engineering(df: pd.DataFrame):
    try:
        # Extract date and time components
        df['Hour'] = df['Timestamp'].dt.hour
        df['Day of Week'] = df['Timestamp'].dt.dayofweek
        df['Month'] = df['Timestamp'].dt.month

        # Feature Engineering
        df['Is_Weekend'] = df['Day of Week'].apply(lambda x: 1 if x >= 5 else 0)
        df['Time_Spent_Ratio'] = df['Daily Time Spent on Site'] / df['Daily Internet Usage']
        df['Income_Per_Age'] = df['Area Income'] / df['Age']
        
        logger.info("Feature engineering completed successfully")
        return df
    except Exception as e:
        logger.error(f"Error in feature engineering: {e}")
        raise e
