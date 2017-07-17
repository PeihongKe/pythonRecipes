import util

class TestList(util.TestCaseBase):
    """ test builtin List"""

    def test_extend_return_None(self):
        """ """
        a = ['a']
        b = ['b']
        self.assertEqual(b.extend(a), None)
        self.assertEqual(b, ['b', 'a'])