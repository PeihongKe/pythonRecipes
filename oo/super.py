import util


class A(object):
    def met(self):
        res = ['A.met']
        return res


class B(A):
    def met(self):
        b = ['B.met']
        b.extend(super().met()) #  super(B, type(self))
        return b


class C(A):
    def met(self):
        c = ['C.met']
        c.extend(super().met()) # super(C, type(self))
        return c


class D(B, C):
    def met(self):
        d = ['D.met']
        d.extend(super().met()) # super(D, type(self))
        return d


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
                return type(self).__name__  # type of self here is not necessarily Base

        class Sub(Base):
            pass

        self.assertEqual(Sub().type_of_self(), 'Sub')
        self.assertFalse(Sub().type_of_self() == 'Base')

    def test_super_no_argument(self):
        """ """
        # print(super(D))
        # print(super())

    def test_super_two_argument(self):
        """ """
        proxy1 = super(B, D)
        proxy2 = super(B, D())
        self.assertTrue(proxy1, proxy2)

    def test_super_error_1(self):
        """ super(type, obj): type should be a sub class of type(obj) """
        with self.assertRaises(TypeError) as err:
            super(D, B)
        error_msg = str(err.exception)
        expected_msg = 'super(type, obj): obj must be an instance or subtype of type'
        self.assertEqual(error_msg, expected_msg)

    def test_super_error_2(self):
        """ super(type, obj): type should be a super set of type(obj) """
        with self.assertRaises(TypeError) as err:
            b = B()
            super(D, b)
        error_msg = str(err.exception)
        expected_msg = 'super(type, obj): obj must be an instance or subtype of type'
        self.assertEqual(error_msg, expected_msg)

    def test_super_multi_inheritance(self):
        """ test how super() works in multi inheritance """
        a = A()
        b = B()
        c = C()
        d = D()
        a_res = ['A.met']
        b_res = ['B.met', 'A.met']
        c_res = ['C.met', 'A.met']
        d_res = ['D.met', 'B.met', 'C.met', 'A.met']  # multi inheritance works out itself because of super()
        self.assertEqual(a.met(), a_res)
        self.assertEqual(b.met(), b_res)
        self.assertEqual(c.met(), c_res)
        self.assertEqual(d.met(), d_res)

    def test_super_second_type_mro(self):
        """ mro of the second arg or super()"""
        d = D()
        s = super(B, d)
        mro = s.__self_class__.mro()
        self.assertEqual(mro, [D, B, C, A, object])




