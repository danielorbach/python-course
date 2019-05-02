"""
Example file to explain decorators.
execution syntax
"""
import time


class AutoDispose:
    # constructor    
    def __init__(self):
        self._setup = self._pass
        self._teardown = self._pass

    # private functions
    def _pass(self, *args, **kwargs):
        '''helper function that does nothing at all'''
        pass

    # decorators
    def setup(self, func):
        self._setup = func
        return func

    def teardown(self, func):
        self._teardown = func
        return func

    # context manager functions
    def __enter__(self):
        self._setup()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self._teardown(exc_type, exc_value, traceback)


# create an instance of a file-manager to ensure proper closing
resource = AutoDispose()


# register preparations for the file
@resource.setup
def file_setup():
    print('this is a specific setup function (would open the file)')
    
# register cleanup for the file
@resource.teardown
def file_teardown(*args, **kwargs):
    print('this is a specific teardown function (would close file)')


def main():
    # open file
    breakpoint()
    with resource:
        # do something
        print(f'file was opened at {time.time()}')
        # close file


if __name__ == '__main__':
    main()