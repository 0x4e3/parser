# coding=utf-8
from __future__ import unicode_literals

import json
import sys
from jinja2 import FileSystemLoader, Environment, Template, meta
from os import path

__author__ = 'ad'
__date__ = '12/03/16'


class Parser(object):
    """
    Main parser class
    """
    def __init__(self, options):
        self.options = options
        self.template = None
        self.keys = None
        self.filter = None

        template_loader = FileSystemLoader(searchpath="/")
        template_env = Environment(loader=template_loader)
        if not self.options.format:
            template_source = \
                '[{{ timestamp }}] {{ fields.level }} {{ message }}'
        else:
            template_file = path.abspath(self.options.format)
            template_source = template_env.loader. \
                get_source(template_env, template_file)[0]
        self.keys = meta.find_undeclared_variables(
            template_env.parse(template_source))
        self.template = Template(template_source)
        if self.options.filter:
            self.filter = self.options.filter.replace('@', '').split('=')

    def parse(self):
        for line in sys.stdin:
            data = json.loads(line.replace('@', ''))
            if self.filter:
                filter_path = self.filter[0].split('.')

                if len(filter_path) == 1:
                    value = data.get(filter_path[0], '')
                else:
                    value = data.get(filter_path[0], '').\
                        get(filter_path[1], '')

                try:
                    filter_value = int(self.filter[1])
                    if value == filter_value:
                        print(self.template.render(**data))
                except ValueError:
                    filter_value = self.filter[1]
                    if value.find(filter_value) != -1:
                        print(self.template.render(**data))
            else:
                print(self.template.render(**data))
