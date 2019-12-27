# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Sejings


def test_basic(settings):

    result = settings.to_dict()

    assert 'one' in result
    assert result['one'] == settings.one()

    assert 'two' in result
    assert result['two'] == settings.two()

    assert 'one.one' in result
    assert result['one.one'] == settings.one.one()

    assert 'one.two' in result
    assert result['one.two'] == settings.one.two()

    assert 'two.three.four' in result
    assert result['two.three.four'] == settings.two.three.four()

    # I want mutable object copied to avoid errors

    assert 'one.one.list' in result
    assert result['one.one.list'] == settings.one.one.list()
    assert result['one.one.list'] is not settings.one.one.list()

    assert 'types.dict' in result
    assert result['types.dict'] == settings.types.dict()
    assert result['types.dict'] is not settings.types.dict()
