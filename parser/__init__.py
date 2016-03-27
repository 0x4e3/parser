# coding=utf-8
"""
jsonparser
==========
Console utility that parses data from stdin and outputs them to the stdout

Usage:
-------
    $ tail -f /var/log/service.log | jsonparser [--format <template_file> ] [--filter <expression>]

Options:
---------
    --format    Tels parser to use given file as output template
    --filter    Filters input lines by given fields value

Default output format:
----------------
    [@timestamp] @fields.level @message

Example:
---------
    $ tail -f /var/log/service.log | jsonparser
    [2015-12-15T05:45:39+00:00] INFO Request processed

"""
from __future__ import unicode_literals
from __future__ import absolute_import

import sys
import re
import argparse
import docopt

from .parser import Parser

__author__ = 'ad'
__date__ = '12/03/16'
__version__ = '0.1'


def filter_type(value):
    try:
        return re.match(r'^@[a-z]*.[a-z_]*=[0-9a-zA-Z/_-]*', value).group(0)
    except:
        raise argparse.ArgumentTypeError(
            'Filter expression must fit the format: @field_name=value or '
            '@field_name.subfield_name=value')


def get_args():
    arg_parser = argparse.ArgumentParser(
        description='Console utility that parses data from stdin '
                    'and outputs them to the stdout')
    arg_parser.add_argument(
        '--format',
        type=str,
        help='Path to the Jinja template',
        required=False)
    arg_parser.add_argument(
        '--filter',
        type=filter_type,
        help='Filter expression',
        required=False)
    return arg_parser.parse_args()


def main():
    if sys.stdin.isatty():
        arguments = docopt.docopt(__doc__)
        print(arguments)
    else:
        args = get_args()
        p = Parser(args)
        p.parse()


if __name__ == '__main__':
    sys.exit(main())
