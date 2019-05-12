"""
Examples
"""
import subprocess

import pytest


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    print('this is module setup')


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print('this is module teardown')


@pytest.fixture(name='process')
def process_fixture():
    process = subprocess.Popen('notepad.exe')
    yield process
    process.kill()
    assert process.wait(3) is not None, 'process is still alive'



class Test:
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print('this is class setup')
        cls.process = subprocess.Popen('notepad.exe')

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        print('this is class teardown')

    def test_process_notepad(self):
        assert self.process.pid < 2 ** 16, 'pid is not in valid range'
        self.process.kill()
        try:
            self.process.wait(3)
        except subprocess.TimeoutExpired:
            print('this should not have happened')
        assert self.process.poll() is not None, 'process is still alive'


def test_process_calc(process):
    # process = subprocess.Popen('calc.exe')
    assert process.pid < 2 ** 16, 'pid is not in valid range'
    # process.kill()


def test():
    pass
