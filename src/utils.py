# utils.py
import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/process.log",
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
