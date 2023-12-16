from pydub import AudioSegment
from error_handler import ErrorHandler
import os

class TrackSortingService:
    def __init__(self, compatibility_criteria):
        self.compatibility_criteria = compatibility_criteria

    def scan_directory(self, directory):
        # Recursively scan the specified music directory for files
        return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if not f.startswith('.') and not f.endswith('.pyc') and not f.endswith('.py')]

    def check_compatibility(self, file_path):
        # Check if a file meets the compatibility criteria
        try:
            audio_file = AudioSegment.from_file(file_path)
            file_format = os.path.splitext(file_path)[1][1:].lower()
            sample_rate = audio_file.frame_rate
            return file_format in self.compatibility_criteria['file_formats'] and sample_rate in self.compatibility_criteria['sample_rates']
        except Exception as e:
            # Handle unsupported file formats and other exceptions
            ErrorHandler.handle_error(f'Unsupported file format or error processing file: {file_path}')
            return False

    def sort_files(self, directory):
        # Organize files into folders based on user-defined criteria
        compatible_files = []
        files = self.scan_directory(directory)
        for file_path in files:
            if self.check_compatibility(file_path):
                compatible_files.append(file_path)
        return compatible_files
