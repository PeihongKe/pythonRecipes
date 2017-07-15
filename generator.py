import util

# Iterators are objects that can be iterated upon.
# Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
# An object is called iterable if we can get an iterator from i,  like: list, tuple, string etc
# The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
# https://www.programiz.com/python-programming/iterator


class SquaresIter(object):
    """ iterator returning square of a range"""

    def __init__(self, start, stop, allowReIterate= False):
        """ iter """
        self.start = start
        self.stop = stop
        self._start = start
        self._stop = stop
        self._allowReIterate = False

    def __iter__(self):
        """ called by iter"""
        if self._allowReIterate:
            self.start = self._restart
            self.stop = self._stop
        return self

    def __next__(self):
        """return current and move to next"""
        if self.start >= self.stop:
            raise StopIteration
        curr = self.start * self.start
        self.start +=1
        return curr

    def current(self):
        """extra method that an iterator can have but not generator"""
        return self.start

class TestBuiltIns(util.TestCaseBase):
    """ test next() and iter() """

    def test_next(self):
        """ iter(collection); next """
        my_list = [1,2,3,4]
        my_iter = iter(my_list)
        self.assertEqual(next(my_iter), 1)
        self.assertEqual(next(my_iter), 2)
        self.assertEqual(my_iter.__next__(), 3)
        self.assertEqual(my_iter.__next__(), 4)
        with self.assertRaises(StopIteration):
            next(my_iter)

    def test_iter_sentinel(self):
        """ iter(callable, sentinel): iterate until sentinel is returned from callable """
        i = 1
        def odd_num():
            """ return 3, 5, 7, 9  ....."""
            nonlocal i
            i+= 2
            return i


        inf = iter(odd_num, 7)
        self.assertEqual(next(inf), 3)
        self.assertEqual(next(inf), 5)
        with self.assertRaises(StopIteration):
            next(inf)


class TestIterator(util.TestCaseBase):
    """test Iterator"""

    def test_iterate(self):
        outcome = [i for i in SquaresIter(1,5)]
        expected = [1, 4, 9, 16]
        self.assertEqual(outcome, expected)

    def test_iter(self):
        """ Return an iterator object. """
        ite = SquaresIter(1, 5)
        a = iter(ite)

    def test_next(self):
        """test __next__"""
        iter_obj = SquaresIter(1, 5)
        ite = iter(iter_obj)
        self.assertEqual(next(ite), 1)
        self.assertEqual(next(ite), 4)
        self.assertEqual(next(ite), 9)
        self.assertEqual(next(ite), 16)









