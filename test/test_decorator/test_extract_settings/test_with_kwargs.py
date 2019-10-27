# Created: 10/20/2019
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

@extract_settings()
def basic_function_with_kwargs(a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, kw_one, kw_two, kw_three


def test_basic_call_with_kwargs():
    result = basic_function_with_kwargs('a_one', 'a_two', kw_three=s.three)

    proper_return = ('a_one', 'a_two', 'kw_one', 'kw_two', 'three')

    assert result == proper_return


def test_kwarg_as_positional_arg():
    result = basic_function_with_kwargs('a_one', 'a_two', 'a_three')

    desired = ('a_one', 'a_two', 'a_three', 'kw_two', 'kw_three')

    assert result == desired


########################################################################
# Testing a simple function with key word arguments and no paren
# decorator.
########################################################################

@extract_settings
def no_paren_function_with_kwargs(a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, kw_one, kw_two, kw_three


def test_no_paren_basic_call_with_kwargs():
    result = no_paren_function_with_kwargs('a_one', 'a_two', kw_three=s.three)

    proper_return = ('a_one', 'a_two', 'kw_one', 'kw_two', 'three')

    assert result == proper_return


def test_no_paren_kwarg_as_positional_arg():
    result = no_paren_function_with_kwargs('a_one', 'a_two', 'a_three')

    desired = ('a_one', 'a_two', 'a_three', 'kw_two', 'kw_three')

    assert result == desired
