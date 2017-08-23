import util


class TestBuildIn(util.TestCaseBase):
    ''' built in function '''

    def test_sum(self):
        """ test sum(iterable) """
        self.assertTrue(sum([1, 2, 3]), 6)

    def test_sum_start(self):
        """ test sum(iterable, start )"""
        self.assertEqual(sum([1, 2, 3], 10), 16)
