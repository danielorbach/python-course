"""
Solution for Workshop #1

Write a function that returns a random string.
Keep in mind Python Conventions (PEP8).
"""


def using_random(length):
    import random
    return ''.join(chr(random.randint(0, 255)) for _ in range(length))


def using_secrets(length):
    import secrets
    return ''.join(chr(secrets.randbits(8)) for _ in range(length))


def using_time(length):
    import time
    return str(time.time_ns())[:length].zfill(length)


def generate_characters(length):
    # which function would you use?
    return using_random(length)
