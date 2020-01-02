# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Sejings, utils


def test_basic():
    input_dict = {
        'one': 'one',
        'one.one': ['one', 'one'],
        'one.two': ['one', 'two'],
        'two': 'two',
        'two.three.four': ['two', 'three', 'four']
    }

    c = Sejings(name='c')
    utils.update_from_dict(c, input_dict)

    assert input_dict['one'] == c.one()
    assert input_dict['two'] == c.two()

    assert input_dict['one.one'] == c.one.one()
    assert input_dict['one.one'] is not c.one.one()

    assert input_dict['one.two'] == c.one.two()
    assert input_dict['one.two'] is not c.one.two()

    assert input_dict['two.three.four'] == c.two.three.four()
    assert input_dict['two.three.four'] is not c.two.three.four()
