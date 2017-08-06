import datetime
from os.path import join

import util


class FileObject(object):
    '''Wrapper for file objects to make sure the file gets closed on deletion.'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


class A(object):
    """ a class with __new__ defined """
    def __new__(cls, *args, **kwargs):
        """ __new__ is a static method, i.e., on class level """
        new_instance = object.__new__(cls, *args, **kwargs)
        setattr(new_instance, 'created_at', datetime.datetime.now())
        return new_instance

    def __init__(self, a, b):
        self.a, self.b = a, b


class TestLifeCycleFunctions(util.TestCaseBase):
    """ """

    def test_new_type(self):
        """ __new__ receives all the arguments that we pass while calling the class.
        __new__(cls, *args, **kwargs)
        """
        print(type(object.__dict__['__new__']))
