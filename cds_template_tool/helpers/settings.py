"""
App configuration
"""

import os
from configparser import ConfigParser


class Settings:
    """Set configuration from config file and env"""

    # logging - please note double quotes are needed for value here!
    # possible values = NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
    LOGGING_LEVEL = "DEBUG"  # noqa

    TIER = ""

    JSON_SCHEMA = ""  # file for validating generated JSON

    @classmethod
    def setup(cls, config_file, json_schema_file, tier):
        cls.config_file = config_file
        cls.JSON_SCHEMA = json_schema_file
        cls.TIER = tier

        # get parameters from config file
        # note - had to make sure to strip double quotes from beginning and
        #        end of strings, otherwise calling varsap would choke on them
        config = ConfigParser()
        config.read(cls.config_file)  # noqa

        # get logging level
        Settings.LOGGING_LEVEL = config.get("logging", "level").strip('"')

