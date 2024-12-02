from gendiff.file_processing import get_data_from_file
from gendiff.file_processing import get_file_extension
from gendiff.parsing import parse
from gendiff.makediff import build_diff_tree
from gendiff.formater import format_diff


def generate_diff(path_to_file1, path_to_file2, format_name='stylish'):
    string1 = get_data_from_file(path_to_file1)
    string2 = get_data_from_file(path_to_file2)

    extension1 = get_file_extension(path_to_file1)
    extension2 = get_file_extension(path_to_file2)

    dict1 = parse(string1, extension1)
    dict2 = parse(string2, extension2)

    diff_tree = build_diff_tree(dict1, dict2)

    final_diff_string = format_diff(diff_tree, format_name)

    return final_diff_string
