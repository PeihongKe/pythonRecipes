import util
import numbers

class A(object):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return self.value == other
        elif isinstance(other, A):
            return self.value == other.value
        return False

    def __cmp__(self, other):
        """ self < other return -1; eq return0; otherwise, return 1
         It actually implements behavior for all of the comparison operators (<, ==, !=, etc.),
         It's usually best to define each comparison you need rather than define them all at once
        """
        if self.value< other.value:
            return -1
        elif self == other:
            return 0
        else:
            return 1


class TestComparison(util.TestCaseBase):
    """ """
    def test_equal(self):
        """ a ==  b is transfered to a.__eq__(b)"""
        a = A(1)
        self.assertTrue(a == 1)

    def test_cmp(self):
        """ """
        a1 = A(1)
        a2 = A(2)
        self.assertNotEqual(a1, a2)