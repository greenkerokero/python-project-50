"""Retrun formated string diff."""


def convert_to_string(inner_data):
    """Convert data to string and boolen and none types in special stinrgs.

    Args:
        inner_data: any build-in data

    Returns:
        Convert to string data
    """
    match inner_data:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return str(inner_data)


def format_stylish(diff_tree, output_format='stylish'):
    """Retrun formated string diff.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries
        output_format: Differences format in which resulting
                       string is output

    Returns:
        String contain differences in given format
    """
    # match output_format:
    #     case 'stylish':
    #         replacer = '    '
    #         replacers_count = 1
    #         add_symbol = '  + '
    #         delete_symbol = '  - '
    #     case _:
    #         return 'Unknown format'

    def inner(inner_data, depth):
        if not isinstance(inner_data, dict):
            return convert_to_string(inner_data)

        replacer = '    '
        indent = replacer * depth
        child_ident_size = depth + 1
        child_ident = replacer * child_ident_size
        child_ident_cut = replacer * (child_ident_size - 1)

        # indent = replacer * depth
        # child_ident_size = depth + replacers_count
        # child_ident = replacer * child_ident_size
        # child_ident_cut = replacer * (child_ident_size - 1)

        children = []
        for key, node in inner_data.items():
            key_indent = child_ident + key
            add_key_indent = child_ident_cut + '  + ' + key
            delete_key_indent = child_ident_cut + '  - ' + key
            if isinstance(node, dict):
                current_type = node.get('type')
                current_value = node.get('value')
                current_old = node.get('old')
                current_new = node.get('new')
                # match current_type:
                #     case 'nested' | 'unchanged':
                #         string = (
                #             f'{key_indent}: '
                #             f'{inner(current_value, child_ident_size)}'
                #         )
                #     case 'added':
                #         string = (
                #             f'{add_key_indent}: '
                #             f'{inner(current_value, child_ident_size)}'
                #         )
                #     case 'deleted':
                #         string = (
                #             f'{delete_key_indent}: '
                #             f'{inner(current_value, child_ident_size)}'
                #         )
                #     case 'changed':
                #         string_del = (
                #             f'{delete_key_indent}: '
                #             f'{inner(current_value, child_ident_size)}'
                #         )
                #         string_add = (
                #             f'{add_key_indent}: '
                #             f'{inner(current_value, child_ident_size)}'
                #         )
                #         string = f'{string_del}\n{string_add}'
                #     case _:
                #         string = (
                #             f'{key_indent}: '
                #             f'{inner(node, child_ident_size)}'
                #         )
                if current_type in {'nested', 'unchanged'}:
                    string = (
                        f'{key_indent}: '
                        f'{inner(current_value, child_ident_size)}'
                    )
                elif current_type == 'added':
                    string = (
                        f'{add_key_indent}: '
                        f'{inner(current_value, child_ident_size)}'
                    )
                elif current_type == 'deleted':
                    string = (
                        f'{delete_key_indent}: '
                        f'{inner(current_value, child_ident_size)}'
                    )
                elif current_type == 'changed':
                    string_del = (
                        f'{delete_key_indent}: '
                        f'{inner(current_old, child_ident_size)}'
                    )
                    string_add = (
                        f'{add_key_indent}: '
                        f'{inner(current_new, child_ident_size)}'
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
