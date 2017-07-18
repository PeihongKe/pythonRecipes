import util


class TestList(util.TestCaseBase):
    """ test builtin List"""

    def test_extend_return_None(self):
        """ """
        a = ['a']
        b = ['b']
        self.assertEqual(b.extend(a), None)
        self.assertEqual(b, ['b', 'a'])


class TestFrozenSet(util.TestCaseBase):
    def test_frozen_set(self):
        f = frozenset({1, 2})
        print(f)


class TestDict(util.TestCaseBase):
    """ """

    def test_tuple_key(self):
        """ """
        d = dict()
        d[1, 2] = 3
        self.assertTrue([k for k in d.keys()][0], (1, 2))

