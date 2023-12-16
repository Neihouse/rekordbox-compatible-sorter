# Local DJ Music Library Management System

This system is designed to help DJs automatically organize and manage their music libraries on their laptops, ensuring compatibility with DJ equipment.

## Features

- Lightweight, executable script to sort music files by compatibility.
- Simple system for organizing music files into user-defined folders based on genre, BPM, or key.
- Standalone script that runs locally on a laptop with minimal setup.

## Requirements

- Python 3.x
- `os`, `shutil` for file operations
- `pydub` for reading audio file metadata

## Usage

1. Run `main.py` through the command line.
2. Input compatibility criteria when prompted.
3. Specify the music directory to be organized.
4. The script will scan the directory, identify compatible files, and organize them based on the input criteria.

## Logging

The script logs its operations to `activity.log`, which can be reviewed for a summary of actions taken.

## Error Handling

The script includes basic error handling for common issues such as file access permissions, non-existent directories, and unsupported file formats.

## Development

To contribute to this project, please create a branch and submit a pull request for review.