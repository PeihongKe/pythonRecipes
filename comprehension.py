import util


class TestListComprehension(util.TestCaseBase):
    """list comprhension """

    def test_basic(self):
        """ basic case"""
        outcome = [x + 1 for x in range(0, 10, 2)]
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(outcome, expected)

    def test_with_if(self):
        """ with if"""
        outcome = [x + 1 for x in range(0, 10, 2) if x % 3 == 0 and x >= 3]
        expected = [7]
        self.assertEqual(outcome, expected)

    def test_nested_for(self):
        """ nested for """
        my_list = ['abc', 'DeF', 'ghI', 'jKl']
        outcome = [my_char.lower() for my_str in my_list for my_char in my_str]
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        self.assertEqual(outcome, expected)

    def test_nested_for_if(self):
        """ as it says """
        my_list = ['abc', 'DeF', 'ghI', 'jKl', 'MLOPQ']
        outcome = [my_char for my_str in my_list if len(my_str) == 3 for my_char in my_str if my_char.islower()]
        expected = ['a', 'b', 'c', 'e', 'g', 'h', 'j', 'l']
        self.assertEqual(outcome, expected)

    def test_nested_for_if_2(self):
        """ if """
        outcome = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
        expected = [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
        self.assertEqual(outcome, expected)


class TestSetComprehension(util.TestCaseBase):
    """as it says"""

    def test_basic(self):
        """ basic case """
        outcome = {x + 1 for x in range(0, 10)}
        expected = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(outcome, expected)

    def test_with_if(self):
        """ with if """
        outcome = {x for x in range(2, 10)
                   if not any(x % y == 0 for y in range(2, x))}  # primes between 2 and 11
        expected = {2, 3, 5, 7}
        self.assertEqual(outcome, expected)


class TestDictComprehension(util.TestCaseBase):
    """ as it says """

    def test_basic(self):
        """ as it says """
        outcome = {x: x ** 2 for x in range(1, 5)}
        expected = {1: 1, 2: 4, 3: 9, 4: 16}
        self.assertEqual(outcome, expected)

    def test_basic_2(self):
        """ nested for """
        keys = [1, 2, 3, 4]
        values = ['a', 'b', 'c', 'd']
        outcome = {x: y for (x, y) in zip(keys, values)}
        expected = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        self.assertEqual(outcome, expected)
