#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_version():
    version_file = read("tenseal/version.py")
    version_re = r"__version__ = '(?P<version>.+)'"
    version = re.match(version_re, version_file).group('version')
    return version

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ben Szymkow",
    author_email='simcof@gmail.com',
    classifiers=[
        "Programming Language :: C++/Python",
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python API for Google's Differential Privacy library",
    install_requires=requirements,
    license="Apache-2.0",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",    
    include_package_data=True,
    keywords='pydp',
    name='pydp',
    packages=find_packages(include=['pydp']), # need to check this
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/OpenMined/PyDP',
    version='0.1.0',
    zip_safe=False,
)
