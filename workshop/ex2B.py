"""
# Workshop #2

Write a decorator (function) that makes sure the `generate_filename` function never repeats itself
Do not change the `generate_filename` function
"""

import time


def safe_generate_filename(func):
    cache = []

    def inner():
        name = func()
        while name in cache:
            name = func()
        cache.append(name)
        return name

    return inner


@safe_generate_filename
def generate_filename():
    return f'file_{time.time_ns()}.tmp'


def test():
    name1 = generate_filename()
    name2 = generate_filename()
    assert name1 != name2
