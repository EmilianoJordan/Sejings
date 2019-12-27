# Created: 10/20/2019
# Author:  Emiliano Jordan,
# Project: sejings

from sejings import extract_sejings, sejings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


########################################################################
# A function with an Arbitrary Argument List. This should be another
# path in the main if block in the decorator.
########################################################################

@extract_sejings()
def vargs_function(a_one, a_two, *args, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, args, kw_one, kw_two, kw_three


def test_no_varargs():
    result = vargs_function('a_one', 'a_two')

    proper_return = ('a_one', 'a_two', (), 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


def test_vargs():
    result = vargs_function('a_one', 'a_two', 'a_three', 'a_four')

    proper_return = ('a_one', 'a_two', ('a_three', 'a_four'), 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


def test_vargs_and_kwargs():
    result = vargs_function('a_one',
                            'a_two',
                            'a_three',
                            'a_four',
                            kw_two='passed_kw_two',
                            kw_one='passed_kw_one')

    proper_return = ('a_one',
                     'a_two',
                     ('a_three', 'a_four'),
                     'passed_kw_one',
                     'passed_kw_two',
                     'kw_three')

    assert result == proper_return


########################################################################
# A function with an Arbitrary Argument List with no paren decorator.
# This should be another path in the main if block in the decorator.
########################################################################

@extract_sejings
def no_paren_vargs_function(a_one, a_two, *args, kw_one=s.one, kw_two=s.two, kw_three='kw_three'):
    return a_one, a_two, args, kw_one, kw_two, kw_three


def test_no_paren_no_varargs():
    result = no_paren_vargs_function('a_one', 'a_two')

    proper_return = ('a_one', 'a_two', (), 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


def test_no_paren_vargs():
    result = no_paren_vargs_function('a_one', 'a_two', 'a_three', 'a_four')

    proper_return = ('a_one', 'a_two', ('a_three', 'a_four'), 'kw_one', 'kw_two', 'kw_three')

    assert result == proper_return


def test_no_paren_vargs_and_kwargs():
    result = no_paren_vargs_function('a_one',
                                     'a_two',
                                     'a_three',
                                     'a_four',
                                     kw_two='passed_kw_two',
                                     kw_one='passed_kw_one')

    proper_return = ('a_one',
                     'a_two',
                     ('a_three', 'a_four'),
                     'passed_kw_one',
                     'passed_kw_two',
                     'kw_three')

    assert result == proper_return
