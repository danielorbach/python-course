"""
Example file to explain decorators.
override syntax
"""

# let's define a function that calculates the square of a number
def square(n):
    return n * n

print(f'The output of square(5) is {square(5)}')



# let's define a decorator to change that from pow(2) to pow(3)
def cube(square_func):
    def inner(n):
        return n * square_func(n)
    return inner
square = cube(square)

print(f'The output of square(5) is {square(5)}')
