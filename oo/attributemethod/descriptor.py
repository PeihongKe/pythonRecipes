import util


# https://docs.python.org/3.6/howto/descriptor.html
# a descriptor is an object that represents the value of an attribute
# a.x has a lookup chain starting with a.__dict__['x'], then type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses.
# http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html#attribute-search-summary

class DataDescriptor(object):
    """ Those methods are __get__(), __set__(), and __delete__(). If any of those methods are defined for an object, it is said to be a descriptor. """

    def __init__(self, value):
        """ """
        self.value = value

    def __get__(self, obj, cls=None):  # obj instance may be None if the attribute was accessed from the class.
        """ """
        return self.value

    def __set__(self, obj, value):
        """ """
        self.value = value


class NonDataDescriptor(object):
    """  Descriptors that only define __get__() are called non-data descriptors (they are typically used for methods but other uses are possible). """

    def __get__(self, obj, cls=None):
        return 'my secret data'


class ReadOnlyDataDescriptor(object):
    """ read only data descriptor """

    def __get__(self, obj, cls=None):
        return 'data'

    def __set__(self, obj, value):
        raise AttributeError()


class Account(object):
    """ """
    data = DataDescriptor('Account.data')
    non_data = NonDataDescriptor()

    def __init__(self):
        self.inst_data = DataDescriptor('account inst data')


class TestDescriptorBasic(util.TestCaseBase):
    """ """

    def test_descriptor_as_cls_attr(self):
        """  object.__getattribute__() transforms b.x into type(b).__dict__['x'].__get__(b, type(b)) """
        acc = Account()
        self.assertEqual(acc.data, type(acc).__dict__['data'].__get__(acc, type(acc)))
        self.assertEqual(type(acc.data), str)

    def test_descriptor_should_only_be_cls_attr(self):
        """ descriptors should only be defined as class attributes """
        acc = Account()
        self.assertNotEqual(acc.inst_data, type(acc).__dict__['data'].__get__(acc, type(acc)))
        self.assertNoteEqual(type(acc.inst_data), str)
        self.assertEqual(type(acc.inst_data), DataDescriptor)

    def test_descriptor(self):
        """  access attribute directly from descriptor """
        acc = Account()
        desc = DataDescriptor('Account.data')
        self.assertEqual(acc.data, desc.__get__(acc))
