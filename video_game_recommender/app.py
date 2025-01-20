import streamlit as st
import pandas as pd
import os
import logging
from src.data_processing import process_data
from src.feature_engineering import clean_and_vectorize, feature_engineering
from src.model import compute_cosine_similarity
from src.predict import display_similar_games_with_covers
# from src.logger import setup_logger

# Set up logging
log_file_path = os.path.join("logs", "logger.log")
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Load and preprocess data
data = pd.read_csv('/workspaces/ML_ZOOMCAMP_2024/video_game_recommender/data/video_game_reviews.csv')  # Update path if needed
data.columns = [col.lower().replace(' ', '_') for col in data.columns]
categorical_cols = data.select_dtypes(include=['object', 'category']).columns

# Process data
data = process_data(data, categorical_cols)

# Perform feature engineering
data = feature_engineering(data)

filtered_data = data.filter(like='combined_features_vec_')
print(filtered_data.isna().sum().sum())  # Total count of NaN values

# Compute cosine similarity
cosine_sim_matrix = compute_cosine_similarity(data.filter(like='combined_features_vec_'))

# Streamlit app interface
st.title('Game Recommendation App')
game_to_check = st.text_input('Enter a game title:')
top_n = st.number_input('Number of similar games to display:', min_value=1, max_value=10, value=5)

if st.button('Get Recommendations'):
    try:
        similar_games = display_similar_games_with_covers(data, cosine_sim_matrix, game_to_check, top_n)
        st.write(similar_games)
    except ValueError as e:
        st.error(str(e))
