#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    llm_runtime


    Unified python api for LLM's runtime

    :date:      04/08/2023
    :author:    llmapi <llmapi@163.com>
    :homepage:  https://github.com/llmapi-io/llm-runtime
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2023 llmapi. All rights reserved
"""
import sys
import json
import os
import argparse as ap
from argparse import RawTextHelpFormatter
import time

__name__ = 'llm_runtime'
__version__ = '0.0.1'
__description__ = 'Run llama/stableDiffusion/controlNet/SAM and so on, just in one lib.'
__keywords__ = 'LLM OpenAPI LargeLanguageModel LLama SD SAM'
__author__ = 'llmapi'
__contact__ = 'llmapi@163.com'
__url__ = 'https://github.com/llmapi-io/llm-runtime'
__license__ = 'MIT'

