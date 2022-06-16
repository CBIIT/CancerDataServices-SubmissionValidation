"""test cds_template_tool.helpers.settings"""

import pytest
from _pytest.monkeypatch import MonkeyPatch
from cds_template_tool.helpers.settings import Settings


class TestSettings(object):
    """test cds_template_tool.helpers.settings"""

    @classmethod
    def setup_class(cls):
        cls.monkeypatch = MonkeyPatch()


    def test_dev_settings(self):
        c = "tests/test_data/config.ini"
        s = "tests/test_data/schema.json"
        t = "DEV"
        Settings.setup(c, s, t)
        assert Settings.LOGGING_LEVEL == "DEBUG"
        assert Settings.TIER == "DEV"

    def test_uat_settings(self):
        c = "tests/test_data/config.ini"
        s = "tests/test_data/schema.json"
        t = "UAT"
        Settings.setup(c, s, t)
        assert Settings.LOGGING_LEVEL == "DEBUG"
        assert Settings.TIER == "UAT"

    def test_prod_settings(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass
