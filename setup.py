# coding=utf-8
from __future__ import unicode_literals
from setuptools import setup, find_packages

from jsonparser import __version__
from jsonparser import __doc__

__author__ = 'ad'
__date__ = '12/03/16'


setup(name='jsonparser',
      version=__version__,
      description='Parses some log, displays result in some format',
      long_description=__doc__,
      keywords=['cli', 'log', 'parser'],
      author='Alexander Lebedev (ad)',
      author_email='lebedev@0x4e3.ru',
      url='https://github.com/ad-lebedev/parser',
      packages=find_packages(),
      install_requires=[
          'docopt==0.6.2',
          'jinja2==2.8'
      ],
      entry_points={
          'console_scripts': [
              'jsonparser=jsonparser:main'
          ]
      },
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'Natural Language :: Russian',
          'Programming Language :: Python',
          'Topic :: System :: Logging',
          'Topic :: System :: Monitoring',
          'Topic :: Utilities'
      ],
      zip_safe=False)
