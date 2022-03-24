import sys
import os
import io
from setuptools import find_packages, setup, Command, Extension

version_file = 'aim_spacy/VERSION'

__version__ = None
with open(version_file) as vf:
    __version__ = vf.read().strip()


here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data
NAME = 'aim_spacy'
DESCRIPTION = 'Aim-spaCy integration'
LONG_DESCRIPTION = DESCRIPTION
VERSION = __version__
REQUIRES_PYTHON = '>=3.6.0'

# Get packages
packages = find_packages(exclude=('tests', 'examples'))

REQUIRED = [
    'html2image',
    'spacy',
    'tqdm',
    'aim',
    'svglib',
    'lxml',
    'pillow',
    'reportlab',
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    packages=packages,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
