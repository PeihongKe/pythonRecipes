

class MyContainer(object):
    """ """

    def __len__(self):
        """ len() """

    def __getitem__(self, item):
        """ self[key]"""

    def __setitem__(self, key, value):
        """ self[key] = value"""

    def __delitem__(self, key):
        """ del self[key]"""

    def __iter__(self):
        """ iter() """

    def __reversed__(self):
        """ reversed() """

    def __contains__(self, item):
        """ in and not in"""

    def __missing__(self, key):
        """
        __missing__ is used in subclasses of dict .
        It defines behavior for whenever a key is accessed that does not exist in a dictionary (so, for instance,
        if I had a dictionary d and said d["george"] when "george" is not a key in the dict, d.__missing__("george") would be called).
        """