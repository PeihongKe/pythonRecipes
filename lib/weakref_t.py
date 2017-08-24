# https://pymotw.com/2/weakref/

import weakref

import util


class ExpensiveObject(object):
    """ """


class TestWeakRef(util.TestCaseBase):
    """ """

    def test_basic(self):
        """ weakref.ref """
        obj = ExpensiveObject()
        r = weakref.ref(obj)
        self.assertEqual(obj, r())

        del obj
        self.assertEqual(r(), None)

    def test_with_callback(self):
        """ weakref.ref with callback"""
        a = 1

        def callback(reference):
            nonlocal a
            a = 0

        obj = ExpensiveObject()
        r = weakref.ref(obj, callback)
        self.assertEqual(a, 1)
        del obj
        self.assertEqual(a, 0)
