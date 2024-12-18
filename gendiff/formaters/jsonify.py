"""Module provides function to format diff string in json format."""

from json import dumps as json_dumps


def format_json(diff_tree):
    """Retrun string diff in stylish json.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries

    Returns:
        String contain differences in json format
    """
    return json_dumps(diff_tree, indent=4)
