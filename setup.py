from setuptools import find_packages
from setuptools import setup

config = {
    'name': 'image_cleaner',
    'version': '0.1.0',
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
    'long_description': ("image_cleaner removes metadata from images. You "
                         "might consider doing so before you upload "
                         "them on public websites."),
    'install_requires': [
        "argparse",
    ],
    'keywords': ['privacy', 'metadata', 'images', 'exif'],
    'download_url': 'https://github.com/MartinThoma/image_cleaner',
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Topic :: Utilities'],
    'zip_safe': False,
    'test_suite': 'nose.collector'
}

setup(**config)
