from setuptools import find_packages
from distutils.core import setup

from .egyszer import __version__ as egyszerVersion

setup(
    name="egyszer",
    version=egyszerVersion,
    author="fogasl",
    description="Plain text with superpowers - base library",
    long_description=open("README.md", "r", encoding="utf8").read(),
    keywords="plain text format metadata",
    python_requires=">3.5",
    packages=find_packages(),
)
