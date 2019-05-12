"""
Default Dict

write a dictionary with a default value so the code in main works without exceptions.
DO NOT change the code in main.

Read about:
  - dict
  - super()
"""
from copy import copy


class DefaultDict(dict):
    # ENTER CODE HERE
    def __init__(self, default_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._default_value = default_value

    def __getitem__(self, item):
        if item not in self:
            return copy(self._default_value)
        return super().__getitem__(item)


d = DefaultDict(list())

default_value1 = d['key']
d['key'].append('first')
default_value1.append('second')

default_value2 = d['other']
d['other'].append('first_other')
default_value2.append('second_other')

print(id(default_value1), id(default_value2))


def main():
    # make sure the following code works
    default_dict = DefaultDict('a default value')
    for i in range(10):
        default_dict[i] = i ** 2

    for i in range(11):
        print(f'default_dict[{i}] = {default_dict[i]}')


if __name__ == '__main__':
    main()
