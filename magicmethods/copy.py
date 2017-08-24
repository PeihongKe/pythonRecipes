import copy

import util


class Object(object):
    """ """

    def __init__(self, value):
        """ """
        self.v = value


class MyObject(object):
    """ overwrite copy: you may want to fine control it for example copy of cache """

    def __init__(self, value=0, obj = None):
        """ """
        self.a = value
        self.a_object = obj

    def __copy__(self):
        """shallow copy"""
        print("shallow copy")
        shallow_cpy = MyObject(self.a, self.a_object)
        return shallow_cpy

    def __deepcopy__(self, memodict={}):
        """ deep copy:"""
        print("deep copy")
        deep_cpy = MyObject(self.a, Object(self.a_object.v))
        return deep_cpy


class TestCopy(util.TestCaseBase):
    """ test shallow and deep copy """

    def test_shallow_copy(self):
        """ shallow copy: copy.copy() """
        obj = MyObject(1, Object(1))
        shallow_cpy = copy.copy(obj)
        self.assertFalse(obj == shallow_cpy)
        self.assertTrue(obj.a_object == shallow_cpy.a_object)

    def test_deep_copy(self):
        """ deep copy: copy.deepcopy() """
        obj = MyObject(1, Object(1))
        deep_cpy = copy.deepcopy(obj)
        self.assertFalse(obj == deep_cpy)
        self.assertFalse(obj.a_object == deep_cpy.a_object)
