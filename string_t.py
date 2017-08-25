# https://pyformat.info/

import util
import string

class Data(object):

    def __str__(self):
        """ """
        return 'str'

    def __repr__(self):
        """ """
        return 'repr'


class TestStr(util.TestCaseBase):
    """as it say"""

    def test_sub_string(self):
        """ """
        self.assertTrue('abc' in 'abcdefg')

    def test_capwords(self):
        """ capitalize words"""
        s = "the university of manchester !! 222 "
        s_c = "The University Of Manchester !! 222"
        self.assertEqual(string.capwords(s), s_c)

    # def test_maketrans(self):
    #     """ translate strings """
    #     leet = string.maketrans("abc", "123")
    #     input = "abcdef"
    #     print(input.translate(leet))

    def test_template(self):
        """ """
        values = {'var': 'foo'}
        t= string.Template("""
        $var
        $$
        ${var}iable
        """)
        res =  t.substitute(values)
        self.assertEqual(res, """
        foo
        $
        fooiable
        """)

    def test_interpolation(self):
        """ """
        values = {'var': 'foo'}
        s = """
        %(var)s
        %%
        %(var)siable
        """
        print(s%values)

    def test_format_basic_string(self):
        """ """
        old = '%s %s'%('one', 'two')
        new = '{} {}'.format('one', 'two')
        res = 'one two'
        self.assertEqual(old, res)
        self.assertEqual(new, res)

    def test_format_basic_int(self):
        """ """
        old = '%d %d' % (1,2)
        new = '{} {}'.format(1,2)
        res = '1 2'
        self.assertEqual(old, res)
        self.assertEqual(new, res)

    def test_new_format_with_pos(self):
        """ """
        s = '{1} {0}'.format('one', 'two')
        self.assertEqual(s, 'two one')

    def test_value_conversion(self):
        """ """
        old = '%s %r' %(Data(), Data())
        new = "{0!s} {0!r}".format(Data())
        res = 'str repr'
        self.assertEqual(old, res)
        self.assertEqual(new, res)

    def test_value_conversion_ascii(self):
        """ """
        class Data(object):
            def __repr__(self):
                return 'räpr'
        old = '%r %a' % (Data(), Data())
        new = '{0!r} {0!a}'.format(Data())
        res = 'räpr r\\xe4pr'
        self.assertEqual(old, res)
        self.assertEqual(new, res)

    def test_to_be_continue(self):
        """ """




