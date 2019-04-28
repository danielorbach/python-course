"""
This is the doc-string for the module.
Note how this part is displayed as the module's help.
"""

# Imports
import sys


# Exception sub-class
class ForbiddenDivisionError(ArithmeticError):
    # Constructor
    def __init__(self, n):
        # Super constructor
        super().__init__('Cannot divide by ' + str(n))


# Function (static)
def safe_divide(x, y, forbidden=0):
    # Condition
    if y == forbidden:
        # Exception
        raise ForbiddenDivisionError(forbidden)
    # use floor-division to match Java's integer division
    return x // y


# Main class for program entry-point
class Main:
    @staticmethod
    def main(args):
        # Print text to stdout
        print('Hello World!')

        # Arguments (complex)
        forbidden = int(args[0]) if len(args) != 0 else 0
        # Call function
        print('1 / 2 =', safe_divide(1, 2, forbidden))


# Program entry-point
if __name__ == '__main__':
    Main.main(sys.argv[1:])
