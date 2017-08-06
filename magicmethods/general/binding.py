#http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods
import util

class A(object):
    """ a test class"""
    # pass

class TestBindingBasic(util.TestCaseBase):
    """ """
    def test_setattr(self):
        """ (object, name, value)
        setattr(x, 'foobar', 123) is equivalent to x.foobar = 123
        """
        a = A()
        setattr(a, 'abc', 1)
        a.efg = 2

        self.assertEqual(a.abc, 1)
        self.assertEqual(a.efg, 2)



