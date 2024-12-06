"""Module contains functions for working with files."""


from pathlib import PurePath


def get_data_from_file(file_path):
    """Open file safely and returns its contents.

    Args:
        file_path: Path to file

    Returns:
        String with file contents
    """
    with open(file_path, 'r') as text_file:
        # lines_list = [line for line in text_file]
        # return ''.join(lines_list)
        return text_file.read()


def get_file_extension(file_path):
    """Get file extension from file path.

    Args:
        file_path: Path to file

    Returns:
        Strings with file file extension
    """
    path = PurePath(file_path)
    return path.suffix.lower()[1:]
