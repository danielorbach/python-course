"""
This is the doc-string for the module.
Note how this part is displayed as the module's help.
"""

# Imports
import math
import os
import sys
from functools import reduce
from tempfile import mktemp as generate_filename
from argparse import ArgumentParser
# noinspection PyUnresolvedReferences
from pathlib import Path

# Constant
PI = math.pi


# internal Function
def _print_fileno():
    print('STDIN', sys.stdin.fileno())
    print('STDOUT', sys.stdout.fileno())


# Class
class Calculator:
    """sums all numbers"""
    # class Member
    VERSION = 1.0

    # Constructor
    def __init__(self, *numbers, initial_value=PI):
        # These are instance members
        self._initial = initial_value
        self.numbers = numbers

    # this is a Static Method
    @staticmethod
    def _calc(x, y):
        return x + y

    # this is a Class Method
    @classmethod
    def version(cls):
        """return version string"""
        return f'Version {cls.VERSION}'

    # this is a Method
    def calc(self):
        """produces a result based on internal state"""
        return reduce(self._calc, self.numbers, self._initial)

    # this is a Method
    def get_initial(self):
        """exposes read-access to internal member"""
        return self._initial


# Function
def main():
    parser = ArgumentParser(description='Example of a python program')
    parser.add_argument('-i', '--initial', type=float, help='where to write output')
    parser.add_argument('-o', '--output', action='store_true', help='should write output')
    parser.add_argument('numbers', nargs='+', type=int, help='all positional input')
    args = parser.parse_args()
    # parser.add_argument('-o', '--output', type=FileType('w'), help='where to write output', default='-')

    calc = Calculator(*args.numbers, initial_value=args.initial)
    if args.output:
        with open(generate_filename(suffix='txt'), 'w') as f:
            def _cout(obj):
                """write-line object to file as string"""
                f.write(repr(obj))
                f.write(os.linesep)

            _cout(calc.version())
            _cout(calc.numbers)
            _cout(calc.get_initial())
            _cout(calc.calc())
            f.write(os.linesep)
            print(f'OUTPUT: {f.name}')
    print(calc.calc())


# Program entry-point
if __name__ == '__main__':
    main()
