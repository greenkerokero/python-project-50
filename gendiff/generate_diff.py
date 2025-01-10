"""Generate diff tow json or yaml files in specified format."""


from gendiff.file_processing import parse_file
from gendiff.formatting import diff_formater
from gendiff.make_diff_tree import build_diff_tree


def generate_diff(path_to_file1, path_to_file2, format_name='stylish'):
    """Generate diff tow json or yaml files in specified format.

    Args:
        path_to_file1: Path to first file
        path_to_file2: Pash to second file
        format_name: Name of format in which you want to get result

    Returns:
        String contains diff in specified format
    """
    dict1 = parse_file(path_to_file1)
    dict2 = parse_file(path_to_file2)

    diff_tree = build_diff_tree(dict1, dict2)

    return diff_formater(diff_tree, format_name)
