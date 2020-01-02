# Created: 1/2/2020
# Author:  Emiliano Jordan,
# Project: sejings
import copy


def test_basic_repr(settings):
    assert 'settings.int' in repr(settings.int)
    assert str(settings.int()) in repr(settings.int)

    assert 'settings.types.list' in repr(settings.types.list)
    assert str(settings.types.list()) in repr(settings.types.list)


def test_copy_sejing_to_branch(settings):
    _copy = copy.deepcopy(settings.types.list)
    settings.list = _copy

    assert 'settings.list' in repr(settings.list)
    assert str(settings.list()) in repr(settings.list)
