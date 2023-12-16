import sys

# CLI Interface for user input

class CLIInterface:
    @staticmethod
    def get_user_input():
        """Collects compatibility criteria from the user.

        Returns:
            dict: User input criteria for file formats and sample rates.
        """
        print("Please enter the compatible file formats (comma separated, e.g., mp3, wav): ", end='')
        file_formats = input().split(',')
        print("Please enter the compatible sample rates (comma separated, e.g., 44100, 48000): ", end='')
        sample_rates = input().split(',')
        return {
            'file_formats': [format.strip().lower() for format in file_formats],
            'sample_rates': [int(rate.strip()) for rate in sample_rates]
        }
