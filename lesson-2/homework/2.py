"""
Stira

assign a value (any value, even your own type works) to the variable 'n' so the code in 'main' works without exceptions.
DO NOT change the code in 'main'.

Read about:
  - object.__eq__
  - int.__lt__, int.__le__, int.__gt__, int.__ge__
  - assert
"""


def absolutely_false(n):
    if n <= 0:
        return False
    return (-1) == n

# ENTER CODE HERE
class Number(int):
    def __le__(self, other):
        return False
n = Number(-1)


def main():
    # make sure the following code works
    assert absolutely_false(n), 'make this code pass without exceptions'


if __name__ == '__main__':
    main()
