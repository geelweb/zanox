#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages
import zanox

setup(
    name = "Zanox",
    version = zanox.__version__,
    packages = find_packages(exclude=["examples"]),
    author = "Guillaume Luchet",
    author_email = "guillaume@geelweb.org",
    description = "Zanox web service API client",
    license = "MIT License",
    keywords = "Zanox Api affiliation",
    platforms = "ALL"
)

