import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import logging

def compute_cosine_similarity(normalized_vectors):
    # Check if the input is of the correct type
    if not isinstance(normalized_vectors, (list, pd.DataFrame)):
        raise TypeError("Input for cosine similarity must be a list or pandas DataFrame.")
    
    # Handle DataFrame input
    if isinstance(normalized_vectors, pd.DataFrame):
        # Drop rows with NaN values
        normalized_vectors = normalized_vectors.dropna()

    # Handle list input
    if isinstance(normalized_vectors, list):
        # Convert list to DataFrame for easier handling of NaN
        normalized_vectors = pd.DataFrame(normalized_vectors).dropna()

    # Compute cosine similarity
    return cosine_similarity(normalized_vectors)



def find_similar_games(data, cosine_sim_matrix, game_title, top_n=5):
    if game_title not in data['game_title'].values:
        raise ValueError(f"Game title '{game_title}' not found in dataset.")

    game_idx = data.index[data['game_title'] == game_title][0]
    similarity_scores = list(enumerate(cosine_sim_matrix[game_idx]))

    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    similar_games = [(data.iloc[idx]['game_title'], score) for idx, score in similarity_scores]

    logging.info(f"Found {len(similar_games)} similar games for '{game_title}'.")


    return similar_games
