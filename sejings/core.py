# Created: 10/12/2019
# Author:  Emiliano Jordan,
# Project: settings


class Settings:

    def __call__(self, value=None):

        if value is None:
            return self._val

        self._val = value

    def __getattr__(self, item):

        setattr(self, item, Settings())
        return super(Settings, self).__getattribute__(item)

    def __setattr__(self, key, value):

        if key == '_val':
            super(Settings, self).__setattr__(key, value)
            return

        try:
            super(Settings, self).__getattribute__(key)
        except AttributeError:
            super(Settings, self).__setattr__(key, Settings())

        if isinstance(value, Settings):
            super(Settings, self).__setattr__(key, value)
            return

        super(Settings, self).__getattribute__(key)(value)

    ####################################################################
    # Mathematic Operations
    ####################################################################

    def __add__(self, other):
        return self() + other

    def __iadd__(self, other):
        self(self() + other)

    def __radd__(self, other):
        return self() + other

    def __sub__(self, other):
        return self() - other

    def __isub__(self, other):
        self(self() - other)

    def __rsub__(self, other):
        return other - self()

    def __mul__(self, other):
        return self() * other

    def __imul__(self, other):
        self(self() * other)

    def __rmul__(self, other):
        return self() * other

    def __truediv__(self, other):
        return self() / other

    def __itruediv__(self, other):
        self(self() / other)

    def __rtruediv__(self, other):
        return other / self()

    def __pow__(self, power, modulo=None):
        return pow(self(), power, modulo)

    def __ipow__(self, other):
        self(self() ** other)

    def __rpow__(self, other):
        return other ** self()

    def __neg__(self):
        return -self()

    def __pos__(self):
        return +self()

    def __abs__(self):
        return abs(self())

    def __invert__(self):
        return ~self()


settings = Settings()
