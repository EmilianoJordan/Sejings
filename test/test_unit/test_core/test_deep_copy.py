# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
from copy import deepcopy


def test_immutable(settings):
    c = deepcopy(settings)

    assert c is not settings

    assert c.one() == settings.one()
    assert c.one() is settings.one()  # strings are immutable.
    assert c.one is not settings.one

    assert c.two.three.four() == settings.two.three.four()
    assert c.two.three.four() is settings.two.three.four()  # strings are immutable.
    assert c.two.three.four is not settings.two.three.four



def test_mutable_objects(settings):
    c = deepcopy(settings)

    assert c is not settings

    assert c.types.list() == settings.types.list()
    assert c.types.list() is not settings.types.list()
    assert c.types.list is not settings.types.list

    assert c.types.dict() == settings.types.dict()
    assert c.types.dict() is not settings.types.dict()
    assert c.types.dict is not settings.types.dict

    assert c.path() == settings.path()
    assert c.path() is not settings.path()
    assert c.path is not settings.path
