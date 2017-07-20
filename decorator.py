import util


# A function that takes another function as an argument, generates a new function, augmenting the work of the original function, and returning the generated function so we can use it anywhere.

def i_love(name):
    """ """
    return 'I love {0}'.format(name)


def upper_case_decorate(func):
    """ decorator """

    def to_upper(name):
        """ """
        upper = func(name).upper()
        return upper

    return to_upper


I_LOVE = upper_case_decorate(i_love)
i_love = upper_case_decorate(i_love)


@upper_case_decorate
def i_hate(name):
    """ """
    return 'I hate {0}'.format(name)


def double_decorator(func):
    """ double the string"""

    def double_it(name):
        """ """
        single = func(name)
        return single + single

    return double_it


def i_enjoy(name):
    """ enjoy sth """
    return "I enjoy {0} ".format(name)


I_ENJOY_I_ENJOY = upper_case_decorate(double_decorator(i_enjoy))

@double_decorator
@upper_case_decorate
def i_like(name):
    """ """
    return "I like {0} ".format(name)


def end_with(symbol):
    def end_with_decorator(func):
        def func_wrapper(name):
            return func(name) +  symbol
        return func_wrapper
    return end_with_decorator


@end_with('@')
def i_miss(name):
    return 'I missed {0}'.format(name)


def deco_args(func):
    """ """
    def wrapper(*args, **wargs):
        """ """
        res = func(*args, **wargs)
        return str(res) + '_'*len(args)
    return wrapper

@deco_args
def func_various_args(*args, **wargs):
    """ """
    res = ""
    print(res)
    for r in args:
        res += str(r)
    return res


class TestFuncDecorator(util.TestCaseBase):
    """ """

    def test_basic_decorator(self):
        """ without @: assign to a diff name"""
        self.assertEqual(I_LOVE('you'), 'I LOVE YOU')

    def test_basic_decorator(self):
        """ without @: assign to the same name"""
        self.assertEqual(i_love('you'), 'I LOVE YOU')

    def test_decorator_at(self):
        """ with @"""
        self.assertEqual(i_hate('you'), 'I HATE YOU')

    def test_double_decorator(self):
        """ without @"""
        self.assertEqual(I_ENJOY_I_ENJOY('life'), 'I ENJOY LIFE I ENJOY LIFE ')

    def test_double_decorator_at(self):
        """ with @ """
        self.assertEqual(i_like('music'), 'I LIKE MUSIC I LIKE MUSIC ')

    def test_decorator_with_param(self):
        """ """
        self.assertEqual(i_miss('you'), 'I missed you@')

    def test_decorate_args_wargs(self):
        """ decorator that accepts args """
        self.assertEqual(func_various_args(1, 2, 3, 4), '1234____')
        self.assertEqual(func_various_args(1, 2, 3 ), '123___')

