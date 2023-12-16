# Local DJ Music Library Management System

This system is designed to help DJs organize and manage their music libraries on their laptops, ensuring compatibility with DJ equipment.

## Features

- Lightweight, executable script to sort music files by compatibility.
- Simple system for organizing music files, ensuring easy access during DJ sets.
- Runs locally on a laptop without the need for complex setups or external dependencies.
- Uses Python 3.x for the programming language.
- Utilizes Python's built-in libraries (os, shutil) for file operations.
- Employs pydub for reading audio file metadata to determine compatibility.
- Command-line interface (CLI) for user input.
- Organizes files into user-defined folders based on genre, BPM, or key.
- Basic logging of operations for user review.
- Basic error handling for common issues.

## How to Use

1. Run the script `main.py` from the command line.
2. Follow the on-screen instructions to input compatibility criteria and organization preferences.
3. Provide the path to your music directory when prompted.
4. The script will scan the directory, filter compatible files, and organize them accordingly.
5. Review the `activity.log` file for a record of operations performed by the script.

## Requirements

- Python 3.x
- pydub library

## Setup

1. Ensure Python 3.x is installed on your laptop.
2. Install the pydub library using `pip install pydub`.
3. Clone or download this repository to your local machine.
4. Navigate to the script's directory and run `python3 main.py`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
