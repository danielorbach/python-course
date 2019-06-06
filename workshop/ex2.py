"""
Workshop #2

Write a decorator (function) that returns a filename.
The filename must be valid for the current os.
"""

from .ex1 import generate_characters


def generate_filename(length=10):
    return generate_characters(length)
