# coding: utf-8

import sys
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

MAJOR, MINOR1, MINOR2, RELEASE, SERIAL = sys.version_info

READFILE_KWARGS = {"encoding": "utf-8"} if MAJOR >= 3 else {}

def readfile(filename):
    with open(filename, **READFILE_KWARGS) as fp:
        filecontents = fp.read()
    return filecontents

VERSION_REGEX = re.compile("__version__ = \"(.*?)\"")
CONTENTS = readfile(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "skytempy", "__init__.py"))

VERSION = VERSION_REGEX.findall(CONTENTS)[0]

setup(name="skytempy",
      version=VERSION,
      author="Renee Spiewak",
      author_email="respiewak@gmail.com",
      description="A simple package to calculate sky temperatures",
      long_description=readfile(
          os.path.join(os.path.dirname(__file__), "README.md")),
      long_description_content_type="text/markdown",
      url="https://github.com/respiewak/skytempy",
      install_requires=readfile(
          os.path.join(os.path.dirname(__file__), "requirements.txt")),\
      license="MIT",
      classifiers=[
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"])
