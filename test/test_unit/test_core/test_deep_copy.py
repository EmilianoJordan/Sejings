# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
from copy import deepcopy

from sejings import Sejings


def test_initial():
    s = Sejings()

    s.one = 'one'
    s.two = 'two'
    s.one.one = 'one.one'
    s.one.two = 'one.two'
    s.two.three.four = 'two.three.four'

    c = deepcopy(s)

    assert c is not s

    assert c.one() == s.one()
    assert c.one() is s.one()  # strings are immutable.
    assert c.one is not s.one

    assert c.two.three.four() == s.two.three.four()
    assert c.two.three.four() is s.two.three.four()  # strings are immutable.
    assert c.two.three.four is not s.two.three.four


def test_mutable_objects():
    s = Sejings()

    s.one = 'one'
    s.two = 'two'
    s.one.one = ['one', 'one']
    s.one.two = ['one', 'two']
    s.two.three.four = ['two', 'three', 'four']

    c = deepcopy(s)

    assert c is not s

    assert c.one() == s.one()
    assert c.one() is s.one()  # strings are immutable.
    assert c.one is not s.one

    assert c.two.three.four() == s.two.three.four()
    assert c.two.three.four() is not s.two.three.four()
    assert c.two.three.four is not s.two.three.four
