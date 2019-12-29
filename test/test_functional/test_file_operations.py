# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
from sejings import Sejings, utils


def test_to_from_config_file(string_only_settings, test_ini_file_path):
    utils.to_config_file(string_only_settings, test_ini_file_path)

    assert test_ini_file_path.is_file()

    result = utils.from_config_file(test_ini_file_path)

    assert result is not string_only_settings

    assert result.one() == string_only_settings.one()
    assert result.one() is not string_only_settings.one()  # strings are immutable.
    assert result.one is not string_only_settings.one

    assert result.two.three.four() == string_only_settings.two.three.four()
    assert result.two.three.four() is not string_only_settings.two.three.four()  # strings are immutable.
    assert result.two.three.four is not string_only_settings.two.three.four
