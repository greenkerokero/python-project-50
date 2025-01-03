"""Module provides function to format diff string in plain format."""
from json import dumps as json_dumps


def convert_to_string(inner_data):
    """Convert data to string and boolen and none types in special stinrgs.

    Args:
        inner_data: any build-in data

    Returns:
        Convert to string data
    """
    if isinstance(inner_data, dict):
        return '[complex value]'
    elif isinstance(inner_data, bool) or inner_data is None:
        return json_dumps(inner_data)
    elif isinstance(inner_data, int):
        return inner_data
    return f"'{inner_data}'"


def format_plain(diff_tree):
    """Retrun string diff in plain format.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries

    Returns:
        String contain differences in plain format
    """
    def inner(inner_data, node_path):
        if not isinstance(inner_data, dict):
            return convert_to_string(inner_data)
        children = []
        for key, node in inner_data.items():
            string = '[complex value]'
            # Добавить в новый список new_node_path
            # элементы старого списка node_path
            # с помощью оператора распаковки *
            # и значение текщего ключа
            new_node_path = [*node_path, key]
            path_in_string = f"'{'.'.join(new_node_path)}'"
            if not isinstance(node, dict):
                children.append(string)
                return '\n'.join(children)
            current_type = node.get('type')
            current_value = node.get('value')
            current_old = node.get('old')
            current_new = node.get('new')
            match current_type:
                case 'nested':
                    string = inner(current_value, new_node_path)
                case 'added':
                    value_add = convert_to_string(current_value)
                    string = (
                        f'Property {path_in_string} was added '
                        f'with value: {value_add}'
                    )
                case 'deleted':
                    string = f'Property {path_in_string} was removed'
                case 'changed':
                    value_old = convert_to_string(current_old)
                    value_new = convert_to_string(current_new)
                    string = (
                        f'Property {path_in_string} was updated. '
                        f'From {value_old} to {value_new}'
                    )
                case 'unchanged':
                    continue
            children.append(string)
        return '\n'.join(children)
    return inner(diff_tree, [])
