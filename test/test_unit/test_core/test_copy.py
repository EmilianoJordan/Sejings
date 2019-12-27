# Created: 12/26/2019
# Author:  Emiliano Jordan,
# Project: sejings
from copy import copy

from sejings import Sejings


def test_initial():
    s = Sejings()

    s.one = 'one'
    s.two = 'two'
    s.one.one = 'one.one'
    s.one.two = 'one.two'
    s.two.three.four = 'two.three.four'

    c = copy(s)

    assert c is not s

    assert c.one() == s.one()
    assert c.one() is s.one()
    assert c.one is not s.one

    assert c.two.three.four() == s.two.three.four()
    assert c.two.three.four() is s.two.three.four()
    assert c.two.three.four is not s.two.three.four


def test_mutable_objects():

    s = Sejings()

    s.one = 'one'
    s.two = 'two'
    s.one.one = ['one', 'one']
    s.one.two = ['one', 'two']
    s.two.three.four = ['two', 'three', 'four']

    c = copy(s)

    assert c is not s

    assert c.one() == s.one()
    assert c.one() is s.one()
    assert c.one is not s.one

    assert c.two.three.four() == s.two.three.four()
    assert c.two.three.four() is s.two.three.four()
    assert c.two.three.four is not s.two.three.four
