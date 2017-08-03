import util


# http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html#attribute-search-summary
# Attribute Search Summary
# This is the long version of the attribute access story, included just for the sake of completeness.
# 1: When retrieving an attribute from an object (print objectname.attrname) Python follows these steps:
# 2: If attrname is a special (i.e. Python-provided) attribute for objectname, return it.
# 3 Check objectname.__class__.__dict__ for attrname. If it exists and is a data-descriptor, return the descriptor result. Search all bases of objectname.__class__ for the same case.
# 4: Check objectname.__dict__ for attrname, and return if found. If objectname is a class, search its bases too. If it is a class and a descriptor exists in it or its bases, return the descriptor result.Check objectname.__class__.__dict__ for attrname. If it exists and is a non-data descriptor, return the descriptor result. If it exists, and is not a descriptor, just return it. If it exists and is a data descriptor, we shouldn't be here because we would have returned at point 2. Search all bases of objectname.__class__ for same case.
# 5: Raise AttributeError


class B(object):
    """ a class for testing class level attributes """
    Version = 1.0

    def f(self):
        return "f defined in class"



class TestClassAttribute(util.TestCaseBase):
    """  test class level and instance level attributes """

    def test_cls_and_inst_attr(self):
        """ attribute on class level is shared by all instance,
        attributes on instance level is unique to that instance and hide the class level attributes """
        b = B()
        self.assertEqual(B.Version, 1.0)
        self.assertEqual(b.Version, 1.0)

        b.Version = 2.0

        self.assertEqual(B.Version, 1.0)
        self.assertEqual(b.Version, 2.0)




class VersionDataDescriptor(object):
    """ version data descriptor """

    def __init__(self):
        """ """
        self.value = 3.0

    def __get__(self, instance, owner):
        """ """
        return self.value

    def __set__(self, instance, value):
        """ """
        self.value = 3.0

class VersionNoneDataDescriptor(object):
    """ version non data descriptor """
    def __init__(self):
        """ """
        self.value = 1.0

    def __get__(self, instance, owner):
        """ """
        return self.value


class C(object):
    Version = VersionDataDescriptor()

class D(object):
    Version = VersionNoneDataDescriptor()


class TestAttributeSearchOrder(util.TestCaseBase):
    """ test attribute search order """

    def test_data_desc_higher_than_inst(self):
        """ data descriptor in the class (and its bases) higher than an attribute in the object __dict__ """
        c = C()
        c.Version = 2.0
        self.assertEqual(c.Version, 3.0)

    def test_inst_higher_than_non_data_desc(self):
        """  an attribute in the object __dict__ higher than a non-data descriptor in the class (and its bases). """
        d = D()
        d.Version = 2.0
        self.assertEqual(d.Version, 2.0)





