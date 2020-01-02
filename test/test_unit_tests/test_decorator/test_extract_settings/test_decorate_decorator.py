# Created: 10/20/2019
# Author:  Emiliano Jordan,
# Project: sejings

from functools import wraps, lru_cache

from sejings import extract_sejings, sejings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


########################################################################
# Need to make sure this works if there's a decorator between
# extract_sejings and the function. This shouldn't be a problem
# and the partial unwrapping should handle this just fine.
########################################################################

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


@extract_sejings()
@decorator
def double_dec_function(a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, kw_one, kw_two, kw_three


def test_double_dec_basic_call():
    result = double_dec_function('a_one', 'a_two')

    proper_return = ('a_one', 'a_two', 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


########################################################################
# If a function has a decorator with
# a different signature (think functools.lru_cache) then
# getfullargspec() returns the signature of the decorator
# not the function. But! in this case func is a partial and
# has a __wrapped__ attribute that we can use to extract
# the desired function.
#
# This should work just fine with the partial unwrapping taking place
# in the while statement.
########################################################################

@extract_sejings()
@lru_cache(maxsize=128)
def differing_signatures_functions(
        a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'
):
    return a_one, a_two, kw_one, kw_two, kw_three


def test():
    result = differing_signatures_functions('a_one', 'a_two')

    proper_return = ('a_one', 'a_two', 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


########################################################################
# No Parenthesis version of the appropriate tests.
########################################################################

@extract_sejings
@decorator
def no_paren_double_dec_function(a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, kw_one, kw_two, kw_three


def test_no_paren_double_dec_basic_call():
    result = no_paren_double_dec_function('a_one', 'a_two')

    proper_return = ('a_one', 'a_two', 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


@extract_sejings()
@lru_cache(maxsize=128)
def no_paren_differing_signatures_functions(
        a_one, a_two, kw_one=s.one, kw_two=s.two, kw_three='kw_three'
):
    return a_one, a_two, kw_one, kw_two, kw_three


def test_no_paren():
    result = no_paren_differing_signatures_functions('a_one', 'a_two')

    proper_return = ('a_one', 'a_two', 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return
