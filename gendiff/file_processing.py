"""Module contains functions for working with files."""

from pathlib import PurePath

from gendiff.parsing import parse_structured_string


def get_file_extension(file_path):
    """Get file extension from file path.

    Args:
        file_path: Path to file

    Returns:
        Strings with file file extension
    """
    path = PurePath(file_path)
    return path.suffix.lower()[1:]


def parse_file(file_path):
    """Parse structured text file.

    Args:
        file_path: Path to file

    Returns:
        Dictionary containing data from structured text file
    """
    with open(file_path, 'r') as text_file:
        file_data = text_file.read()

    extension = get_file_extension(file_path)
    return parse_structured_string(file_data, extension)
