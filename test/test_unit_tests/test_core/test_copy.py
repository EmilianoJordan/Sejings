# Created: 12/26/2019
# Author:  Emiliano Jordan,
# Project: sejings
from copy import copy

from sejings import Sejings


def test_initial(settings):

    c = copy(settings)

    assert c is not settings

    assert c.one() == settings.one()
    assert c.one() is settings.one()
    assert c.one is not settings.one

    assert c.two.three.four() == settings.two.three.four()
    assert c.two.three.four() is settings.two.three.four()
    assert c.two.three.four is not settings.two.three.four


def test_mutable_objects(settings):

    c = copy(settings)

    assert c is not settings

    assert c.one() == settings.one()
    assert c.one() is settings.one()
    assert c.one is not settings.one

    assert c.two.three.four() == settings.two.three.four()
    assert c.two.three.four() is settings.two.three.four()
    assert c.two.three.four is not settings.two.three.four
