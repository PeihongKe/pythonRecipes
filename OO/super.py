import util
import types

class A(object): pass


class B(A): pass


class C(A): pass


class D(B, C): pass


# http://sixty-north.com/blog/series/pythons-super-explained
# When you invoke super() in Python [4], what actually happens is that you construct an object of type super
# The benefits of super() in single-inheritance are minimal. However, it's almost impossible to use multiple-inheritance without super().

class TestSuperProxy(util.TestCaseBase):
    """ test the super builtin function """

    def test_super_type(self):
        """ the type of super"""
        s = super(C)
        self.assertEqual(type(s), super)

    def test_type_of_self(self):
        ''' type of self is not the class implement the method '''
        class Base(object):
            def type_of_self(self):
                return type(self).__name__ # type of self here is not Base

        class Sub(Base):
            pass

        self.assertEqual(Sub().type_of_self(), 'Sub')
        self.assertFalse(Sub().type_of_self() == 'Base')

    def test_super_no_argument(self):
        """ """
        super()



