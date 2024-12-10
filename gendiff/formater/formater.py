from gendiff.formater.plain import format_plain
from gendiff.formater.stylish import format_stylish


def diff_formater(diff_tree, format_name):
    match format_name:
        case 'stylish':
            return format_stylish(diff_tree)
        case 'plain':
            return format_plain(diff_tree)
        case _:
            return 'Unknown format'
