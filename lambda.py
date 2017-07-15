import util
import types


class TestLambda(util.TestCaseBase):
    """ """

    def test_lambda_type(self):
        """ test lambda """
        one_func = lambda: 1  #
        self.assertEqual(type(one_func), types.FunctionType)  # types.FunctionType == types.LambdaType returns true
        self.assertEqual(type(one_func), types.LambdaType)

    def test_basic(self):
        """ basic """
        one_func = lambda: 1
        self.assertEqual(one_func(), 1)

    def test_capture(self):
        """ """
        a = 1
        plus_a_func = lambda x, a=a: x + a
        self.assertEqual(plus_a_func(1), 2)
