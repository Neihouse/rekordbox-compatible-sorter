# Compatibility Manager

class CompatibilityCriteria:
    def __init__(self):
        self.file_formats = []
        self.sample_rates = []

    def set_criteria(self, file_formats, sample_rates):
        # Sets the compatibility criteria based on user input
        self.file_formats = file_formats
        self.sample_rates = sample_rates

    def get_criteria(self):
        # Retrieves the current compatibility criteria
        return {
            'file_formats': self.file_formats,
            'sample_rates': self.sample_rates
        }
