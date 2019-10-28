# Created: 10/26/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Settings
from sejings.core import SettingsNumber


def test_initial():
    s = Settings()

    s.one = 'one'
    s.two = 'two'

    assert s.one() == 'one'
    assert s.two() == 'two'

    s.one = 'uno'
    s.two = 'dos'

    assert s.one() == 'uno'
    assert s.two() == 'dos'


def test_number_factory():
    s = Settings()

    s.one = 1
    s.two = 2

    assert s.one() == 1
    assert s.two() == 2

    assert isinstance(s.one, SettingsNumber)
    assert isinstance(s.two, SettingsNumber)


def test_type_change():
    s = Settings()

    s.one = 'one'
    s.two = 'two'

    assert s.one() == 'one'
    assert s.two() == 'two'

    s.one = 1
    s.two = 2.0

    assert s.one() == 1
    assert s.two() == 2

    assert isinstance(s.one, SettingsNumber)
    assert isinstance(s.two, SettingsNumber)


def test_type_change_with_copy():
    s = Settings()

    s.one = 'one'
    s.two = 'two'
    s.one.one = 'one.one'
    s.one.two = 'one.two'

    assert s.one() == 'one'
    assert s.two() == 'two'

    s.one = 1
    s.two = 2.0

    assert s.one() == 1
    assert s.two() == 2

    assert isinstance(s.one, SettingsNumber)
    assert isinstance(s.two, SettingsNumber)

    assert s.one.one() == 'one.one'
    assert s.one.two() == 'one.two'

    assert s.one * 4 == 4