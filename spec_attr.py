import types

import util


def a_function():
    return 'I am a function'


class AClass():
    """ """
    class_attr = "attr on class"

    def a_class_func(self):
        """ """
        return 'a class function'


class TestSpecialAttr(util.TestCaseBase):
    """ test special attributes """

    def test__name__(self):
        """ test __name__  """
        self.assertTrue(hasattr(a_function, '__name__'))
        self.assertTrue(hasattr(AClass, '__name__'))
        self.assertFalse(hasattr(AClass(), '__name__'))

    def test__class__(self):
        """ test __class__ """
        self.assertEqual(a_function.__class__, types.FunctionType)
        self.assertEqual(AClass.__class__, type)
        self.assertEqual(AClass().__class__, AClass)
        self.assertEqual(AClass.__class__.__class__, type)

    def test_class__dict__(self):
        """ """
        self.assertEqual(AClass.__dict__['class_attr'], 'attr on class')

    def test_default_inst_dict(self):
        """ the instance dict by default is empty"""
        a = AClass()
        self.assertEqual(len(a.__dict__), 0)

    def test_inst_dict(self):
        """  instance dict can be set  __dict__ contains only the user-provided attributes. """
        a = AClass()
        a.inst_attr = 'attr on instance'
        self.assertEqual(next(iter(a.__dict__.keys())), 'inst_attr')

    def test_access_cls_attr_from_instance(self):
        """ class attributes are accessible from an instance """
        a = AClass()
        self.assertEqual(a.class_attr, 'attr on class')
