import util


def try_except():
    """ try except"""
    try:
        1 / 0
    except ZeroDivisionError:
        return 'an divided by 0 exeption'


def put_specific_before_general_exp():
    """ """
    try:
        1 / 0
    except Exception:
        return 'an exception'
    except ZeroDivisionError:
        return 'an divided by 0 exception'


def when_else_is_hit():
    """  else is hit when try terminate normally"""
    try:
        a = 1
    except:
        return 'an exception'
    else:
        return 'else is hit'

    return 'else is not hit'


def when_else_not_hit_exception():
    """ else is not hit due to exception """
    res = 'else is not hit'
    try:
        1 / 0
    except ZeroDivisionError:
        res = 'an exception is hit'
    else:
        res = 'else is hit'
    return res


def when_else_not_hit_break():
    """ else not hit due to break """
    res = 'else is not hit'
    for a in range(3):
        try:
            break;
        except:
            res = 'an exception is hit'
        else:
            res = 'else is hit'
    return res


def when_else_not_hit_continue():
    """ else not hit due to continue """
    res = 'else is not hit'
    for a in range(3):
        try:
            continue
        except:
            res = 'an exception is hit'
        else:
            res = 'else is hit'
    return res


class TestExceptionBasic(util.TestCaseBase):
    """ """

    def test_general_exp_before_specific(self):
        """ always put specific exception before more general ones """
        self.assertEqual(put_specific_before_general_exp(), 'an exception')

    def test_try_except_else(self):
        """ test try except else"""
        self.assertEqual(when_else_is_hit(), 'else is hit')
        self.assertEqual(when_else_not_hit_exception(), 'an exception is hit')
        self.assertEqual(when_else_not_hit_break(), 'else is not hit')
        self.assertEqual(when_else_not_hit_continue(), 'else is not hit')
