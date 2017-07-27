import util

Reach_Function_Pos = 0
Curr = None
Value = None


def minimize():
    global Curr
    global Value
    global Reach_Function_Pos

    Reach_Function_Pos = 1
    Curr = yield
    Reach_Function_Pos = 2
    while True:
        Reach_Function_Pos = 3
        Value = yield Curr  # stop after yield current and wait for the next send to assign data to value
        Reach_Function_Pos = 4
        Curr = min(Value, Curr)
        Reach_Function_Pos = 5


class TestCoroutine(util.TestCaseBase):
    """ """

    def test_1(self):
        it = minimize()
        self.assertEqual(Reach_Function_Pos, 0)

        res = next(it)
        self.assertEqual(Reach_Function_Pos, 1)
        self.assertEqual(Curr, None)
        self.assertEqual(res, None)
        self.assertEqual(Value, None)

        res = it.send(10)
        self.assertEqual(Reach_Function_Pos, 3)
        self.assertEqual(Curr, 10)
        self.assertEqual(res, 10)
        self.assertEqual(Value, None)

        res = it.send(15)
        self.assertEqual(Reach_Function_Pos, 3)
        self.assertEqual(Value, 15)
        self.assertEqual(Curr, 10)
        self.assertEqual(res, 10)

        res = it.send(5)
        self.assertEqual(Reach_Function_Pos, 3)
        self.assertEqual(Value, 5)
        self.assertEqual(res, 5)
        self.assertEqual(Curr, 5)


def yield_empty():
    """ yield without anything"""
    yield
    yield
    yield


def yield_none():
    """ yield none"""
    yield None
    yield None
    yield None


class TestSendNoneYieldNone(util.TestCaseBase):
    """ send(None) is yield"""

    def test_yield_none(self):
        """ yield empty and yield none is quievalent """
        y_empty = yield_empty()
        y_none = yield_none()
        self.assertEqual(next(y_empty), None)
        self.assertEqual(next(y_none), None)

    def test_next_and_send_none(self):
        """ next and send none is equivalent """
        gen = (i for i in range(4))
        i = next(gen)
        j = gen.send(None)
        k = gen.__next__()
        l = gen.send(None)

        self.assertEqual(i, 0)
        self.assertEqual(j, 1)
        self.assertEqual(k, 2)
        self.assertEqual(l, 3)
