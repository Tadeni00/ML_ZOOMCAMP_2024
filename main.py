# main.py
import pandas as pd
from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.feature_engineering import feature_engineering
from src.data_transformation import transform_data
from src.model import train_and_evaluate_model

def main():
    file_path = "data/ad_10000records.csv"
    
    df = load_data(file_path)
    df = preprocess_data(df)
    df = feature_engineering(df)
    X, y, column_transformer = transform_data(df)
    
    best_model = train_and_evaluate_model(X, y)

if __name__ == "__main__":
    main()
