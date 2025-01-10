#!/usr/bin/env python3
"""Entry point of project. Script implement user interface."""

from gendiff.argument_parsing import pars_cli_argument
from gendiff.generate_diff import generate_diff


def main():
    """Implement user interface."""
    args = pars_cli_argument()
    compare = generate_diff(args.FILE1, args.FILE2, args.format)
    print(compare)


if __name__ == '__main__':
    main()
