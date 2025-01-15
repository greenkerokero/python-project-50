
"""Test makediff module."""

import os

from gendiff.generate_diff import generate_diff
from pytest import mark


def get_fixture_path(name):
    """Return path from project root to fixture.

    Args:
        name: fixture name

    Returns:
        Path from project root to fixture
    """
    return os.path.join('tests/fixtures', name)


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


@mark.parametrize(
    'format_name,filepath1,filepath2,correct_diff_path',
    [
        (
            'stylish',
            get_fixture_path('flat_file1.json'),
            get_fixture_path('flat_file2.json'),
            get_fixture_path('expected/diff_result_stylish_flat'),
        ),
        (
            'stylish',
            get_fixture_path('flat_file1.yaml'),
            get_fixture_path('flat_file2.yaml'),
            get_fixture_path('expected/diff_result_stylish_flat'),
        ),
        (
            'stylish',
            get_fixture_path('flat_file1.yml'),
            get_fixture_path('flat_file2.yml'),
            get_fixture_path('expected/diff_result_stylish_flat'),
        ),
        (
            'stylish',
            get_fixture_path('nested_file1.json'),
            get_fixture_path('nested_file2.json'),
            get_fixture_path('expected/diff_result_stylish_nested'),
        ),
        (
            'stylish',
            get_fixture_path('nested_file1.yaml'),
            get_fixture_path('nested_file2.yaml'),
            get_fixture_path('expected/diff_result_stylish_nested'),
        ),
        (
            'stylish',
            get_fixture_path('nested_file1.yml'),
            get_fixture_path('nested_file2.yml'),
            get_fixture_path('expected/diff_result_stylish_nested'),
        ),
        (
            'plain',
            get_fixture_path('nested_file1.json'),
            get_fixture_path('nested_file2.json'),
            get_fixture_path('expected/diff_result_plain_nested'),
        ),
        (
            'plain',
            get_fixture_path('nested_file1.yaml'),
            get_fixture_path('nested_file2.yaml'),
            get_fixture_path('expected/diff_result_plain_nested'),
        ),
        (
            'plain',
            get_fixture_path('nested_file1.yml'),
            get_fixture_path('nested_file2.yml'),
            get_fixture_path('expected/diff_result_plain_nested'),
        ),
        (
            'json',
            get_fixture_path('nested_file1.json'),
            get_fixture_path('nested_file2.json'),
            get_fixture_path('expected/diff_result_json_nested'),
        ),
        (
            'json',
            get_fixture_path('nested_file1.yaml'),
            get_fixture_path('nested_file2.yaml'),
            get_fixture_path('expected/diff_result_json_nested'),
        ),
        (
            'json',
            get_fixture_path('nested_file1.yml'),
            get_fixture_path('nested_file2.yml'),
            get_fixture_path('expected/diff_result_json_nested'),
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
    diff = generate_diff(filepath1, filepath2, format_name)
    expected = open_file(correct_diff_path)
    assert diff == expected


@mark.parametrize(
    'filepath1,filepath2,correct_diff_path',
    [
        (
            get_fixture_path('flat_file1.json'),
            get_fixture_path('flat_file2.json'),
            get_fixture_path('expected/diff_result_stylish_flat'),
        ),
        (
            get_fixture_path('flat_file1.yaml'),
            get_fixture_path('flat_file2.yaml'),
            get_fixture_path('expected/diff_result_stylish_flat'),
        ),
        (
            get_fixture_path('flat_file1.yml'),
            get_fixture_path('flat_file2.yml'),
            get_fixture_path('expected/diff_result_stylish_flat'),
        ),
        (
            get_fixture_path('nested_file1.json'),
            get_fixture_path('nested_file2.json'),
            get_fixture_path('expected/diff_result_stylish_nested'),
        ),
        (
            get_fixture_path('nested_file1.yaml'),
            get_fixture_path('nested_file2.yaml'),
            get_fixture_path('expected/diff_result_stylish_nested'),
        ),
        (
            get_fixture_path('nested_file1.yml'),
            get_fixture_path('nested_file2.yml'),
            get_fixture_path('expected/diff_result_stylish_nested'),
        ),
    ],
)
def test_param_default_style(filepath1, filepath2, correct_diff_path):
    """Check that files are compare correctly.

    Args:
        filepath1: Path to first file
        filepath2: Path to first file
        correct_diff_path: Path to file containing correct compare result
    """
    diff = generate_diff(filepath1, filepath2)
    expected = open_file(correct_diff_path)
    assert diff == expected
