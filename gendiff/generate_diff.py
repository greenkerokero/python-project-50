"""Generate diff tow json or yaml files in specified format."""


from gendiff.file_processing import get_data_from_file
from gendiff.file_processing import get_file_extension
from gendiff.parsing import parse_structured_string
from gendiff.makediff import build_diff_tree
from gendiff.formater import format_diff


def generate_diff(path_to_file1, path_to_file2, format_name):
    """Generate diff tow json or yaml files in specified format.

    Args:
        path_to_file1: Path to first file
        path_to_file2: Pash to second file
        format_name: Name of format in which you want to get result

    Returns:
        String contains diif in specified formt
    """
    string1 = get_data_from_file(path_to_file1)
    string2 = get_data_from_file(path_to_file2)

    extension1 = get_file_extension(path_to_file1)
    extension2 = get_file_extension(path_to_file2)

    dict1 = parse_structured_string(string1, extension1)
    dict2 = parse_structured_string(string2, extension2)

    diff_tree = build_diff_tree(dict1, dict2)

    return format_diff(diff_tree, format_name)
