import util


def empty_class_factory(cls_name):
    """ factory for creating empty class """
    # arg1: class name;
    # arg2: tuple giving the parent classes of the class to be constructed
    # arg3: a dictionary of the attributes and methods of the class to be constructed
    return type(cls_name, (), {})


def create_a_class(directly=True):
    """ create a class directly or indirectly use type class """
    if directly:
        class Foo(object):
            i = 4

        class Bar(Foo):
            def get_i(self):
                return self.i

        return Bar
    else:
        Foo = type('Foo', (), dict(i=4))
        Bar = type('Bar', (Foo,), dict(get_i=lambda self: self.i))
        return Bar


class TestMetaClassBasic(util.TestCaseBase):
    """ test basic concept """

    def test_class_type(self):
        """ test class type """
        self.assertEqual(int, type(1))
        self.assertEqual(type, type(int))
        self.assertEqual(type, type(type))

    def test_default_metaclass(self):
        """ test type is the default meta class for all classes """
        self.assertEqual(type(int), type)
        self.assertEqual(type(dict), type)
        self.assertEqual(type(float), type)
        self.assertEqual(type(type), type)

    def test_class_from_type(self):
        """ create a class from type class """
        empty_cls_name = 'Foo'
        empty_class = empty_class_factory(empty_cls_name)
        self.assertEqual(empty_cls_name, empty_class.__name__)

    def test_class_creation(self):
        """ test creating a class directly or indirectly """
        class_directly = create_a_class(True)
        class_indirectly = create_a_class(False)
        self.assertEqual('Bar', class_directly.__name__)
        self.assertTrue('get_i' in class_directly.__dict__.keys())


class InterfaceMeta(type):
    ''' a metaclass inherit from the default meta class type'''

    def __new__(cls, name, parents, dct):
        # create a class_id if it's not specified
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()

        # open the specified file for writing
        if 'file' in dct:
            filename = dct['file']
            dct['file'] = open(filename, 'w')

        # we need to call type.__new__ to complete the initialization
        return super(InterfaceMeta, cls).__new__(cls, name, parents, dct)


class TestMetaClassModifyingAttributes(util.TestCaseBase):
    """ test custom metaclass modifying attributes
    example from: https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/
    """

    def test_interface_metaclass(self):
        """ test InterfaceMeta"""
        interface = InterfaceMeta('Interface', (), dict(file='tmp.txt'))
        self.assertTrue(type(interface) == InterfaceMeta)
        self.assertFalse(type(interface) == type)
        self.assertEqual(interface.class_id, 'interface')
        self.assertEqual(str(type(interface.file)), r"<class '_io.TextIOWrapper'>")


class DBInterfaceMeta(type):
    # we use __init__ rather than __new__ here because we want
    # to modify attributes of the class *after* they have been
    # created
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, 'registry'):
            # this is the base class.  Create an empty registry
            cls.registry = {}
        else:
            # this is a derived class.  Add cls to the registry
            interface_id = name.lower()
            cls.registry[interface_id] = cls

        super(DBInterfaceMeta, cls).__init__(name, bases, dct)


class DBInterface(metaclass=DBInterfaceMeta):
    """ """


class TestMetaClassRegisterSubClasses(util.TestCaseBase):
    """ use case of meta class """

    def test_1(self):
        """ """
        self.assertEqual(DBInterface.registry, {})

    def test_2(self):
        """ """

        class FirstInterface(DBInterface):
            pass

        self.assertTrue('firstinterface' in DBInterface.registry.keys())


MyMeta_New_Arg = {}
MyMeta_Init_Arg = {}


class MyMeta(type):
    """  """

    def __new__(meta, name, bases, dct):
        """ """
        MyMeta_New_Arg['meta'] = meta
        MyMeta_New_Arg['name'] = name
        MyMeta_New_Arg['bases'] = bases
        MyMeta_New_Arg['dct'] = dct
        return super(MyMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        """ """
        MyMeta_Init_Arg['cls'] = cls
        MyMeta_Init_Arg['name'] = name
        MyMeta_Init_Arg['bases'] = bases
        MyMeta_Init_Arg['dct'] = dct
        return super(MyMeta, cls).__init__(name, bases, dct)

    #def __prepare__(metacls, name, bases):

    #def __call__(self, *args, **kwargs):


class MyKlass(object, metaclass=MyMeta):
    def foo(self, param):
        pass

    barattr = 2


class TestMetaClassMethods(util.TestCaseBase):
    """ a meta class's method __new__ __init__ and __call"""

    def test_meta_class_new_arg(self):
        """ test the argument of meta class's __new__"""
        self.assertEqual(MyMeta_New_Arg['meta'], MyMeta)
        self.assertEqual(MyMeta_New_Arg['name'], 'MyKlass')
        self.assertEqual(MyMeta_New_Arg['bases'], (object,))
        self.assertTrue('foo' in MyMeta_New_Arg['dct'].keys())
        self.assertTrue('barattr' in MyMeta_New_Arg['dct'].keys())

    def test_meta_class_init_arg(self):
        """ test the arguments of meta class's __init__ """
        k = MyKlass()
        self.assertEqual(MyMeta_Init_Arg['cls'], MyKlass)
        self.assertEqual(MyMeta_Init_Arg['name'], 'MyKlass')
        self.assertEqual(MyMeta_Init_Arg['bases'], (object,))
        self.assertTrue('foo' in MyMeta_Init_Arg['dct'].keys())
        self.assertTrue('barattr' in MyMeta_Init_Arg['dct'].keys())
