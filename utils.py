import logging

logging.basicConfig(level=logging.INFO)

def log_error(error_message):
    logging.error(f"Error: {error_message}")

def log_info(message):
    logging.info(f"Info: {message}")
