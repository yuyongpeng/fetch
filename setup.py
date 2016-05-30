#!/usr/bin/env python
#  -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
    scripts=['fetchrun.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['feedparser>=5.2.0'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },
    # metadata for upload to PyPI
    author="yuyongpeng",
    author_email="yuyongpeng@hotmail.com",
    description="这个是抓取程序,通过配置,抓取rss的页面",
    license="apache 2.0",
    keywords="fetch rss",
    url="https://github.com/yuyongpeng/fetch",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)