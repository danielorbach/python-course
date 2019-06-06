"""
Unittest for Workshop #1
"""

from .ex1 import generate_characters


def test():
    name1 = generate_characters()
    name2 = generate_characters()
    assert name1 != name2
