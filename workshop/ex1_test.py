"""
Unittest for Workshop #1
"""

from .ex1 import generate_characters


def test():
    for i in range(1, 100):
        name1 = generate_characters(i)
        name2 = generate_characters(i)
        assert name1 != name2
