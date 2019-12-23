# Created: 10/26/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Settings


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
