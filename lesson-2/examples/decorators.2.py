"""
Example file to explain decorators.
decorator syntax
"""

# let's define a function that calculates the square of two numbers
def double_square(x, y):
    return (x*x, y*y)

print(f'The output of double_square(2, 3) is {double_square(2, 3)}')



# let's define a decorator to change that from two numbers to one
def square(func):
    def inner(n):
        x2, y2 = func(n, 0)
        return x2
    return inner

# redefine double_square, but with a decorator this time
@square
def double_square(x, y):
    return (x*x, y*y)

try:
    print(f'The output of double_square(2, 3) is {double_square(2, 3)}')
except Exception as e:
    print('The call failed because the function now takes only one argument')
    print(f'original exception - "{e}"')
print(f'The output of double_square(2, *) is {double_square(2)}')
