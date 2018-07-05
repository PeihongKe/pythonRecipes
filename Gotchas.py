import util


def append_to(elem, s=[]):
    s.append(elem)
    return  s

def append_to_right_version(elem, s = None):
    ''' working version '''
    if s is None:
        s = []
    s.append(elem)
    return s

def create_multipliers():
    # Python¡¯s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called.
    return [lambda x : i * x for i in [0,1,2,3,4]]

class TestGotchas(util.TestCaseBase):
    '''     '''
    def testMutableAsArgument(self):
        ''' '''
        append_to(1)
        l2 = append_to(2)
        self.assertTrue(l2 == [1,2]) # rather than [2] as you expected

        #right version
        append_to_right_version(1)
        l4 = append_to_right_version(2)
        self.assertTrue(l4 == [2])

    def testClosureLateBinding(self):
        for multiplier in create_multipliers():
            print(multiplier(2)) # prints out 8,8,8,8,8 instead of 0,2,4,6,8





