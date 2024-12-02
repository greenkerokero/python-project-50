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