#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    llm-runtime

    Unified python runtime api for LLMs

    :author:    llmapi <llmapi@163.com>
    :homepage:  https://llmapi.io/
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2023 llmapi. All rights reserved
"""
import codecs
import llm_runtime
import setuptools.command.test


# -*- Long Description -*-

def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.rst file'


setuptools.setup(
    name=llm_runtime.__name__,
    version=llm_runtime.__version__,
    description=llm_runtime.__description__,
    long_description=long_description(),
    keywords=llm_runtime.__keywords__,
    author=llm_runtime.__author__,
    author_email=llm_runtime.__contact__,
    url=llm_runtime.__url__,
    license=llm_runtime.__license__,
    platforms=['any'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Terminals',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        '': ['*.py']
    },
    python_requires = '>=3.6',
    install_requires = ['torch','torchvision','tinygrad','numpy'],
)
