"""Generate difference between two json or yaml files.

Takes paths to files as input and
outputs the difference between them as string.
"""

from gendiff.parsing import parse


def get_file_extension(path):
    """Get file extension from path to file.

    Args:
        path: Path to file

    Returns:
        String with extension of file. If extension not exist - empty string
    """
    file_name = path.split('/')[-1]
    split_file_name = file_name.split('.')
    if len(split_file_name) < 2:
        return ''
    return split_file_name[-1]


def bool_to_lowercase(input_value):
    """If input value is boolean convert it to string in lowercase.

    Args:
        input_value: Any value

    Returns:
        String in lowercase if input is boolean, in other case input_value
    """
    if isinstance(input_value, bool):
        return str(input_value).lower()
    return input_value


def build_diff_tree(first_dict, second_dict):
    def inner(first, second):
        inner_repr = {}
        keys = first.keys() | second.keys()
        keys = sorted(keys)
        for key in keys:
            if key not in first:
                inner_repr[key] = {
                    'type': 'added',
                    'value': second[key],
                }
            elif key not in second:
                inner_repr[key] = {
                    'type': 'deleted',
                    'value': first[key],
                }
            elif first[key] == second[key]:
                inner_repr[key] = {
                    'type': 'unchanged',
                    'value': first[key],
                }
            elif isinstance(first[key], dict) and isinstance(second[key], dict):
                inner_repr[key] = {
                    'type': 'nested',
                    'value': inner(first[key], second[key]),
                }
            else:
                inner_repr[key] = {
                    'type': 'changed',
                    'old': first[key],
                    'new': second[key],
                }
        return inner_repr
    return inner(first_dict, second_dict)


def make_diff(file_path1, file_path2):
    """Generate difference between two json or yaml files.

    Args:
        file_path1: Path to first file
        file_path2: Path to second file

    Returns:
        String contains difference between two files located at paths
        in file_path1 and file_path2
    """
    with open(file_path1, 'r') as first_file:
        first_list = [line for line in first_file]
        first_data = ''.join(first_list)
    with open(file_path2, 'r') as second_file:
        second_list = [line for line in second_file]
        second_data = ''.join(second_list)
    extention = get_file_extension(file_path1)
    first_dict = parse(first_data, extention)
    second_dict = parse(second_data, extention)

    keys = first_dict.keys() | second_dict.keys()
    keys = sorted(keys)
    diff_list = ['{']
    for key in keys:
        if key not in first_dict:
            second_dict_value = bool_to_lowercase(second_dict[key])
            diff_list.append(f'  + {key}: {second_dict_value}')
        elif key not in second_dict:
            first_dict_value = bool_to_lowercase(first_dict[key])
            diff_list.append(f'  - {key}: {first_dict_value}')
        elif first_dict[key] == second_dict[key]:
            first_dict_value = bool_to_lowercase(first_dict[key])
            diff_list.append(f'    {key}: {first_dict_value}')
        else:
            first_dict_value = bool_to_lowercase(first_dict[key])
            second_dict_value = bool_to_lowercase(second_dict[key])
            diff_list.append(f'  - {key}: {first_dict_value}')
            diff_list.append(f'  + {key}: {second_dict_value}')
    diff_list.append('}')
    return '\n'.join(diff_list)
