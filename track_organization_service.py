import os
import shutil
from error_handler import ErrorHandler

class TrackOrganizationService:
    def __init__(self):
        pass

    def organize_files(self, sorted_files, destination_folder):
        # Organize the sorted files into the destination folder
        try:
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            for file_path in sorted_files:
                shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))
        except Exception as e:
            ErrorHandler.handle_error(f'Error organizing files: {e}')
