import pandas as pd
import logging


def process_data(data, categorical_cols):
    # Initialize an empty string for combined features
    data['combined_features'] = ''

    # Combine categorical columns into the combined_features string
    for col in categorical_cols:
        data['combined_features'] += data[col].astype(str) + ' '

    # Add numerical columns
    data['combined_features'] += 'Rating_' + data['user_rating'].astype(str) + ' ' + \
                                 'Price_' + data['price'].astype(str) + ' '

    # Remove duplicates based on 'game_title'
    data = data.drop_duplicates(subset=['game_title'])
    
    logging.info("Data processed successfully.")
    return data
