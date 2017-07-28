import util


class A(object):
    def return_name(self):
        return 'A::return_name'


class TestClassLevelMethod(util.TestCaseBase):
    """ static and class method"""

    def test_per_instance_method(self):
        """ instance specific binding hinds a class level binding"""
        a = A()
        self.assertEqual(a.return_name(), 'A::return_name')
        a.return_name = lambda: 'a::return_name'
        self.assertEqual(a.return_name(), 'a::return_name')

    def test_per_instance_method_special(self):
        """ instance cannot override special method """
        pass

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


class B(object):
    """ a class for testing class level attributes """
    Version = 1.0


class TestClassAttribute(util.TestCaseBase):
    """  test class level and instance level attributes """

    def test_class_attribute(self):
        """ attribute on class level is shared by all instance, attributes on instance level is unique to that instance"""
        b = B()
        self.assertEqual(B.Version, 1.0)
        self.assertEqual(b.Version, 1.0)

        b.Version = 2.0

        self.assertEqual(B.Version, 1.0)
        self.assertEqual(b.Version, 2.0)
