import util


class TestBuildIn(util.TestCaseBase):
    ''' built in function '''

    def test_sum(self):
        """ test sum(iterable) """
        self.assertTrue(sum([1, 2, 3]), 6)

    def test_sum_start(self):
        """ test sum(iterable, start )"""
        self.assertEqual(sum([1, 2, 3], 10), 16)

    def test_reversed(self):
        """ returns the reversed iterator of the given sequence: corresponding magic method __reversed__"""
        l = [1, 2, 3]
        expected = [3, 2, 1]
        self.assertEqual(list(reversed(l)), expected)
