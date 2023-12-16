from pydub import AudioSegment

# Compatibility Checker for audio files

class CompatibilityChecker:
    def __init__(self, criteria):
        self.criteria = criteria

    def check_file(self, file_path):
        """Checks if the audio file meets the compatibility criteria.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            bool: True if the file is compatible, False otherwise.
        """
        audio_file = AudioSegment.from_file(file_path)
        file_format = file_path.split('.')[-1].lower()
        sample_rate = audio_file.frame_rate
        return file_format in self.criteria['file_formats'] and sample_rate in self.criteria['sample_rates']
