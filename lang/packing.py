import util


def func1(a=1, b=2):
    return a + b


def func2(a, b):
    return a + b


def func3(*args):
    return sum(args)


def func4(**kwargs):
    return sum(kwargs.values())


def func5(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


class TestUnpacking(util.TestCaseBase):
    """ test arguments """

    def test_dict_unpack_to_keyword_args(self):
        """ test key word arguments: ** is used for dictionary """
        input = {'a': 2, 'b': 3}
        res = func1(**input)
        self.assertEqual(res, 5)

    def test_unpack_list_to_args(self):
        """ unpack list """
        input = [1, 2]
        res = func2(*input)
        self.assertEqual(res, 3)

    def test_unpack_tuple_to_args(self):
        """ unpack tuple """
        input = (1, 2)
        res = func2(*input)
        self.assertEqual(res, 3)


class TestPacking(util.TestCaseBase):
    """ test packing """

    def test_pack_pos(self):
        """ test pos packing """
        res = func3(1, 2, 3, 4)
        self.assertEqual(res, 10)

    def test_pack_dict(self):
        """ tes keyword packing """
        res = func4(a=1, b=2, c=3, d=4)
        self.assertEqual(res, 10)

    def test_pack_pos_dict(self):
        """ tes pos and keyword packing """
        res = func5(1, 2, a=3, b=4)
        self.assertEqual(res, 10)
