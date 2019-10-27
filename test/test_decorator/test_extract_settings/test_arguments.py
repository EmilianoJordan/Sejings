# Created: 10/20/2019
# Author:  Emiliano Jordan,
# Project: settings

from sejings import extract_settings, settings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


########################################################################
# Testing a basic function call with only arguments.
########################################################################

@extract_settings()
def basic_function(a_one, a_two):
    return a_one, a_two


def test_basic_call():
    result = basic_function('a_one', 'a_two')

    proper_return = ('a_one', 'a_two')

    assert result == proper_return


def test_basic_call_with_settings():
    result = basic_function(s.three, 'a_two')

    proper_return = ('three', 'a_two')

    assert result == proper_return


########################################################################
# Testing a basic function call with only arguments with no paren
# decorator.
########################################################################

@extract_settings
def no_paren_basic_function(a_one, a_two):
    return a_one, a_two


def test_no_paren_basic_call():
    result = no_paren_basic_function('a_one', 'a_two')

    proper_return = ('a_one', 'a_two')

    assert result == proper_return


def test_no_paren_basic_call_with_settings():
    result = no_paren_basic_function(s.three, 'a_two')

    proper_return = ('three', 'a_two')

    assert result == proper_return
