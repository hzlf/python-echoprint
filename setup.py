#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from setuptools import Extension

#from distutils.core import Extension


#from distutils.core import setup, Extension

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

echoprint_c = Extension(
    'echoprint',
    [
        'libcodegen/AudioBufferInput.cxx',
        'libcodegen/AudioStreamInput.cxx',
        'libcodegen/Base64.cxx',
        'libcodegen/Codegen.cxx',
        'libcodegen/Fingerprint.cxx',
        'libcodegen/MatrixUtility.cxx',
        #'libcodegen/Metadata.cxx',
        'libcodegen/SubbandAnalysis.cxx',
        'libcodegen/Whitening.cxx',
        'echoprint.cpp',
    ],
    include_dirs=[
        '/usr/include/taglib',
        'libcodegen'
    ],
    libraries=[
        #'pthread'
        'tag',
        'z',
    ],
)

setup(
    name='python-echoprint',
    version='0.0.2',
    license='MIT',
    author='Jonas Ohrstrom',
    author_email='ohrstrom@gmail.com',
    url='https://github.com/hzlf/python-echoprint',
    description='Echoprint-codegen Library',
    ext_modules=[
        echoprint_c
    ],
    test_suite='tests'
)

