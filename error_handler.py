# Error Handler

class ErrorHandler:
    @staticmethod
    def handle_error(error_message):
        """Handles common file and directory errors by printing an error message.

        Args:
            error_message (str): The error message to be handled.
        """
        print(f'Error: {error_message}')
