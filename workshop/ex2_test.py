"""
Unittest for Workshop #2
"""
import os

from .ex2 import generate_filename


def is_file_valid(path):
    try:
        with open(path, 'x') as _:
            pass
        os.remove(path)
        return True
    except OSError:
        return False


def test():
    for i in range(10):
        name1 = generate_filename()
        name2 = generate_filename()
        assert name1 != name2
        assert is_file_valid(name1)
        assert is_file_valid(name2)
