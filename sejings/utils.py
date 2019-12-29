# Created: 12/29/2019
# Author:  Emiliano Jordan,
# Project: sejings
import configparser
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Optional, Union, List

from .core import Sejings


def to_configparser(
        sejing,
        config: Optional[configparser.ConfigParser] = None,
        label: str = 'Sejings',
):
    if config is None:
        config = configparser.ConfigParser()

    config[label] = to_dict(sejing)

    return config


def to_dict(sejing, storage_dict=None, key=''):
    if storage_dict is None:
        storage_dict = dict()

    if key and key[0] == '.':
        key = key[1:]

    if sejing() is not ...:
        storage_dict[key] = copy.deepcopy(sejing())

    for iter_key, val in sejing.children.items():
        to_dict(val, storage_dict, f'{key}.{iter_key}')

    return storage_dict


def to_json(sejing):
    return json.dumps(to_dict(sejing))


def to_config_file(
        sejing,
        file: Union[str, Path],
        mode: str = 'w',
        label='Sejings',
):
    config = to_configparser(sejing, label=label)

    with open(file, mode=mode) as f:
        config.write(f)


def update_from_dict(sejing, storage_dict: dict):
    sorting_dict = defaultdict(dict)

    for key, val in storage_dict.items():

        if '.' not in key:

            val = copy.deepcopy(val)

            if key not in sejing.__dict__:
                setattr(sejing, key, Sejings(val))
            else:
                getattr(sejing, key)(val)

            continue

        attr_parts = key.split('.')
        first_attr, attr_string = attr_parts[0], '.'.join(attr_parts[1:])

        sorting_dict[first_attr][attr_string] = val

    for key, val in sorting_dict.items():

        if key not in sejing.__dict__:
            setattr(sejing, key, Sejings())

        update_from_dict(getattr(sejing, key), val)


def from_dict(
        storage_dict: dict
) -> 'Sejings':
    sejing = Sejings()
    update_from_dict(sejing, storage_dict)

    return sejing


def from_config_file(
        file: Union[str, Path],
        labels: Union[List[str], str, None] = None,
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

    return from_dict(build_dict)
