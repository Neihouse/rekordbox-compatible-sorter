import logging

# Logger for operations

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_operation(self, message):
        """Logs operations to a text file.

        Args:
            message (str): The message to log.
        """
        logging.info(message)
