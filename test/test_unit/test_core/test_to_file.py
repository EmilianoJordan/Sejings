# Created: 12/27/2019
# Author:  Emiliano Jordan,
# Project: sejings
import configparser
from pathlib import Path


def test_basic(settings, test_ini_file_path):

    assert isinstance(test_ini_file_path, Path)

    label = 'Settings'

    settings.to_file(test_ini_file_path, label=label)

    config = configparser.ConfigParser()

    config.read(test_ini_file_path)

    assert label in config

    assert test_ini_file_path.is_file()
