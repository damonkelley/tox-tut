
#! /usr/bin/env python
import os
from setuptools import setup, find_packages

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()


#allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="tox-tut",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,

    license="BSD",
    description="Tutorial for the tox workshop",
    # long_description=README,
    keywords="tox testing",
    author="Damon Kelley",
    # cmdclass={'test': PyTest},
    url="https://github.com/damonkelley/tox-tut",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
