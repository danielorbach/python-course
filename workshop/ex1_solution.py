"""
# Workshop #1

Write a function that returns a random name for a file
"""

import random


def generate_filename():
    return f'file_{random.random()}.tmp'
