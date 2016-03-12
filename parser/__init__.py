# coding=utf-8
"""

"""
from __future__ import unicode_literals

import sys

from .parser import Parser

__author__ = 'ad'
__date__ = '12/03/16'
__version__ = '0.1'


def main():
    p = Parser()
    p.parse()


if __name__ == '__main__':
    sys.exit(main())
