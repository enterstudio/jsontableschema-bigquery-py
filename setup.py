# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
from setuptools import setup, find_packages


# Helpers
def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding='utf-8').read().strip()
    return contents


# Prepare
PACKAGE = 'jsontableschema_bigquery'
NAME = PACKAGE.replace('_', '-')
INSTALL_REQUIRES = [
    'six>=1.9,<2.0a',
    'python-slugify>=1.2,<2.0a',
    'google-api-python-client>=1.5,<2.0a',
    'unicodecsv>=0.14,<1.0a',
    'jsontableschema>=0.7,<1.0a',
    'tabulator>=0.7,<1.0a',
]
TESTS_REQUIRE = [
    'pylama',
    'tox',
]
README = read('README.md')
VERSION = read(PACKAGE, 'VERSION')
PACKAGES = find_packages(exclude=['examples', 'tests'])


# Run
setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={'develop': TESTS_REQUIRE},
    zip_safe=False,
    long_description=README,
    description='Generate BigQuery tables, load and extract data, based on JSON Table Schema descriptors.',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='https://github.com/frictionlessdata/jsontableschema-bigquery-py',
    license='MIT',
    keywords=[
        'frictionless data',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
