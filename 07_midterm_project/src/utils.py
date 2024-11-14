# src/utils.py
import pandas as pd

def save_to_csv(df: pd.DataFrame, file_path: str):
    df.to_csv(file_path, index=False)
