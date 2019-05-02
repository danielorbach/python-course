"""
Default Dict

write a dictionary with a default value so the code in main works without exceptions.
DO NOT change the code in main.

Read about:
  - dict
  - super()
"""



class DefaultDict(dict):
    # ENTER CODE HERE
    pass


def main():
    # make sure the following code works
    default_dict = DefaultDict('a default value')
    for i in range(10):
        default_dict[i] = i ** 2

    for i in range(11):
        print(f'default_dict[{i}] = {default_dict[i]}')


if __name__ == '__main__':
    main()
