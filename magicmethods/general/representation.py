import util

class A(object):
    """ """
    def __str__(self):
        """ str() for human readable """

    def __repr__(self):
        """ repr() for machine readable, even machine code that can be evaluated by eval(repr(object))"""

    def __unicode__(self):
        """ unicode() """

    def __format__(self, format_spec):
        """ ???  """

    def __hash__(self):
        """ hash() """

    def __nonzero__(self):
        """ bool() python 2 """

    def __bool__(self):
        """ book python 3"""

    def __dir__(self):
        """ dir(), implement it if you redefine  __getattr__ or __getattribute__ """

    def __sizeof__(self):
        """ sys.getsizeof() """
