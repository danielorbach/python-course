"""
Solution for Workshop #2

Write a decorator (function) that returns a filename.
The filename must be valid for the current os.

Docs: https://docs.microsoft.com/en-us/windows/desktop/fileio/naming-a-file
"""

from .ex1 import generate_characters


def base64_filename(filename):
    import base64
    return base64.b32encode(bytes(filename, 'utf-8'))


def windows_filename(filename):
    windows_reserved_characters = r'<>:"/|\?*'
    windows_translation = str.maketrans({c: None for c in map(chr, range(256))
                                          if not c.isprintable()
                                          or c in windows_reserved_characters
                                          or ord(c) <= 31 or ord(c) >= 128})
    return filename.translate(windows_translation)


def alphanum_filename(filename):
    my_translation = str.maketrans({c: None for c in map(chr, range(256))
                                     if not c.isalnum()})
    return filename.translate(my_translation)


def hash_filename(filename):
    import hashlib
    return hashlib.md5(filename.encode()).hexdigest()


def safe_filename(func):
    def inner(*args, **kwargs):
        filename = func(*args, **kwargs)
        return hash_filename(filename)

    return inner


@safe_filename
def generate_filename(length=10):
    return generate_characters(length)
