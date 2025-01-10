"""Parsing structured string."""

from json import loads as json_loads

from yaml import SafeLoader
from yaml import load as yaml_load


def parse_structured_string(string, string_format='json'):
    """Get data from structured string.

    Args:
        string: Input string
        string_format: Input string format, json or yaml

    Returns:
        Dictionary containing data from string
    """
    if string_format == 'json':
        return json_loads(string)
    elif string_format in {'yaml', 'yml'}:
        return yaml_load(string, Loader=SafeLoader)
