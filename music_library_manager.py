import os
from pydub import AudioSegment

class MusicLibraryManager:
    def scan_directory(self, directory):
        # Scan the specified music directory for audio files
        audio_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(tuple(self.acceptable_formats)):
                    audio_files.append(os.path.join(root, file))
        return audio_files

    def filter_compatible_files(self, files, criteria):
        # Filter files based on user-defined compatibility criteria
        compatible_files = []
        for file in files:
            audio_file = AudioSegment.from_file(file)
            if audio_file.frame_rate in criteria['sample_rates']:
                compatible_files.append(file)
        return compatible_files
