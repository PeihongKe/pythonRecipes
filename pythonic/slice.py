import util

items = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

class TestDictComprehension(util.TestCaseBase):

    def test_slice(self):
        print(items[:5])            # ['a', 'b', 'c', 'd', 'e']
        print(items[0:5])           # ['a', 'b', 'c', 'd', 'e']

        print(items[5:])            # ['f', 'g', 'h']
        print(items[5:len(items)])  # ['f', 'g', 'h']

        print(items[:])             #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        print(items[::-1])          #['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

        print(items[:])             # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        print(items[:-1])           # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        print(items[:-2])           # ['a', 'b', 'c', 'd', 'e', 'f']

        print(items[-3:-1])         # ['f', 'g']
        print(items[2:2])           # []
        print(items[3:2])           # []


        first_six = items[:6]
        last_six = items[-6:]

        print(first_six)            #['a', 'b', 'c', 'd', 'e', 'f']
        print(last_six)             #['c', 'd', 'e', 'f', 'g', 'h']

        b = items[:]
        assert b is not items

        b[2:4] = ["C", "D"]         #['a', 'b', 'C', 'D', 'e', 'f', 'g', 'h']
        print(b)


    def test_stride(self):

        print(items[::2])           #['a', 'c', 'e', 'g']
        print(items[::-2])          #['h', 'f', 'd', 'b']

        print(items[2::2])          #['c', 'e', 'g']
        print(items[-2::-2])        #['g', 'e', 'c', 'a']

        print(items[2:5:1])         #['c', 'd', 'e']
        print(items[2:5:-1])        #[]

        print(items[5:2:1])         #[]
        print(items[5:2:-1])        #['f', 'e', 'd']

        print(items[-2:2:1])        #[]
        print(items[-2:2:-1])       #['g', 'f', 'e', 'd']





