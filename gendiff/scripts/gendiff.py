#!/usr/bin/env python3
"""Entry point of project. Script implement user interface."""
import argparse

from gendiff.generate_diff import generate_diff


def main():
    """Implement user interface."""
    parser = argparse.ArgumentParser(
        usage='gendiff [options] <first_file> <second_file>',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', help=argparse.SUPPRESS)
    parser.add_argument('second_file', help=argparse.SUPPRESS)
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output',
    )
    args = parser.parse_args()
    compare = generate_diff(args.first_file, args.second_file, args.format)
    print(compare)


if __name__ == '__main__':
    main()
