"""
Workshop #3

Write a decorator that wraps the generated filename (from the previous exercise)
and creates the file in the given directory.
A new file must be created, existing filenames are not valid return values.
"""
import os

from .ex2 import generate_filename


def generate_file(func):
    def inner(folder, mode='r', *args, **kwargs):
        filename = func(*args, **kwargs)
        while os.path.exists(filename):
            filename = func(*args, **kwargs)
        return open(os.path.join(folder, filename), mode)

    return inner


generate_file = generate_file(generate_filename)
