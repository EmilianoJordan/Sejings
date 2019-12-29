# Created: 10/12/2019
# Author:  Emiliano Jordan,
# Project: sejings
import sys

def _in_doctest():
    """
    Determined by observation

    Thanks! https://stackoverflow.com/questions/8116118/
    how-to-determine-whether-code-is-running-in-a-doctest
    """
    if '_pytest.doctest' in sys.modules:
        return True
    ##
    if hasattr(sys.modules['__main__'], '_SpoofOut'):
        return True
    ##
    if sys.modules['__main__'].__dict__.get('__file__', '').endswith('/pytest'):
        return True
    ##
    return False

class Sejings:

    def __init__(self, value=...):

        super().__setattr__('_val', value)

        super().__setattr__('children', dict())

    def __call__(self, value=...):

        if value is ...:
            return self._val

        super().__setattr__('_val', value)

    def __getattr__(self, item):

        if item == '__wrapped__' and _in_doctest():
            raise AttributeError

        setattr(self, item, Sejings())
        return super().__getattribute__(item)

    def __setattr__(self, key, value):

        if key == '_val':
            super().__setattr__(key, value)
            return

        children: dict = super().__getattribute__('children')

        if isinstance(value, Sejings):
            super().__setattr__(key, value)
            children[key] = value
            return

        try:
            obj = super().__getattribute__(key)
            obj(value)
        except AttributeError:
            new_sejings = Sejings(value)
            super().__setattr__(key, new_sejings)
            children[key] = new_sejings
            return

    def __len__(self):
        return len(self.children)

    def __copy__(self):
        cls = self.__class__

        new = cls()

        iterator: dict = self.children
        iterator['_val'] = self._val

        for attr, val in iterator.items():
            if isinstance(val, cls):
                setattr(new, attr, val.__copy__())
            else:
                setattr(new, attr, val)

        return new

    def __deepcopy__(self, memodict):

        cls = self.__class__

        new = cls()

        memodict[id(self)] = new

        iterator: dict = self.children
        iterator['_val'] = self._val

        for attr, val in iterator.items():

            if id(val) in memodict:
                setattr(new, attr, memodict[id(val)])

            elif hasattr(val, '__deepcopy__'):
                setattr(new, attr, val.__deepcopy__(memodict))

            elif hasattr(val, 'copy') and callable(getattr(val, 'copy')):

                attr_copy = val.copy()

                if attr is not attr_copy:
                    memodict[id(val)] = attr_copy

                setattr(new, attr, attr_copy)

            elif hasattr(val, '__copy__'):

                attr_copy = val.__copy__()

                if attr is not attr_copy:
                    memodict[id(val)] = attr_copy

                setattr(new, attr, attr_copy)

            else:

                setattr(new, attr, val)

        return new



sejings = Sejings()
