# Compatibility Manager

class CompatibilityCriteria:
    def __init__(self):
        self.file_formats = []
        self.sample_rates = []

    def set_criteria(self, file_formats, sample_rates):
        """Sets the compatibility criteria based on user input.

        Args:
            file_formats (list): A list of acceptable file formats.
            sample_rates (list): A list of acceptable sample rates.
        """
        self.file_formats = file_formats
        self.sample_rates = sample_rates

    def get_criteria(self):
        """Retrieves the current compatibility criteria.

        Returns:
            dict: The current set of compatibility criteria.
        """
        return {
            'file_formats': self.file_formats,
            'sample_rates': self.sample_rates
        }
