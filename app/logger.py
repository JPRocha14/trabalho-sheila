import logging
from logging.handlers import RotatingFileHandler
import os

log_path = "logs"
os.makedirs(log_path, exist_ok=True)

def get_logger():
    logger = logging.getLogger("WebLogger")
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(f"{log_path}/app.log", maxBytes=1000000, backupCount=3)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
