#!/usr/bin/env python3
"""Entry point of project. Script implement user interface."""
import argparse
import sys

from gendiff.generate_diff import generate_diff


def main():
    """Implement user interface."""
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] FILE1 FILE2',
        description='Compares two configuration files and shows a difference',
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help=(
            'specify the format of the output\n'
            'available formats: stylish (default), plain, json'
        ),
    )
    parser.add_argument('FILE1', help=argparse.SUPPRESS)
    parser.add_argument('FILE2', help=argparse.SUPPRESS)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    compare = generate_diff(args.FILE1, args.FILE2, args.format)
    print(compare)


if __name__ == '__main__':
    main()
