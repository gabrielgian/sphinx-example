#  -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = "0.0.1"

setup(
    name='sphinx-example',
    version=__version__,
    author='Gabriel Tessaroli Giancristofaro',
    url='https://github.com/gabrielgian/sphinx-example',
    description='This repository contains a sphinx example code'
                ' which will integrates with Read the Docs website.',
    packages=find_packages(),
    zip_safe=False
)
