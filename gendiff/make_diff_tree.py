"""Build diff betwin two dictionary."""

from gendiff import constants


def build_diff_tree(first_dict, second_dict):
    """Build diff betwin two dictionary.

    Args:
        first_dict: some dictionary
        second_dict: some other dictionary

    Returns:
        Dictionary contains tree of differences between two source dictionaries
    """
    def inner(first, second):
        inner_repr = {}
        keys = sorted(first.keys() | second.keys())
        for key in keys:
            if key not in first:
                inner_repr[key] = {
                    'type': constants.ADDED,
                    'value': second[key],
                }
            elif key not in second:
                inner_repr[key] = {
                    'type': constants.DELETED,
                    'value': first[key],
                }
            elif first[key] == second[key]:
                inner_repr[key] = {
                    'type': constants.UNCHANGED,
                    'value': first[key],
                }
            elif isinstance(first[key], dict) and isinstance(second[key], dict):
                inner_repr[key] = {
                    'type': constants.NESTED,
                    'value': inner(first[key], second[key]),
                }
            else:
                inner_repr[key] = {
                    'type': constants.CHANGED,
                    'old': first[key],
                    'new': second[key],
                }
        return inner_repr
    return inner(first_dict, second_dict)
