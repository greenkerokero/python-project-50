
"""Test makediff module."""

import os

from pytest import mark
from gendiff.generate_diff import generate_diff


def get_fixture_path(name):
    """Return path from project root to fixture.

    Args:
        name: fixture name

    Returns:
        Path from project root to fixture
    """
    return os.path.join('gendiff/tests/fixtures', name)


def open_file(path):
    """
    Open file and return it content as string.

    Args:
        path: path to file

    Returns:
        File content as string
    """
    with open(path, encoding='utf8') as fl:
        return fl.read().strip()


# def test_diff_flat_json():
#     """Check that flat json files are compare correctly."""
#     filepath1 = get_fixture_path('flat_file1.json')
#     filepath2 = get_fixture_path('flat_file2.json')
#     format_name = 'stylish'
#     correct_diff_path = get_fixture_path('diff_result_stylish_flat_json')
#     correct = open_file(correct_diff_path)
#     diff = generate_diff(filepath1, filepath2, format_name)
#     assert correct == diff


# def test_diff_flat_yaml():
#     """Check that flat yaml files are compare correctly."""
#     filepath1 = get_fixture_path('flat_file1.yaml')
#     filepath2 = get_fixture_path('flat_file2.yaml')
#     format_name = 'stylish'
#     correct_diff_path = get_fixture_path('diff_result_stylish_flat_yaml')
#     correct = open_file(correct_diff_path)
#     diff = generate_diff(filepath1, filepath2, format_name)
#     assert correct == diff


# def test_diff_nested_json():
#     """Check that nested json files are compare correctly."""
#     filepath1 = get_fixture_path('nested_file1.json')
#     filepath2 = get_fixture_path('nested_file2.json')
#     format_name = 'stylish'
#     correct_diff_path = get_fixture_path('diff_result_stylish_nested_json')
#     correct = open_file(correct_diff_path)
#     diff = generate_diff(filepath1, filepath2, format_name)
#     assert correct == diff


# def test_diff_nested_yaml():
#     """Check that nested yaml files are compare correctly."""
#     filepath1 = get_fixture_path('nested_file1.yaml')
#     filepath2 = get_fixture_path('nested_file2.yaml')
#     format_name = 'stylish'
#     correct_diff_path = get_fixture_path('diff_result_stylish_nested_yaml')
#     correct = open_file(correct_diff_path)
#     diff = generate_diff(filepath1, filepath2, format_name)
#     assert correct == diff


@mark.parametrize(
    'format_name,filepath1,filepath2,correct_diff_path',
    [
        (
            'stylish',
            get_fixture_path('flat_file1.json'),
            get_fixture_path('flat_file2.json'),
            get_fixture_path('diff_result_stylish_flat'),
        ),
        (
            'stylish',
            get_fixture_path('flat_file1.yaml'),
            get_fixture_path('flat_file2.yaml'),
            get_fixture_path('diff_result_stylish_flat'),
        ),
        (
            'stylish',
            get_fixture_path('nested_file1.json'),
            get_fixture_path('nested_file2.json'),
            get_fixture_path('diff_result_stylish_nested'),
        ),
        (
            'stylish',
            get_fixture_path('nested_file1.yaml'),
            get_fixture_path('nested_file2.yaml'),
            get_fixture_path('diff_result_stylish_nested'),
        ),
        (
            'plain',
            get_fixture_path('nested_file1.json'),
            get_fixture_path('nested_file2.json'),
            get_fixture_path('diff_result_plain_nested'),
        ),
        (
            'plain',
            get_fixture_path('nested_file1.yaml'),
            get_fixture_path('nested_file2.yaml'),
            get_fixture_path('diff_result_plain_nested'),
        ),
    ],
)
def test_param(format_name, filepath1, filepath2, correct_diff_path):
    """Check that files are compare correctly.

    Args:
        format_name: Name of format in which you want to get result
        filepath1: Path to first file
        filepath2: Path to first file
        correct_diff_path: Path to file containing correct compare result
    """
    correct = open_file(correct_diff_path)
    diff = generate_diff(filepath1, filepath2, format_name)
    assert correct == diff
