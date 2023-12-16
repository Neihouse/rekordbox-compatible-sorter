import os
import shutil
from pydub import AudioSegment
from error_handler import ErrorHandler

# Organizer for music files

class Organizer:
    def organize_files(self, files, destination_folder):
        """Organizes files into folders based on user input or templates.

        Args:
            files (list): List of file paths to organize.
            destination_folder (str): The destination folder where files will be organized.
        """
        for file in files:
            try:
                # Extract metadata for organization
                audio_file = AudioSegment.from_file(file)
                genre = audio_file.tags.get('genre', 'Unknown')
                bpm = audio_file.tags.get('bpm', 'Unknown')
                key = audio_file.tags.get('key', 'Unknown')

                # Create a folder path based on genre, BPM, and key
                folder_path = os.path.join(destination_folder, genre, f'BPM_{bpm}', key)
                os.makedirs(folder_path, exist_ok=True)

                # Move file to the new folder path
                shutil.move(file, folder_path)
            except Exception as e:
                # Handle issues such as file already exists or permission errors
                ErrorHandler.handle_error(f'Error moving file {file}: {e}')
