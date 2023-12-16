# Local DJ Music Library Management System

This system is designed to help DJs organize and manage their music libraries on their laptops, ensuring compatibility with DJ equipment.

## Features

- Lightweight, executable script to sort music files by compatibility.
- Simple system for organizing music files for easy access during DJ sets.
- Runs locally on a laptop without the need for complex setups or external dependencies.
- Uses Python's built-in libraries and pydub for audio file metadata reading.
- Command-line interface for inputting compatibility criteria.
- Organizes files into user-defined folders based on genre, BPM, or key.
- Basic logging of operations.

## Requirements

- Python 3.x
- pydub library

## Usage

1. Input compatibility criteria through the CLI.
2. The script scans the specified music directory.
3. Files that match the criteria are segregated and organized.
4. Actions are logged for user review.

## Setup

1. Install Python 3.x on your laptop.
2. Install the pydub library using `pip install pydub`.
3. Run the script from the command line with the required arguments.

## Error Handling

The system includes basic error handling for common issues such as file access permissions, non-existent directories, and unsupported file formats.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.