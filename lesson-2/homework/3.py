"""
Calculator

Make it so the main function passes all assertions just by changing the code in the decorators alone.
Remember PEP8 - do not submit code that does not adhere to the conventions.

Read about:
  - decorators
  - __repr__ vs __str__
  - list arithmetic operators
  - new-style format strings
  - order of multiple decorators
"""
import operator
from functools import reduce


# ENTER YOUR DECORATORS HERE

def decorator1(func):
    pass


def decorator2(func):
    pass


def decorator3(func):
    pass


def decorator4(func):
    pass


# ==========================


def decorator5(func):
    return lambda x, y: func(y, x)


@decorator1
def add(x, y):
    return x + y


@decorator2
def subtract(x, y, base):
    return int(x, base) - int(y, base)


@decorator3
def multiply(x, y):
    return reduce(operator.add, x * y)


@decorator4
@decorator5
def divide(x, y):
    return x / y


def main():
    decimal = 10
    hexadecimal = '0x10'
    octal = '10'

    # addition
    assert add(hexadecimal, octal) == 24, \
        f'add({hexadecimal!r}, {octal!r}) -> {add(hexadecimal, octal)!r}'

    # based subtraction
    assert subtract(hexadecimal, octal) == 0, \
        f'subtract({hexadecimal!r}, {octal!r}) -> {subtract(hexadecimal, octal)!r}'

    # unary multiplication
    assert multiply(decimal, 10) == 100, \
        f'multiply({decimal!r}, {10!r}) -> {multiply(decimal, 10)!r}'

    # ordered division
    assert divide(0, decimal) == 0, \
        f'divide({10!r}, {decimal!r}) -> {divide(0, decimal)!r}'


if __name__ == '__main__':
    main()
