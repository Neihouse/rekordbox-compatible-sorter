import logging

class ErrorHandler:
    @staticmethod
    def handle_error(error):
        # Handle common errors and exceptions
        logging.error(f'Error: {error}')
        print(f'Error: {error}')
