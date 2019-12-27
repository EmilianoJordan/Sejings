# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
import copy
from pathlib import Path

from pytest import fixture

from sejings import Sejings


########################################################################
#
# File paths and operations.
#
########################################################################
@fixture(scope='session')
def test_root() -> Path:
    return Path(__file__).parent


@fixture(scope='session')
def data_root(test_root) -> Path:
    return test_root / 'data'


@fixture(scope='function')
def blank_ini_file(data_root) -> Path:
    file = data_root / 'blank.ini'

    if file.is_file():
        file.unlink()

    file.touch()

    yield file

    if file.is_file():
        file.unlink()


########################################################################
#
# Example Sejings objects labeled as settings and variations of.
#
########################################################################
@fixture(scope='session')
def _settings() -> Sejings:
    settings = Sejings()

    settings.one = 'one'
    settings.two = 'two'
    settings.one.one = 'one.one'
    settings.one.two = 'one.two'

    settings.one.one.list = ['one', 'one']
    settings.one.two.list = ['one', 'two']

    settings.two.three.four = 'two.three.four'
    settings.types.list = ['two', 'three', 'four', 'list']
    settings.types.dict = {
        2: 'two',
        'three.two': 3.2,
        'list': ['two', 'three', 'four']
    }
    return settings


@fixture(scope='function')
def settings(_settings, blank_ini_file):

    s = copy.deepcopy(_settings)
    s.path = blank_ini_file

    return s
