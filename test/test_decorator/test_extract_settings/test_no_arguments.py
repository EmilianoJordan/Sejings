# Created: 10/20/2019
# Author:  Emiliano Jordan,
# Project: sejings

from sejings import extract_sejings, sejings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


@extract_sejings()
def function_no_args():
    return None


def test_no_arguments():
    assert function_no_args() is None


@extract_sejings
def no_parent_function_no_args():
    return None


def test_no_paren_no_arguments():
    assert no_parent_function_no_args() is None
