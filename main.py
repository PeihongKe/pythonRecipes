import unittest

import idioms
from oo import mro

tests_to_run = [mro.TestMRO, idioms.TestIdioms]


def run_tests(m):
    print('run module ' + m.__name__)
    unittest.main(m.__name__)

if __name__ == '__main__':
    for m in tests_to_run:
        m.run_tests()


