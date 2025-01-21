import streamlit as st
import pandas as pd
import os
import logging
from src.data_processing import process_data
from src.feature_engineering import clean_and_vectorize, feature_engineering
from src.model import compute_cosine_similarity, find_similar_games
from src.predict import display_similar_games_with_covers
from src.fetch_game_cover import fetch_game_cover

# Set up logging
log_file_path = os.path.join("logs", "logger.log")
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Load and preprocess data
data = pd.read_csv('./data/video_game_reviews.csv')
data.columns = [col.lower().replace(' ', '_') for col in data.columns]
categorical_cols = data.select_dtypes(include=['object', 'category']).columns

# Process data
data = process_data(data, categorical_cols)

# Perform feature engineering
data = feature_engineering(data)

filtered_data = data.filter(like='combined_features_vec_')
print(filtered_data.isna().sum().sum())

# Compute cosine similarity
cosine_sim_matrix = compute_cosine_similarity(data.filter(like='combined_features_vec_'))

# Streamlit app title and inputs
st.title("🎮 Game Recommendation 🎮")
st.subheader("Discover your next favorite game!")

# Input section
game_title = st.text_input("Enter a Game Title:", placeholder="E.g., Street Fighter V")
num_similar_games = st.number_input("Number of similar games to display:", min_value=1, max_value=10, value=5)

# Add some spacing and style
st.markdown("---")  # Horizontal line for separation
st.write("Click the button below to get game recommendations based on your input!")
if st.button("Get Recommendations", key="get_recommendations"):
    if not game_title.strip():
        st.error("🚨 Please enter a valid game title.")
    else:
        # Generate recommendations using your recommendation model
        recommendations = find_similar_games(data, cosine_sim_matrix, game_title, top_n=num_similar_games)
        
        if not recommendations:
            st.error("😞 No recommendations found. Please try a different game title.")
        else:
            st.markdown("### Recommended Games:")
            st.markdown("---")  # Horizontal line for separation

            # Arrange recommendations horizontally using st.columns
            cols = st.columns(len(recommendations))

            for i, (game_name, similarity_score) in enumerate(recommendations):
                with cols[i]:
                    # Fetch game cover and details
                    game_details = fetch_game_cover(game_name)
                    logging.info("Game Cover picture fetched")
                

                    if game_details:
                        st.image(
                            game_details["cover_url"],
                            caption=f"{game_details['name']}  \nReleased: {game_details['release_date']}",
                            use_container_width=True,
                        )
                    else:
                        st.warning(f"No image available for '{game_name}'")