from sklearn.feature_extraction import DictVectorizer
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np
import logging
from src.logger import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Handling missing values with mode imputation")
    # Mode imputation for categorical columns
    for column in df.columns:
        df[column] = df[column].fillna(df[column].mode()[0])
    logging.info("Missing values handled successfully")
    return df

def impute_numerical_columns(df: pd.DataFrame, numerical_columns: list) -> pd.DataFrame:
    logging.info("Imputing missing numerical values using KNNImputer")
    # Convert non-numeric values (e.g., ' NA') to NaN
    for column in numerical_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')
    
    # Apply KNN imputation
    imputer = KNNImputer(n_neighbors=5)
    df[numerical_columns] = imputer.fit_transform(df[numerical_columns])
    logging.info("Numerical imputation completed")
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Performing feature engineering")
    logging.info("Creating new feature columns for each category of accounts") 
    deposit_features = ['savings_account', 'current_account', 'short_term_deposits',
                        'medium_term_deposits', 'long_term_deposits']
    credit_features = ['mortgage', 'loan', 'credit_card']
    investment_features = ['investment_funds', 'securities']
    pension_features = ['pension_plan', 'pensions_recent']
    special_features = ['e_account', 'junior_account', 'particular_account',
                        'mas_particular_account', 'particular_plus_account', 'home_account', 'payroll_account']


    # Add total account columns
    df['total_deposit_accounts'] = df[deposit_features].sum(axis=1)
    df['total_credit_accounts'] = df[credit_features].sum(axis=1)
    df['total_investment_accounts'] = df[investment_features].sum(axis=1)
    df['total_pension_accounts'] = df[pension_features].sum(axis=1)
    df['total_special_accounts'] = df[special_features].sum(axis=1)
    logging.info("New feature columns for each category of accounts created")

    logging.info("Encoding categorical features") 
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['deceased_indicator'] = df['deceased_indicator'].map({'Deceased': 1, 'Not Deceased': 0})
    df['foreigner_index'] = df['foreigner_index'].map({'Foreigner': 1, 'Non-Foreigner': 0})
    df['residence_index'] = df['residence_index'].map({'Resident': 1, 'Non-Resident': 0})
    df['relationship_type'] = df['relationship_type'].map({
        'Active': 1, 'Inactive': 0, 'Potential': 2, 'New': 3, 'Standard': 4, 'Business': 5
    })
    logging.info("Categorical features encoded successfully") 

    logging.info("Converting columns to datetime")
    df['data_date'] = pd.to_datetime(df['data_date'], errors='coerce')
    df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
    
    # Ensure the columns are not categorical
    df['data_date'] = df['data_date'].astype('datetime64[ns]')
    df['registration_date'] = df['registration_date'].astype('datetime64[ns]')
    logging.info("Columns to successfully converted to datetime")


    # Calculate the tenure in days
    df['customer_tenure'] = (df['data_date'] - df['registration_date']).dt.days
    
    # List of columns to drop
    columns_to_drop = [
        'data_date', 'registration_date', 'last_primary_date', 'savings_account', 'current_account',
        'short_term_deposits', 'medium_term_deposits', 'long_term_deposits',
        'mortgage', 'loan', 'credit_card', 'investment_funds', 'securities',
        'pension_plan', 'pensions_recent', 'e_account', 'junior_account',
        'particular_account', 'mas_particular_account', 'particular_plus_account',
        'home_account', 'payroll_account', 'age', 'primary_address', 'activity_index', 'gross_income'
    ]

    # Drop the columns
    df.drop(columns=columns_to_drop, inplace=True)

    # Convert DataFrame to a dictionary format
    df = df.to_dict(orient='records')

    # Initialize DictVectorizer for categorical columns
    dict_vectorizer = DictVectorizer(sparse=False)

    # Transform data using DictVectorizer
    df_encoded = dict_vectorizer.fit_transform(df)

    # Convert back to DataFrame to separate out encoded features
    df = pd.DataFrame(df_encoded, columns=dict_vectorizer.get_feature_names_out())
    logging.info("Feature engineering completed successfully")
    return df
