# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
import copy

from sejings import Sejings, utils


def test_to_from_config_file(string_only_settings, test_ini_file_path):
    """
    natively configparser only supports strings. Therefore
    this is a pure test of the configparser capabilities.
    """
    utils.to_config_file(string_only_settings, test_ini_file_path)

    assert test_ini_file_path.is_file()

    result = copy.deepcopy(string_only_settings)

    utils.update_from_config_file(result, test_ini_file_path)

    assert result is not string_only_settings

    assert result.one() == string_only_settings.one()
    assert result.one() is not string_only_settings.one()  # strings are immutable.
    assert result.one is not string_only_settings.one

    assert result.two.three.four() == string_only_settings.two.three.four()
    assert result.two.three.four() is not string_only_settings.two.three.four()  # strings are immutable.
    assert result.two.three.four is not string_only_settings.two.three.four


def test_to_from_config_file_mutable_objects(settings, test_ini_file_path):
    """
    natively configparser only supports strings. Therefore
    this is a pure test of the configparser capabilities.
    """
    utils.to_config_file(settings, test_ini_file_path)

    assert test_ini_file_path.is_file()

    result = copy.deepcopy(settings)

    utils.update_from_config_file(result, test_ini_file_path)

    assert result is not settings

    assert result.one() == settings.one()
    assert result.one() is not settings.one()  # strings are immutable.
    assert result.one is not settings.one

    assert result.two.three.four() == settings.two.three.four()
    assert result.two.three.four() is not settings.two.three.four()  # strings are immutable.
    assert result.two.three.four is not settings.two.three.four

    assert result.types.list() == settings.types.list()
    assert result.types.list() is not settings.types.list()
    assert result.types.list is not settings.types.list
