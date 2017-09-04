import collections

import util

Person = collections.namedtuple('Person', 'name age gender')


class TestNamedTuple(util.TestCaseBase):
    """ test namedtuple from collections """

    def test_basic(self):
        """ """
        bob = Person(name='Rob', age=18, gender = 'M')
        fields = ('name', 'age', 'gender')
        self.assertEqual(fields, bob._fields)
        self.assertEqual(bob.name, 'Rob')
        self.assertEqual(bob.age, 18)

    def test_invalid_field_name(self):
        """ """
        with self.assertRaises(ValueError) as ctx:
            collections.namedtuple('Person', 'name class age gender')
            print(str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            collections.namedtuple('Person', 'name age gender age')

    def test_rename_true(self):
        """ """
        with_key_work_class = collections.namedtuple('Person', 'name class age gender', rename=True)
        expected = ('name', '_1', 'age', 'gender')
        self.assertEqual(with_key_work_class._fields, expected)

        with_duplicated_name = collections.namedtuple('Person', 'name age gender age', rename=True)
        expected = ('name', 'age', 'gender', '_3')
        self.assertEqual(with_duplicated_name._fields, expected)

