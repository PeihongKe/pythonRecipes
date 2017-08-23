import util


class OddMetaClass(type):
    """ __instancecheck__ and __subclasscheck__ must be defined in meta class """

    def __instancecheck__(self, instance):  #
        """ override isinstance(instance, class), self would be the super class """
        return instance.__class__.__name__.lower() == self.__name__.lower()

    def __subclasscheck__(self, subclass):
        """ issubclass(subclass, class), self would be the super class,
        overwrite the behaviour to return true only if it is a direct subclass """
        sup = self.__name__.lower()
        bases = [base.__name__.lower() for base in subclass.__bases__]

        return sup in bases


class MyInt(int, metaclass=OddMetaClass):
    """ """


class MYINT(int, metaclass=OddMetaClass):
    """ """


class MyIntInt(MyInt, metaclass=OddMetaClass):
    """ """


class MyIntIntInt(MyIntInt, metaclass=OddMetaClass):
    """ """


class IntInt(int):
    """ """


class IntIntInt(IntInt):
    """ """


class TestReflection(util.TestCaseBase):
    """  test isinstance and issubclass"""

    def test_builtin_isinstance(self):
        """ isinstance(instance, class) """
        self.assertEqual(isinstance(1, int), True)

    def test_builtin_issubclass(self):
        """ default checking if a type is a type of another type """
        self.assertEqual(issubclass(IntInt, object), True)
        self.assertEqual(issubclass(IntInt, int), True)

    def test_overwritten_isinstance(self):
        """ """
        r = MyInt()
        self.assertEqual(isinstance(r, MYINT), True)

    def test_overwritten_issubclass(self):
        """ issubclass behavour changed to check direct sup class"""
        self.assertTrue(issubclass(MyIntInt, MyInt))
        self.assertTrue(issubclass(MyIntIntInt, MyIntInt), )

        # not a direct sup class
        self.assertFalse(issubclass(MyIntIntInt, MyInt))
