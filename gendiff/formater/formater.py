"""Module provides function to format diff string in selected format."""

from gendiff.formater.plain import format_plain
from gendiff.formater.stylish import format_stylish


def diff_formater(diff_tree, format_name):
    """Format diff sting in selected format.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries
        format_name: Name of format in which you want to get result

    Returns:
        String contains diff in specified format
    """
    match format_name:
        case 'stylish':
            return format_stylish(diff_tree)
        case 'plain':
            return format_plain(diff_tree)
        case _:
            return 'Unknown format'
