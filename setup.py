# coding=utf-8
from __future__ import unicode_literals
from setuptools import setup, find_packages
from codecs import open
from os.path import abspath, dirname, join

from parser import __version__

__author__ = 'ad'
__date__ = '12/03/16'

base_dir = abspath(dirname(__file__))
with open(join(base_dir, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(name='jsonparser',
      version=__version__,
      description='Parses some log, displays result in some format',
      long_description=long_description,
      keywords='cli log parser',
      author='Alexander Lebedev (ad)',
      author_email='lebedev@0x4e3.ru',
      packages=find_packages(exclude=['docs', 'tests*']),
      entry_points={
          'console_scripts': [
              'jsonparser=parser:main'
          ]
      },
      zip_safe=False)
