import pandas as pd
import logging
from src.data_ingestion import load_data
from src.data_preprocessing import preprocess_data
from src.feature_engineering import feature_engineering
from src.data_transformation import transform_data
from src.model import train_and_evaluate_model
from src.predict_pipeline import PredictionPipeline 

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Load and process the data
    file_path = "data/ad_10000records.csv"
    
    # Load the dataset
    df = load_data(file_path)
    
    # Preprocess the data
    df = preprocess_data(df)
    
    # Feature engineering step
    df = feature_engineering(df)
    
    # Data transformation
    X, y, column_transformer = transform_data(df)
    
    # Train the model
    best_model = train_and_evaluate_model(X, y)
    
    # Mock input for prediction
    test_data = {
        "Ad Topic Line": "Decentralized real-time circuit",
        "City": "West Angelabury",
        "Gender": "Male",
        "Country": "Singapore",
        "Daily Time Spent on Site": 100.5,
        "Age": 25,
        "Area Income": 40000.0,
        "Daily Internet Usage": 120.0,
    }
    
    # Convert the test data into a DataFrame
    test_df = pd.DataFrame([test_data])

    # Initialize the PredictionPipeline
    prediction_pipeline = PredictionPipeline()

    # Use the pipeline to preprocess and make a prediction
    prediction = prediction_pipeline.predict(test_df)

    # Log the prediction result
    if prediction[0] == 1:
        logging.info("😊😀...The user clicked on Ad")
    else:
        logging.info("😥🤔...The user did not click on Ad")

if __name__ == "__main__":
    main()
