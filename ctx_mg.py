# https://contextlib2.readthedocs.io/en/stable/

from contextlib import contextmanager


class File(object):
    """ example of context manager """

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()


@contextmanager
def open_file(path, mode):
    """ exactly one yield, everything before yield is like __enter__, everything after yield is like in __exit__"""
    the_file = open(path, mode)
    yield the_file
    the_file.close()


from contextlib import ContextDecorator


class makeparagraph(ContextDecorator):
    """ ContextDecorator: A base class that enables a context manager to also be used as a decorator. """
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False


@makeparagraph()
def emit_html():
    """
    returns
    <p>
    Here is some non-HTML
    </p>
    """
    print('Here is some non-HTML')
