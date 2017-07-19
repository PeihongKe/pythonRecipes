import util

class TestScope(util.TestCaseBase):

    def test_outter_scope(self):
        """ """


        def function1():
            a = 1
            def function2():
                a =2
                b = a+1

                return b
            return function2()

        print(function1())