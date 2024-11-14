# data_transformation.py
import os
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import LabelEncoder
import logging
from src.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def transform_data(df: pd.DataFrame):
    try:
        # Box-Cox transformation for numerical columns
        numeric_cols = ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']
        for col in numeric_cols:
            if (df[col] > 0).all():  # Ensuring the column contains positive values
                df[col], _ = boxcox(df[col])

        # Drop Timestamp column (non-relevant for modeling)
        df = df.drop('Timestamp', axis=1)

        # Create the preprocessing pipeline for numerical and categorical columns
        numerical_pipeline = Pipeline([
            ('scaler', RobustScaler())  # Scaling the numerical features
        ])

        categorical_pipeline = Pipeline([
            ('onehot', OneHotEncoder(sparse_output=False))  # Ensure dense output for one-hot encoding
        ])

        # Defining the full column transformer
        column_transformer = ColumnTransformer(
            transformers=[
                ('num', numerical_pipeline, numeric_cols),
                ('cat', categorical_pipeline, ['Ad Topic Line', 'City', 'Gender', 'Country'])
            ])

        # Apply the column transformer
        transformed_data = column_transformer.fit_transform(df)

        # Convert to a DataFrame
        transformed_df = pd.DataFrame(transformed_data)

        # Label encoding for target column 'Clicked on Ad'
        y = df['Clicked on Ad']
        X = transformed_df
        y = LabelEncoder().fit_transform(y)

        logger.info("Data transformation completed successfully")

        # Save the entire column transformer pipeline as a pickle file
        transformer_path = 'artifacts/transformer.pkl'
        os.makedirs(os.path.dirname(transformer_path), exist_ok=True)
        joblib.dump(column_transformer, transformer_path)
        logger.info("Pickle file for column transformer saved successfully")

        return X, y, column_transformer
    except Exception as e:
        logger.error(f"Error in data transformation: {e}")
        raise e
