import util

value = 0


def method_global():
    """ """
    global value
    value = 1
    return value


def method_nonlocal():
    """ test nonlocal """
    value = 100

    def method2():
        nonlocal value
        value = 200

    method2()
    return value


class TestGlobalNonlocal(util.TestCaseBase):
    """ global and nonlocal """

    def test_global(self):
        """ test global """
        self.assertEqual(value, 0)
        method_global()
        self.assertEqual(value, 1)

    def test_nonlocal(self):
        """ test nonlocal
         Nonlocal is similar in meaning to global.
         But it takes effect primarily in nested methods.
         It means "not a global or local variable.
        """
        v = method_nonlocal()
        self.assertEqual(v, 200)
