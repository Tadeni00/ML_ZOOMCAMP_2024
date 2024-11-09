# src/clustering.py
from sklearn.cluster import KMeans
import pandas as pd
import logging
from src.logger import logger

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def apply_kmeans(df: pd.DataFrame, n_clusters: int) -> pd.DataFrame:
    logging.info(f"Applying KMeans clustering with {n_clusters} clusters")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(df)
    logging.info("KMeans clustering completed")
    return df
