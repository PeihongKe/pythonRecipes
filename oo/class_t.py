import util


class B(object):
    a = 'B.a'
    b = 'B.b'

    def __init__(self, a=0):
        """ """
        self.a = a

    def f(self): return 'B.f()'

    def g(self): return 'B.g()'


class C(B):
    b = 'C.b'
    c = 'C.c'

    def __init__(self, a=0, d=0):
        """ call base class's ctor; super(type[, object-or-type])"""
        # way 1: old style class
        B.__init__(self, a)
        # way 2: python 2
        super(C, self).__init__(a)
        # way 3: python 3 What super does is: it calls the method from the next class in MRO (method resolution order).
        super().__init__(a)

        self.d = d

    def g(self): return 'C.g()'

    def h(self): return 'C.h()'


class TestClassHierarchy(util.TestCaseBase):
    """ """

    def test_data_attr_override(self):
        """ subclass override data attribute in super class """
        c = C()
        self.assertEqual(c.b, 'C.b')

    def test_method_attr_override(self):
        """ subclass override callable attribute in super class"""
        c = C()
        self.assertEqual(c.g(), 'C.g()')

    def test_super_basic(self):
        pass

    def test_super_multi_inheritance(self):
        # https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
        pass


class TestInheritantFromBuiltIn(util.TestCaseBase):
    """  test inheritance with built in types """

    def test_inherit_from_list(self):
        """ a class can inherit from built in types"""

        class MyList(list):
            """ inherit from builtin list"""

            def my_special_method(self):
                return "my special method"

        my_list = MyList()
        self.assertEqual(my_list.my_special_method(), 'my special method')


    def test_inherit_from_dict_list(self):
        """ multiple base classes have instance lay-out conflct"""
        with self.assertRaises(TypeError) as err:
            class MyListDict(dict, list): pass

        print(str(err.exception), 'multiple bases have instance lay-out conflict')

