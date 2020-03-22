#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example for a simple program with a command line parser."""

# Core Library modules
import os
from os import listdir
from os.path import isfile, join

# First party modules
import PIL.ExifTags
import PIL.Image


def main(args):
    onlyfiles = [
        os.path.join(args.folder, f)
        for f in listdir(args.folder)
        if isfile(join(args.folder, f))
    ]
    image_files = filter_images(onlyfiles)
    if args.show_metadata:
        show_metadata(image_files)
    elif args.remove_metadata:
        remove_metadata(image_files)
    else:
        print("No action was chosen.")


def show_metadata(image_files):
    for filename in image_files:
        print("## %s" % filename)
        img = PIL.Image.open(filename)
        if not hasattr(img, "_getexif"):
            exif = None
        else:
            exif = img._getexif()
        if exif is not None:
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }
            for k, v in sorted(exif.items(), key=lambda n: n[0]):
                if isinstance(v, str) and len(v) > 80:
                    print(
                        "  %s: %s (cropped to 80 characters, was %i "
                        "characters long)" % (k, v[:80], len(v))
                    )
                else:
                    print("  {}: {}".format(k, v))
        else:
            print("  No metadata found.")


def remove_metadata(image_files):
    """
    Remove EXIF metadata from an list of images.

    Parameters
    ----------
    image_files : list of paths to images
    """
    for filename in image_files:
        print("## %s" % filename)

        image_file = open(filename)
        image = PIL.Image.open(image_file)

        # next 3 lines strip exif
        data = list(image.getdata())
        image_without_exif = PIL.Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        image_without_exif.save(filename)


def filter_images(filenames):
    """Return a list which contains images only."""
    # TODO: Consider using https://docs.python.org/2/library/imghdr.html
    endings = ["jpg", "png", "gif", "jpeg"]
    filtered = []
    for filename in filenames:
        for end in endings:
            if filename.lower().endswith(end):
                filtered.append(filename)
                break
    return filtered


def is_valid_folder(parser, arg):
    """Check if arg is a valid file that already exists on the file system."""
    arg = os.path.abspath(arg)
    if not os.path.isdir(arg):
        parser.error("The folder %s does not exist!" % arg)
    else:
        return arg


def get_parser():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description=__doc__, formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-f",
        "--folder",
        dest="folder",
        required=True,
        type=lambda x: is_valid_folder(parser, x),
        help="FOLDER to which an action gets applied",
        metavar="FOLDER",
    )
    parser.add_argument(
        "-r",
        "--remove",
        action="store_true",
        dest="remove_metadata",
        default=False,
        help="remove metadata from images (cannot be undone!)",
    )
    parser.add_argument(
        "-s",
        "--show",
        action="store_true",
        dest="show_metadata",
        default=False,
        help="show metadata of images",
    )
    return parser


def entry_point():
    args = get_parser().parse_args()
    main(args)
