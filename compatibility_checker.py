import os
import shutil
from pydub.utils import mediainfo

# Constants
SOURCE_DIR = '/mnt/data/chanceneihouse'  # Source folder path
DESTINATION_DIR = '/mnt/data/rekordbox_compatible'  # Destination folder path
COMPATIBLE_FORMATS = {
    '.flac': ['44100', '48000', '88200', '96000'],
    '.m4a': ['44100', '48000', '88200', '96000'],
    '.wav': ['88200', '96000'],
    '.aiff': ['88200', '96000']
}

# Function to create the destination directory if it doesn't exist
def create_destination_dir():
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)

# Function to get the file extension of a given file path
def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()

# Function to get the sample rate of a given audio file
def get_sample_rate(file_path):
    info = mediainfo(file_path)
    return info.get('sample_rate', None)

# Function to check if a file is in a compatible format and sample rate
def is_compatible(file_path):
    extension = get_file_extension(file_path)
    if extension in COMPATIBLE_FORMATS:
        sample_rate = get_sample_rate(file_path)
        return sample_rate in COMPATIBLE_FORMATS[extension]
    return False

# Function to scan the source directory, check each file for compatibility, and move compatible files
def move_compatible_files():
    create_destination_dir()
    compatible_files = []
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if is_compatible(file_path):
                compatible_files.append(file_path)
                shutil.move(file_path, os.path.join(DESTINATION_DIR, file))
    return compatible_files

# Main function to orchestrate the execution
def main():
    compatible_files = move_compatible_files()
    print(f'Compatible files moved: {compatible_files}')

if __name__ == '__main__':
    main()
