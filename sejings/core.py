# Created: 10/12/2019
# Author:  Emiliano Jordan,
# Project: settings


class Settings:

    def __call__(self, value=...):

        if value is ...:
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


settings = Settings()
