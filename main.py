from cli_interface import CLIInterface
from compatibility_manager import CompatibilityCriteria
from organizer import Organizer
from logger import Logger
from error_handler import ErrorHandler
from sorting_engine import MusicSorter
import os

# Main script to orchestrate the execution

def main():
    # Initialize logger
    logger = Logger('activity.log')

    # Get user input for compatibility criteria
    criteria = CLIInterface.get_user_input()
    compatibility_criteria = CompatibilityCriteria()
    compatibility_criteria.set_criteria(criteria['file_formats'], criteria['sample_rates'])

    # Initialize the MusicSorter with the user-defined criteria
    music_sorter = MusicSorter(compatibility_criteria.get_criteria(), os.getcwd())

    # Scan and sort files
    sorted_files = music_sorter.sort_files()

    # Get user input for organization
    # Get user input for organization criteria
    print("Please enter the destination folder name: ", end='')
    destination_folder = input().strip()
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Organize files
    organizer = Organizer()
    organizer.organize_files(sorted_files, destination_folder)

    # Log the operation
    logger.log_operation(f'Organized files into {destination_folder}')

    # Error handling example
    try:
        # Placeholder for a potential operation that could fail
        pass
    except Exception as e:
        ErrorHandler.handle_error(str(e))
        logger.log_operation(f'Error occurred: {e}')

if __name__ == '__main__':
    main()
