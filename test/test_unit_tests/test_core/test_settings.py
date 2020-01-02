# Created: 10/26/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Sejings


def test_initial(settings):

    assert settings.one() == 'one'
    assert settings.two() == 'two'

    settings.one = 'uno'
    settings.two = 'dos'

    assert settings.one() == 'uno'
    assert settings.two() == 'dos'
