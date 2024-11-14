# src/data_transformation.py
from scipy.stats import boxcox
from scipy.stats.mstats import winsorize
from sklearn.preprocessing import RobustScaler
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
from src.logger import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def handle_outliers(df: pd.DataFrame, numerical_columns: list) -> pd.DataFrame:
    logging.info("Handling outliers using winsorization")
    """
    Winsorize columns to handle outliers in the provided numerical columns list.
    """
    lower_limit = 0.05
    upper_limit = 0.95
    
    # Ensure 'age' is not in numerical_columns
    numerical_columns = [col for col in numerical_columns if col in df.columns and col != 'age']
    
    for col in numerical_columns:
        # Apply winsorize only if column exists in DataFrame
        if col in df.columns:
            df[col] = winsorize(df[col], limits=(lower_limit, upper_limit))
    logging.info("Outlier handling completed")
    
    return df

def boxcox_transformation(df: pd.DataFrame, numerical_columns: list) -> pd.DataFrame:
    logging.info("Applying Box-Cox transformation")
    """
    Apply Box-Cox transformation on the provided numerical columns.
    """
    # Ensure 'age' is not in numerical_columns
    numerical_columns = [col for col in numerical_columns if col in df.columns and col != 'age']
    
    for col in numerical_columns:
        if col in df.columns and df[col].nunique() > 1:
            df[col] = boxcox(df[col] + 1)[0]
        else:
            print(f"Skipping column {col} as it is constant or not present in DataFrame.")
    logging.info("Box-Cox transformation completed")
    
    return df

def scale_numerical_data(df: pd.DataFrame, numerical_columns: list) -> pd.DataFrame:
    logging.info("Scaling numerical data using RobustScaler")
    """
    Scale numerical data using RobustScaler.
    """
    # Ensure 'age' is not in numerical_columns
    numerical_columns = [col for col in numerical_columns if col in df.columns and col != 'age']
    
    if numerical_columns:  # Check if list is not empty
        scaler = RobustScaler()
        df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    logging.info("Data scaling completed")

    
    return df
