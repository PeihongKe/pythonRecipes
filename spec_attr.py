import util
import types

def a_function():
    return 'I am a function'


class AClass():
    """ """
    def a_class_func(self):
        """ """
        return 'a class function'


class TestSpecialAttr(util.TestCaseBase):
    """ test special attributes """
    def test__name__(self):
        """ test __name__  """
        self.assertEqual(a_function.__name__, 'a_function')
        self.assertEqual(AClass.__name__, 'AClass')
        with self.assertRaises(AttributeError) as err:
            AClass().__name__
        self.assertEqual(str(err.exception), r"'AClass' object has no attribute '__name__'")

    def test__class__(self):
        """ test __class__ """
        #print(a_function.__class__)
        self.assertEqual(a_function.__class__, types.FunctionType)
        self.assertEqual(AClass.__class__, type)
        self.assertEqual(AClass().__class__, AClass)


