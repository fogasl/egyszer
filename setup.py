#!/usr/bin/env python

from egyszer import __version__ as version
from setuptools import find_packages, setup

setup(
    name="egyszer",
    version=version,
    url="",
    author="fogasl",
    description="Plain text with superpowers - base library",
    keywords="plain text file format metadata",
    packages=find_packages()
)
