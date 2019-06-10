"""
Workshop #3

Write a decorator that wraps the generated filename (from the previous exercise)
and creates the file in the given directory.
A new file must be created, existing filenames are not valid return values.
"""

from .ex2 import generate_filename


def generate_file(func):
    # TODO
    return func


generate_file = generate_file(generate_filename)
