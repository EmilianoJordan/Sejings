# Created: 10/20/2019
# Author:  Emiliano Jordan,
# Project: settings

from sejings import extract_settings, settings as s

s.one = 'kw_one'
s.two = 'kw_two'
s.three = 'three'
s.three.one = 'three.one'


@extract_settings()
def function_no_args():
    return None


def test_no_arguments():
    assert function_no_args() is None


@extract_settings
def no_parent_function_no_args():
    return None


def test_no_paren_no_arguments():
    assert no_parent_function_no_args() is None
