import util


class TestMethods(util.TestCaseBase):
    """" """

    def test_return_none_by_default(self):
        """ return none if not return statement """
        def return_none_func():
            a = 1

        self.assertEqual(return_none_func(), None)