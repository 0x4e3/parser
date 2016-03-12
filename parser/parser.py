# coding=utf-8
from __future__ import unicode_literals
import fileinput

__author__ = 'ad'
__date__ = '12/03/16'


class Parser(object):
    """
    Main parser class
    """
    def __init__(self):
        self.keys = ['@timestamp', '@fields', '@message']
        self.format = '[%s] %s %s'
        self.template = None
        self.filter = None

    def parse(self):
        for line in fileinput.input():
            print(line)
