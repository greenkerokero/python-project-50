from json import load


def bool_to_lowercase(input_value):
    if isinstance(input_value, bool):
        return str(input_value).lower()
    return input_value


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as json_data1:
        first_data = load(json_data1)
    with open(file_path2, 'r') as json_data2:
        second_data = load(json_data2)

    keys = first_data.keys() | second_data.keys()
    keys = sorted(keys)
    #output = '{'
    #for key in keys:
    #    if key not in first_data:
    #        second_data_value = bool_to_lowercase(second_data[key])
    #        output = f'{output}\n  + {key}: {second_data_value}'
    #    elif key not in second_data:
    #        first_data_value = bool_to_lowercase(first_data[key])
    #        output = f'{output}\n  - {key}: {first_data_value}'
    #    elif first_data[key] == second_data[key]:
    #        first_data_value = bool_to_lowercase(first_data[key])
    #        output = f'{output}\n    {key}: {first_data_value}'
    #    else:
    #        first_data_value = bool_to_lowercase(first_data[key])
    #        second_data_value = bool_to_lowercase(second_data[key])
    #        output =f'{output}\n  - {key}: {first_data_value}\n  + {key}: {second_data_value}'
    #output = output + '\n}'
    diff_list = ['{']
    for key in keys:
        if key not in first_data:
            second_data_value = bool_to_lowercase(second_data[key])
            diff_list.append(f'  + {key}: {second_data_value}')
        elif key not in second_data:
            first_data_value = bool_to_lowercase(first_data[key])
            diff_list.append(f'  - {key}: {first_data_value}')
        elif first_data[key] == second_data[key]:
            first_data_value = bool_to_lowercase(first_data[key])
            diff_list.append(f'    {key}: {first_data_value}')
        else:
            first_data_value = bool_to_lowercase(first_data[key])
            second_data_value = bool_to_lowercase(second_data[key])
            diff_list.append(f'  - {key}: {first_data_value}')
            diff_list.append(f'  + {key}: {second_data_value}')
    diff_list.append('}')
    return '\n'.join(diff_list)
