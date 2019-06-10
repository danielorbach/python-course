"""
Unittest for Workshop #3
"""
import os
import tempfile

from .ex3_solution import generate_file


class Mock:
    cache_exists = []

    def __call__(self, path):
        if path not in self.cache_exists:
            self.cache_exists.append(path)
            return True
        return False

    def __enter__(self):
        self._os_path_exists = os.path.exists
        os.path.exists = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.path.exists = self._os_path_exists
        self._os_path_exists = None


def test():
    with Mock() as mock:
        with tempfile.TemporaryDirectory() as tmpdir:
            name = generate_file(tmpdir)
