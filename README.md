[![PyPI version](https://badge.fury.io/py/image-cleaner.svg)](https://badge.fury.io/py/image-cleaner)
[![Python Support](https://img.shields.io/pypi/pyversions/image-cleaner.svg)](https://pypi.org/project/image-cleaner/)

Remove all metadata from images in a given folder.

Images can contain lots of metadata. Most critical to privacy might be GPS
coordinates and date / time. You might consider doing so before you upload them
on public websites.

`image_cleaner` removes all metadata from all images in a given folder.


## Installation and Dependencies

You need to install [Pillow](http://pillow.readthedocs.org/installation.html):

```bash
$ pip install Pillow
```

Now install image cleaner

```bash
$ pip install image_cleaner
```

And call it: `image_cleaner --help`
