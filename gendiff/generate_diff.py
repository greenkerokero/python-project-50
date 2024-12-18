"""Generate diff tow json or yaml files in specified format."""


from gendiff.file_processing import get_data_from_file, get_file_extension
from gendiff.formatting import diff_formater
from gendiff.make_diff_tree import build_diff_tree
from gendiff.parsing import parse_structured_string


def generate_diff(path_to_file1, path_to_file2, format_name):
    """Generate diff tow json or yaml files in specified format.

    Args:
        path_to_file1: Path to first file
        path_to_file2: Pash to second file
        format_name: Name of format in which you want to get result

    Returns:
        String contains diff in specified format
    """
    string1 = get_data_from_file(path_to_file1)
    string2 = get_data_from_file(path_to_file2)

    extension1 = get_file_extension(path_to_file1)
    extension2 = get_file_extension(path_to_file2)

    dict1 = parse_structured_string(string1, extension1)
    dict2 = parse_structured_string(string2, extension2)

    diff_tree = build_diff_tree(dict1, dict2)

    return diff_formater(diff_tree, format_name)
