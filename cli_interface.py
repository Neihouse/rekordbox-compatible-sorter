import re

class CLIInterface:
    def get_user_input(self):
        # Capture compatibility criteria and organization preferences from the user
        criteria = {}
        criteria['acceptable_formats'] = input('Enter acceptable file formats (comma separated, e.g., mp3, wav): ').split(',')
        criteria['sample_rates'] = list(map(int, input('Enter acceptable sample rates (comma separated, e.g., 44100, 48000): ').split(',')))
        criteria['organization_method'] = input('Enter organization method (e.g., genre, BPM, key): ')
        return criteria

    def display_instructions(self):
        # Guide the user through the input process
        print('Welcome to the Local DJ Music Library Management System.')
        print('Please enter the compatibility criteria and organization preferences.')
