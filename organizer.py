import os
import shutil

class Organizer:
    def organize_files(self, files, organization_method):
        # Organize files into folders based on user input or templates
        for file in files:
            # Extract the organization criteria from the file's metadata or filename
            # For simplicity, let's assume we're organizing by genre which is part of the filename
            genre = os.path.basename(file).split('-')[0].strip()
            destination_folder = os.path.join('organized', organization_method, genre)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file, destination_folder)
