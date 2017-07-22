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
            return func(name) + symbol

        return func_wrapper

    return end_with_decorator


@end_with('@')
def i_miss(name):
    return 'I missed {0}'.format(name)


def trailing_underscore(func):
    """ """

    def wrapper(*args, **wargs):
        """ """
        res = func(*args, **wargs)
        return str(res) + '_' * len(args)

    return wrapper


@trailing_underscore
def func_various_args(*args, **wargs):
    """ """
    res = ""
    print(res)
    for r in args:
        res += str(r)
    return res


class CaseDecorator(object):
    """ a class for decorator """

    @staticmethod
    def upper(func):
        """ upper """

        def upper_wrapper(input):
            """ """
            res = func(input)
            return res.upper()

        return upper_wrapper

    @classmethod
    def lower(cls, func):
        """ upper """

        def lower_wrapper(input):
            """ as it says """
            res = func(input)
            return res.lower()

        return lower_wrapper

    @classmethod
    def with_name(cls, name):
        """ """

        def with_name_f(func):
            """ """

            def with_name_f_wrapper():
                """ """
                res = func()
                return res + name

            return with_name_f_wrapper

        return with_name_f


@CaseDecorator.upper
def i_am(name):
    """ as it says """
    return "I am {}".format(name)


@CaseDecorator.lower
def i_am_not(name):
    """ as it says """
    return "I am not {}".format(name)


@CaseDecorator.with_name('Hero')
def he_is():
    """ """
    return 'He is '


class TestClassDecorator(util.TestCaseBase):
    """ class decorator """

    def test_class_decorator_upper(self):
        """ as it says"""
        self.assertEqual(i_am_not('WEAK'), 'i am not weak')

    def test_class_decorator_lower(self):
        """ as it says"""
        self.assertEqual(i_am('strong'), 'I AM STRONG')

    def test_class_decorator_with_arg(self):
        """ as it says"""
        self.assertEqual(he_is(), 'He is Hero')


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
        self.assertEqual(func_various_args(1, 2, 3), '123___')
        self.assertEqual(func_various_args(1), '1_')
