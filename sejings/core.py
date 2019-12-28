# Created: 10/12/2019
# Author:  Emiliano Jordan,
# Project: sejings
import configparser
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Optional, Union, List

from .utils import in_doctest


class Sejings:

    def __init__(self, value=...):

        super().__setattr__('_val', value)

        super().__setattr__('children', dict())

    def __call__(self, value=...):

        if value is ...:
            return self._val

        super().__setattr__('_val', value)

    def __getattr__(self, item):

        if item == '__wrapped__' and in_doctest():
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

    def to_configparser(
            self,
            config: Optional[configparser.ConfigParser] = None,
            label: str = 'Sejings',
            parser='to_dict'
    ):

        if config is None:
            config = configparser.ConfigParser()

        parser = getattr(self, parser)
        config[label] = parser()

        return config

    def to_dict(self, storage_dict=None, key=''):

        if storage_dict is None:
            storage_dict = dict()

        if key and key[0] == '.':
            key = key[1:]

        if self._val is not ...:
            storage_dict[key] = copy.deepcopy(self._val)

        for iter_key, val in self.children.items():
            val.to_dict(storage_dict, f'{key}.{iter_key}')

        return storage_dict

    def to_json(self):

        return json.dumps(self.to_dict())

    def to_file(
            self,
            file: Union[str, Path],
            mode: str = 'w',
            label='Sejings',
            parser='to_dict'
    ):

        config = self.to_configparser(label=label, parser=parser)

        with open(file, mode=mode) as f:
            config.write(f)

    def update_from_dict(self, storage_dict: dict):

        sorting_dict = defaultdict(dict)

        for key, val in storage_dict.items():

            if '.' not in key:

                val = copy.deepcopy(val)

                if key not in self.__dict__:
                    setattr(self, key, Sejings(val))
                else:
                    getattr(self, key)(val)

                continue

            attr_parts = key.split('.')
            first_attr, attr_string = attr_parts[0], '.'.join(attr_parts[1:])

            sorting_dict[first_attr][attr_string] = val

        for key, val in sorting_dict.items():

            if key not in self.__dict__:
                setattr(self, key, Sejings())

            getattr(self, key).update_from_dict(val)

    @classmethod
    def from_dict(
            cls,
            storage_dict: dict
    ) -> 'Sejings':

        sejing = cls()
        sejing.update_from_dict(storage_dict)

        return sejing

    @classmethod
    def from_file(
            cls,
            file: Union[str, Path],
            labels: Union[List[str], str, None] = None,
            parser='from_dict'
    ) -> 'Sejings':

        config = configparser.ConfigParser()

        config.read(file)

        if labels is None:
            labels = list(config.keys())
        if not isinstance(labels, list):
            labels = [labels]

        iterator = {
            key: val
            for key, val
            in config.items()
            if key in labels
        }

        build_dict = dict()

        for key, val in iterator.items():
            build_dict = {**build_dict, **val}

        if len(build_dict) == 0:
            raise LookupError(f'label does not exist in file: {file}')

        parser = getattr(cls, parser)
        return parser(build_dict)


sejings = Sejings()
