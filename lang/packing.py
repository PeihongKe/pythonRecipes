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


def func6(a, *args):
    return a + sum(args)


def func7(*args, b):
    return sum(args) + b


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

    def test_it(self):
        input = (2, 3)
        expected = 6
        res = func6(1, *input)
        self.assertEqual(res, expected)

        # res1 = func6(a=1, *input) # TypeError: func6() got multiple values for argument 'a'

    def test_that(self):
        input = (1, 2)
        expected = 6
        res = func7(*input, b=3)
        self.assertEqual(res, expected)

        # func7(*input, 3) #SyntaxError: only named arguments may follow *expression

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
