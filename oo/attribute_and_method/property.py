import math

import util


# with property, it is safe to use public data attribute, as you can always add an abstraction on top of it whenever necesary

class Rectangle(object):
    """ """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """ as it says """
        return self.width * self.height

    read_only_area = property(fget=get_area, doc='area of the rectangle ')
    not_allowed_area = property(fget=None, fset=None, fdel=None, doc=None)

    @property # the x property. the decorator creates a read-only property
    def read_only_area_decorator(self):
        """ readonly using decorator """
        return self.width * self.height

    @property
    def read_write_area_decorator(self):
        return self.width * self.height

    @read_write_area_decorator.setter
    def read_write_area_decorator(self, value):
        scale = math.sqrt(value / self.read_write_area_decorator)
        self.width *= scale
        self.height *= scale


class TestProperty(util.TestCaseBase):
    """ property(fget=None, fset=None, fdel=None, doc=None) """

    def test_read_only_property(self):
        """ read only """
        r = Rectangle(2, 4)
        self.assertEqual(r.read_only_area, 8)

    def test_not_allowed_area(self):
        """ disallowed property"""
        r = Rectangle(2, 4)

        with self.assertRaises(AttributeError) as err:
            r.not_allowed_area

        msg = str(err.exception)
        self.assertEqual(msg, 'unreadable attribute')

    def test_read_only_area_decorator(self):
        """ read only using property """
        r = Rectangle(2, 4)
        self.assertEqual(r.read_only_area_decorator, 8)

    def test_read_write_area_decorator(self):
        """ read write using property """
        r = Rectangle(2, 4)
        self.assertEqual(r.read_only_area_decorator, 8)

        r.read_write_area_decorator = 32
        self.assertEqual(r.width, 4.0)
        self.assertEqual(r.height, 8.0)

    def test_property_inheritance(self):
        """ """

        class Base(object):
            def f(self):
                return 'base::f'

            g = property(f)

        class Derive(Base):
            def f(self):
                return 'drive::f'

        d = Derive()
        self.assertEqual(d.g, 'base::f')
