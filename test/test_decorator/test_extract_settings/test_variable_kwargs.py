# Created: 10/20/2019
# Author:  Emiliano Jordan,
# Project: settings

from typing import Any

from sejings import extract_settings, settings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


########################################################################
# An Arbitrary Keyword Argument Dictionary should not need another
# path in the if block. In fact this should all be taken care of without
# the getfullargspec call.
########################################################################

@extract_settings()
def vkwargs_function(a_one, a_two, kw_one: Any = s.one, kw_two: Any = s.two, kw_three='kw_three',
                     **kwargs):
    return a_one, a_two, kw_one, kw_two, kw_three, kwargs


def test_vkwargs():
    result = vkwargs_function('a_one',
                              'a_two',
                              kw_two=2,
                              vkwarg_one='test',
                              vkwarg_two=s.three.one)

    proper_return = (
        'a_one',
        'a_two',
        'kw_one',
        2,
        'kw_three',
        {
            'vkwarg_one': 'test',
            'vkwarg_two': 'three.one'
        }
    )

    assert proper_return == result


########################################################################
# Test no parenthesis decorator call.
########################################################################

@extract_settings
def no_paren_vkwargs_function(a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three', **kwargs):
    return a_one, a_two, kw_one, kw_two, kw_three, kwargs


def test_no_paren_vkwargs():
    result = no_paren_vkwargs_function('a_one',
                              'a_two',
                              kw_two=2,
                              vkwarg_one='test',
                              vkwarg_two=s.three.one)

    proper_return = (
        'a_one',
        'a_two',
        'kw_one',
        2,
        'kw_three',
        {
            'vkwarg_one': 'test',
            'vkwarg_two': 'three.one'
        }
    )

    assert proper_return == result
