"""Module provides function to format diff string in selected format."""

from gendiff.formaters.jsonify import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish


def diff_formater(diff_tree, format_name='stylish'):
    """Format diff sting in selected format.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries
        format_name: Name of format in which you want to get result

    Returns:
        String contains diff in specified format
    """
    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    return 'Unknown format'
