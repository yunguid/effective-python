"""
Know how to contruct key-dependent default values with
__missing__

The built in dict type's setdefault method results in shorter code
when handling missing keys in some specific circumstances

For many situations, the better tool is defaultdict. However there are times when
neither is the right fit

In this example, we are writing a program to manage social network profile pictures
on the filesystem. We need a dictionary to map profile picture pathnames
to open file handles so I can read and write those images as needed.
"""

pictures = {}
path = "profile_1234.png"

if (handle := pictures.get(path)) is None:
    try:
        handle = open(path, "a+b")
    except OSError:
        print(f"failed to open path {path}")
else:
    pictures[path] = handle
handle.seek(0)
image_data = handle.read()

try:
    handle = pictures.setdefault(path, open(path, "a+b"))
except OSError:
    print(f"failed ot open the path {path}")
    raise
else:
    handle.seek(0)
    image_data = handle.read()


"""
This code sucks.
The open built-in function to create the file handle is always called, even
when the path is already present in the dictionary
"""

from collections import defaultdict


def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"failed to open path {profile_path}")
        raise


"""
This won't work because defaultdict assumes the function passed in to it does not
require any arguments
"""
pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()


class Pictures(dict):
    def __mising__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

"""
TTR:
    1. setdefault is a bad fit when creating the default value has high computational cost or may
    cause raise exceptions
    2. function passed to defaultdict must not require any arguments which makes it impossible
    to have the default value depened on the key being accessed
    3. you can define your own dict subclass with a __missing__ method in order to construct default
    values that must know which key was being accessed
"""
