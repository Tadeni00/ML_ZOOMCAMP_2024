from src.data_ingestion import download_data, load_data
from src.data_preprocessing import rename_columns, convert_data_types
from src.feature_engineering import handle_missing_values, impute_numerical_columns, feature_engineering
from src.data_transformation import handle_outliers, boxcox_transformation, scale_numerical_data
from src.clustering import apply_kmeans
from src.utils import save_to_csv
import logging
from src.logger import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the data processing pipeline")
    # Data Ingestion
    download_data('12r59IXJ1GECKHTgY8erhWgM5H3x_pJxz', 'data/customers_data.csv')
    df = load_data('data/customers_data.csv')
    
    # Preprocessing
    df = rename_columns(df)
    df = convert_data_types(df)
    
    # Feature Engineering
    df = handle_missing_values(df)
    numerical_columns = ['age', 'customer_seniority', 'gross_income']
    df = impute_numerical_columns(df, numerical_columns)
    
    # Apply feature engineering (e.g., account sums, categorical encoding)
    df = feature_engineering(df)
    
    # Data Transformation
    df = handle_outliers(df, numerical_columns)
    df = boxcox_transformation(df, numerical_columns)
    df = scale_numerical_data(df, numerical_columns)
    
    # Clustering
    df = apply_kmeans(df, 5)
    
    # Save results
    save_to_csv(df, 'artifacts/df_segmented.csv')
    logging.info("Data processing pipeline completed successfully")

if __name__ == '__main__':
    main()
