import unittest


class TestCaseBase(unittest.TestCase):

    @classmethod
    def run_tests(cls):
        test = unittest.defaultTestLoader.loadTestsFromTestCase(cls)
        unittest.TextTestRunner().run(test)