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

    def test_dict_init_kw(self):
        """ create dictionary using key work arguments"""
        d = dict(i=1, j=2)
        self.assertEqual(d['i'], 1)
        self.assertEqual(d['j'], 2)

    def test_dict_key_value_types(self):
        """ key and value types are frozenset"""
        dct = {1: 2}
        print(type(dct.keys()), frozenset)
        print(type(dct.values()), frozenset)
