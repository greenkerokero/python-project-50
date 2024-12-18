"""Module provides function to format diff string in stylish format."""


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


def format_stylish(diff_tree):
    """Retrun formated string diff.

    Args:
        diff_tree: Dictionary contains tree of differences
                   between two another dictionaries

    Returns:
        String contain differences in given format
    """
    def inner(inner_data, depth):
        if not isinstance(inner_data, dict):
            return convert_to_string(inner_data)

        replacer = '    '
        indent = replacer * depth
        child_ident_size = depth + 1
        child_ident = replacer * child_ident_size
        child_ident_cut = replacer * (child_ident_size - 1)

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


# def format_stylish1(diff_tree):
#     """Retrun formated string diff.

#     Args:
#         diff_tree: Dictionary contains tree of differences
#                    between two another dictionaries

#     Returns:
#         String contain differences in given format
#     """
#     def inner(inner_data, depth):
#         if not isinstance(inner_data, dict):
#             return convert_to_string(inner_data)

#         replacer = '    '
#         indent = replacer * depth
#         child_ident_size = depth + 1
#         child_ident = replacer * child_ident_size
#         child_ident_cut = replacer * (child_ident_size - 1)
#         some_list = []
#         children = []
#         in_item = inner_data.items()
#         l_in_item = list(in_item)
#         for key, node in in_item:
#             key_indent = child_ident + key
#             add_key_indent = child_ident_cut + '  + ' + key
#             delete_key_indent = child_ident_cut + '  - ' + key

#             some_list.append(
#             [inner(node, child_ident_size) for key, node in in_item])
#             qwe = inner(node, child_ident_size)
#             string = f'{key_indent}: {qwe}'
#             if not isinstance(node, dict):
#                 children.append(string)
#                 diff_list = ['{'] + children + [indent + '}']
#                 return '\n'.join(diff_list)

#             current_type = node.get('type')
#             current_value = node.get('value')
#             current_old = node.get('old')
#             current_new = node.get('new')
#             if current_type == 'nested':
#                 string = (
#                     f'{key_indent}: '
#                     f'{inner(current_value, child_ident_size)}'
#                 )
#             elif current_type == 'added':
#                 string = (
#                     f'{add_key_indent}: '
#                     f'{inner(current_value, child_ident_size)}'
#                 )
#             elif current_type == 'deleted':
#                 string = (
#                     f'{delete_key_indent}: '
#                     f'{inner(current_value, child_ident_size)}'
#                 )
#             elif current_type == 'changed':
#                 string_del = (
#                     f'{delete_key_indent}: '
#                     f'{inner(current_old, child_ident_size)}'
#                 )
#                 string_add = (
#                     f'{add_key_indent}: '
#                     f'{inner(current_new, child_ident_size)}'
#                 )
#                 string = f'{string_del}\n{string_add}'
#             elif current_type == 'unchanged':
#                 string = (
#                     f'{key_indent}: '
#                     f'{inner(current_value, child_ident_size)}'
#                 )
#             children.append(string)
#         diff_list = ['{'] + children + [indent + '}']
#         return '\n'.join(diff_list)
#     return inner(diff_tree, 0)
