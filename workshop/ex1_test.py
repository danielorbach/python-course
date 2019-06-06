"""
# Workshop #1

Write a function that returns a random name for a file
"""

import random


def generate_filename():
    return f'file_{random.random()}.tmp'


def test():
    name1 = generate_filename()
    name2 = generate_filename()
    assert name1 != name2
