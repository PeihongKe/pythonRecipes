import util


class TestClassLevelMethod(util.TestCaseBase):
    """ static and class method"""

    def test_static_method(self):
        """ test builtin type staticmethod """

        class AClass(object):
            def a_static():
                return 'static method called'

            a_static = staticmethod(a_static)  # without this, calling from object would fail

        self.assertEqual(AClass.a_static(),
                         'static method called')  # this would success even without a_static = staticmethod(a_static)
        self.assertEqual(AClass().a_static(), 'static method called')

    def test_class_method(self):
        """ test builtin type classmethod """

        class ABase(object):
            def a_classmet(cls):
                return 'class method for' + cls.__name__

            a_classmet = classmethod(a_classmet)  # without this, calling from object would fail

        self.assertEqual(ABase.a_classmet(), 'class method forABase')
        self.assertEqual(ABase().a_classmet(), 'class method forABase')

        class ADeriv(ABase):
            pass

        self.assertEqual(ADeriv.a_classmet(), 'class method forADeriv')
        self.assertEqual(ADeriv().a_classmet(), 'class method forADeriv')

    def test_static_method_decorator(self):
        """ static method using decorator """

        class AClass(object):
            @staticmethod
            def a_static():
                return 'static method called'

        self.assertEqual(AClass.a_static(), 'static method called')
        self.assertEqual(AClass().a_static(), 'static method called')

    def test_class_method_decorator(self):
        """ class method using decorator """

        class ABase(object):
            @classmethod
            def a_classmet(cls):
                return 'class method for' + cls.__name__

        self.assertEqual(ABase.a_classmet(), 'class method forABase')
        self.assertEqual(ABase().a_classmet(), 'class method forABase')

        class ADeriv(ABase):
            pass

        self.assertEqual(ADeriv.a_classmet(), 'class method forADeriv')
        self.assertEqual(ADeriv().a_classmet(), 'class method forADeriv')
