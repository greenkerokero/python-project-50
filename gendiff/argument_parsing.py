"""Pars arguments entered by user into the command line."""
import argparse
import sys


def pars_cli_argument():
    """Pars arguments entered by user into the command line.

    Returns:
        Namespace with command line parameters as attributes
    """
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
    return parser.parse_args()
