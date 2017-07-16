import util


class A(object):
    def whoami(self):
        return 'I am A'


class B(object):
    def whoami(self):
        return 'I am B'


class C(A, B):
    pass


class D(B, A):
    def whoami(self):
        return 'I am D'


# The MRO if a subclass is an extension without -re-ordering of the MROs of the superclasses
# linearization of a class using C3 algorithm


class TestMRO(util.TestCaseBase):
    def test_depth_first(self):
        d_obj = D()
        outcome = d_obj.whoami()
        expected = 'I am D'
        self.assertEqual(outcome, expected)

    def test_left_to_right(self):
        c_obj = C()
        outcome = c_obj.whoami()
        expected = 'I am A'
        self.assertEqual(outcome, expected)

    def test_inconsistent_method_resolution_error(self):
        with self.assertRaises(TypeError) as err:
            class E(C, D):
                pass
        outcome = (str(err.exception))
        expected1 = 'Cannot create a consistent method resolution\norder (MRO) for bases B, A'
        expected2 = 'Cannot create a consistent method resolution\norder (MRO) for bases A, B'
        self.assertTrue(outcome == expected1 or outcome == expected2)

    def test_inconsistent_method_resolution_error2(self):
        with self.assertRaises(TypeError) as err:
            class F(A, object, B):
                pass
        outcome = (str(err.exception))
        expected = 'Cannot create a consistent method resolution\norder (MRO) for bases object, B'
        self.assertTrue(outcome == expected)

    def test_mro_cls_attr(self):
        outcome = D.__mro__
        expected = (D, B, A, object)  # tuple
        self.assertEqual(outcome, expected)

    def test_mro_class_func(self):
        outcome = D.mro()
        expected = [D, B, A, object]  # list
        self.assertEqual(outcome, expected)
