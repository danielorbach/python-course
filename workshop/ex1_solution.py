"""
Solution for Workshop #1

Write a function that returns a random string
"""

import random


def generate_characters(length=10):
    return ''.join(chr(random.randint(0, 255)) for _ in range(length))
