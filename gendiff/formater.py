from gendiff.makediff import build_diff_tree


def format_diff(diff_tree, output_format='stylish'):
    match output_format:
        case 'stylish':
            replacer = ' '
            replacers_count = 1
            add_symbol = '+'
            remove_delete_symbol = '-'

    def inner(inner_value, depth):
        if not isinstance(inner_value, dict):
            return str(inner_value)

        indent = replacer * depth
        child_ident_size = depth + replacers_count
        child_ident = replacer * child_ident_size

        children = []
        for key, value in inner_value.items():
            string = f'{child_ident}{key}: {inner(value, child_ident_size)}'
            children.append(string)

        result = ['{'] + children + [indent + '}']
        return '\n'.join(result)
    return inner(diff_tree, 0)
