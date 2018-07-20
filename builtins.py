import util

class PowTwo(object):
    """class to implement an iterator protocol  """
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        """The __iter__() method returns the iterator object itself. If required, some initialization can be performed."""
        self.n = 0
        return self # needs to return the iterator object itself

    def __next__(self):
        """The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration."""
        if self.n<self.max  :
            res = 2** self.n
            self.n +=1
            return result
        else:
            raise StopIteration # to indicate foo loop that it stops

class PowTwo2(object):
    """If a container object’s __iter__() method is implemented as a generator,
    it will automatically return an iterator object (technically, a generator object) supplying the  __iter__() and next() methods."""

    def __iter__(self):
        yield 1
        yield 2
        yield 3


class TestIterator(util.TestCaseBase):

    def test_container(self):
        """get iterator from container"""
        list = [1,2,3,4]
        iterator = iter(list)
        print(next(iterator))

    def test_powTow2(self):
        it2 = PowTwo2()
        print(sum(it2))



class TestBuildIn(util.TestCaseBase):
    ''' built in function '''

    def test_sum(self):
        """ test sum(iterable) """
        self.assertTrue(sum([1, 2, 3]), 6)

    def test_sum_start(self):
        """ test sum(iterable, start )"""
        self.assertEqual(sum([1, 2, 3], 10), 16)

    def test_reversed(self):
        """ returns the reversed iterator of the given sequence: corresponding magic method __reversed__"""
        l = [1, 2, 3]
        expected = [3, 2, 1]
        self.assertEqual(list(reversed(l)), expected)

    def test_cha_ord(self):
        chr(97) == 'a'
        ord('a') == 97

