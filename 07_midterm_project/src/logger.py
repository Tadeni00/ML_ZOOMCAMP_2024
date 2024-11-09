# src/logger.py
import logging
import os
from datetime import datetime

# Create the logs directory if it doesn't exist
logs = "logs"
os.makedirs(logs, exist_ok=True)

# Define the log file name with timestamp
log_filename = datetime.now().strftime("log_%Y_%m_%d.log")
log_filepath = os.path.join(logs, log_filename)

# Configure the logger
logging.basicConfig(
    filename=log_filepath,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Create a logger instance
logger = logging.getLogger()
