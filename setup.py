# core modules
from setuptools import find_packages
from setuptools import setup
import io
import os


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding='utf-8') as f:
        return f.read()

config = {
    'name': 'image_cleaner',
    'version': '0.1.1',
    'author': 'Martin Thoma',
    'author_email': 'info@martin-thoma.de',
    'maintainer': 'Martin Thoma',
    'maintainer_email': 'info@martin-thoma.de',
    'packages': find_packages(),
    'scripts': ['bin/image_cleaner'],
    'package_data': {},
    'platforms': ['Linux', 'MacOS X', 'Windows'],
    'url': 'https://github.com/MartinThoma/image_cleaner',
    'license': 'MIT',
    'description': 'remove metadata from images to enhance privacy',
    'long_description': read('README.md'),
    'long_description_content_type': 'text/markdown',
    'install_requires': [
        "argparse",
    ],
    'keywords': ['privacy', 'metadata', 'images', 'exif'],
    'download_url': 'https://github.com/MartinThoma/image_cleaner',
    'classifiers': ['Development Status :: 7 - Inactive',
                    'Topic :: Utilities'],
    'zip_safe': False,
    'test_suite': 'nose.collector'
}

setup(**config)
