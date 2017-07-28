import util

# https://docs.python.org/3.6/howto/descriptor.html
# a descriptor is an object that represents the value of an attribute





class MyDataDescriptor(object):
    """ a simple data descriptor """
    def __get__(self, obj, cls):
        return 'my secret data'

class Account(object):
    """ """
    data = MyDataDescriptor()
    def __init__(self):
        self.inst_data = MyDataDescriptor()


class TestDescriptorBasic(util.TestCaseBase):
    """ """
    def test_basic(self):
        """  object.__getattribute__() transforms b.x into type(b).__dict__['x'].__get__(b, type(b)) """
        acc = Account()
        self.assertEqual(acc.data, type(acc).__dict__['data'].__get__(acc, type(acc)))
        self.assertEqual(type(acc.data), str)

    def test_descriptor_should_only_be_cls_attr(self):
        """ descriptors should only be defined as class attributes """
        acc = Account()
        self.assertNotEqual(acc.inst_data, type(acc).__dict__['data'].__get__(acc, type(acc)))
        self.assertEqual(type(acc.inst_data), MyDataDescriptor)





