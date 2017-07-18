import util


class Rectangle(object):
    """ """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """ as it says """
        return self.width * self.height


class OptimizedRectangle(Rectangle):
    __slots__ =  ('width', 'height')


class TestSlot(util.TestCaseBase):
    """ __slots__: to save space"""

    def test_dict_with_slot(self):
        """ __dict__ when slots are specified """
        o_r = OptimizedRectangle(2, 4)
        self.assertEqual(o_r.__dict__, {})

        r = Rectangle(2,4)
        self.assertEqual(r.__dict__, {'width': 2, 'height': 4})

    def test_slot_with_slot(self):
        """ __slots__ when __slots__ is specified """
        o_r = OptimizedRectangle(2, 4)
        self.assertEqual(o_r.__slots__, ('width', 'height'))

        r = Rectangle(2, 4)
        with self.assertRaises(AttributeError) as err:
            r.__slots__
        self.assertEqual(str(err.exception), r"'Rectangle' object has no attribute '__slots__'")








