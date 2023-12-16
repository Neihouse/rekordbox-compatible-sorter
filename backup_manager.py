import os
import shutil
from datetime import datetime

class BackupManager:
    def __init__(self, backup_path):
        self.backup_path = backup_path
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)

    def create_backup(self, music_directory):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_folder = os.path.join(self.backup_path, f'backup_{timestamp}')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        for item in os.listdir(music_directory):
            s = os.path.join(music_directory, item)
            d = os.path.join(backup_folder, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

    def restore_backup(self, backup_folder):
        music_directory = os.path.dirname(self.backup_path)
        if os.path.exists(music_directory):
            shutil.rmtree(music_directory)
        shutil.copytree(backup_folder, music_directory)
