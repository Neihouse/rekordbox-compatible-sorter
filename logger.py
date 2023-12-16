import logging

# Configure logging
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    @staticmethod
    def log_operation(operation):
        # Log operations performed by the script
        logging.info(operation)
