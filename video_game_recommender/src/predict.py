from src.model import find_similar_games
import logging

def display_similar_games_with_covers(data, cosine_sim_matrix, game_to_check, top_n=5):
    try:
        similar_games = find_similar_games(data, cosine_sim_matrix, game_to_check, top_n=top_n)
        logging.info(f"Displaying similar games for '{game_to_check}'.")
        return similar_games
    except ValueError as e:
        logging.error(e)
        return []
