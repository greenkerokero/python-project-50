"""Module provides function to format diff string in stylish format."""

from gendiff import constants

REPLACER = '    '


def convert_to_string(inner_data):
    """Convert data to string and boolen and none types in special stinrgs.

    Args:
        inner_data: any build-in data

    Returns:
        Convert to string data
    """
    if inner_data is True:
        return 'true'
    elif inner_data is False:
        return 'false'
    elif inner_data is None:
        return 'null'
    return inner_data


def format_stylish(diff_tree):
    """Retrun string diff in stylish format.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries

    Returns:
        String contain differences in stylish format
    """
    def inner(inner_data, depth):
        if not isinstance(inner_data, dict):
            return convert_to_string(inner_data)

        indent = REPLACER * depth
        child_ident_size = depth + 1
        child_ident = REPLACER * child_ident_size
        child_ident_cut = REPLACER * (child_ident_size - 1)

        children = []
        for key, node in inner_data.items():
            key_indent = child_ident + key
            add_key_indent = child_ident_cut + '  + ' + key
            delete_key_indent = child_ident_cut + '  - ' + key
            if isinstance(node, dict):
                current_type = node.get('type')
                current_value = node.get('value')
                if current_type in {constants.NESTED, constants.UNCHANGED}:
                    string = (
                        f'{key_indent}: '
                        f'{inner(current_value, child_ident_size)}'
                    )
                elif current_type == constants.ADDED:
                    string = (
                        f'{add_key_indent}: '
                        f'{inner(current_value, child_ident_size)}'
                    )
                elif current_type == constants.DELETED:
                    string = (
                        f'{delete_key_indent}: '
                        f'{inner(current_value, child_ident_size)}'
                    )
                elif current_type == constants.CHANGED:
                    string_del = (
                        f'{delete_key_indent}: '
                        f'{inner(node.get("old"), child_ident_size)}'
                    )
                    string_add = (
                        f'{add_key_indent}: '
                        f'{inner(node.get("new"), child_ident_size)}'
                    )
                    string = f'{string_del}\n{string_add}'
                else:
                    string = f'{key_indent}: {inner(node, child_ident_size)}'
            else:
                string = f'{key_indent}: {inner(node, child_ident_size)}'
            children.append(string)

        diff_list = ['{'] + children + [indent + '}']
        return '\n'.join(diff_list)
    return inner(diff_tree, 0)
