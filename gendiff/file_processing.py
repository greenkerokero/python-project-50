from pathlib import PurePath


def get_data_from_file(file_path):
    with open(file_path, 'r') as text_file:
        #lines_list = [line for line in text_file]
        #return ''.join(lines_list)
        return text_file.read()


def get_file_extension(file_path):
    path = PurePath(file_path)
    return path.suffix.lower()[1:]
