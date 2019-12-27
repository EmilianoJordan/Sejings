# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Sejings


def test_basic():

    s = Sejings()

    s.one = 'one'
    s.two = 'two'
    s.one.one = ['one', 'one']
    s.one.two = ['one', 'two']
    s.two.three.four = ['two', 'three', 'four']

    result = s.to_dict()

    assert 'one' in result
    assert result['one'] == s.one()

    assert 'two' in result
    assert result['two'] == s.two()

    assert 'one.one' in result
    assert result['one.one'] == s.one.one()

    assert 'one.two' in result
    assert result['one.two'] == s.one.two()

    assert 'two.three.four' in result
    assert result['two.three.four'] == s.two.three.four()