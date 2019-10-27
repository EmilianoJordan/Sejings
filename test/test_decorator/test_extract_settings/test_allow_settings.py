# Created: 10/25/2019
# Author:  Emiliano Jordan,
# Project: settings
from sejings import extract_settings, settings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


########################################################################
# Testing a simple function with key word arguments.
########################################################################

@extract_settings('a_one', 'kw_one')
def basic_function_with_kwargs(a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, kw_one, kw_two, kw_three


def test_basic_call_with_kwargs():
    result = basic_function_with_kwargs('a_one', 'a_two', kw_three=s.three)

    proper_return = ('a_one', 'a_two', s.one, 'kw_two', 'three')

    assert result == proper_return


def test_kwarg_as_positional_arg():
    result = basic_function_with_kwargs(s.one, 'a_two', 'a_three')

    desired = (s.one, 'a_two', 'a_three', 'kw_two', 'kw_three')

    assert result == desired
