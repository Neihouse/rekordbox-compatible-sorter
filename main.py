from cli_interface import CLIInterface
from music_library_manager import MusicLibraryManager
from compatibility_checker import CompatibilityChecker
from organizer import Organizer
from logger import Logger
from error_handler import ErrorHandler
import sys


def main():
    cli_interface = CLIInterface()
    music_manager = MusicLibraryManager()
    compatibility_checker = CompatibilityChecker()
    organizer = Organizer()
    logger = Logger()
    error_handler = ErrorHandler()

    try:
        # Display instructions to the user
        cli_interface.display_instructions()

        # Get user input for compatibility criteria and organization preferences
        criteria = cli_interface.get_user_input()

        # Validate and set acceptable formats for the MusicLibraryManager
        music_manager.acceptable_formats = [fmt.strip().lower() for fmt in criteria['acceptable_formats'] if fmt.strip()]

        # Get the music directory from the user
        music_directory = input('Enter the path to your music directory: ').strip()
        if not music_directory:
            print('Music directory path is required.')
            sys.exit(1)

        # Scan the music directory
        files = music_manager.scan_directory(music_directory)

        # Filter compatible files
        compatible_files = music_manager.filter_compatible_files(files, criteria)

        # Organize files
        organizer.organize_files(compatible_files, criteria['organization_method'])

        # Log the operation
        logger.log_operation('Music library organized successfully.')

    except Exception as e:
        # Handle any errors that occur
        error_handler.handle_error(e)


if __name__ == '__main__':
    main()
