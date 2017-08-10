# https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/

import util

class TestImmutable(util.TestCaseBase):
    """ """

    def test_int(self):
        """ """
        a = 1
        b = 1

        print(id(a))
        print(id(b))

    def test_tuple(self):
        """ """
        a = 1, 2
        b = 2, 3

