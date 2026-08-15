import os 
import logging

log_file = os.getenv("LOG_FILE_PATH")
logging.basicConfig(
    filename = log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Server started")


def log_message(message):
    logger.info(message)