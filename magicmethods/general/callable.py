import util


class SumAll(object):
    """ x()  is x.__call__()"""

    def __init__(self, initial=0):
        """ """
        self.sum = initial

    def __call__(self, *args, **kwargs):
        """ """
        for x in args:
            self.sum += x

        return self.sum


class TestCallable(util.TestCaseBase):
    """ """

    def test_callable(self):
        """ """
        s = SumAll(1);
        self.assertEqual(s(1, 2, 3, 4), 11)
        self.assertEqual(s.__call__(1, 2, 3, 4), 21)
