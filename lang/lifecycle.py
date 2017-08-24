import util


class TestLifeCycle(util.TestCaseBase):
    """ """

    def test_name_delete(self):
        """ delete a name """
        a = 1
        del a
        with self.assertRaises(UnboundLocalError) as err:
            a
            print(str(err))
