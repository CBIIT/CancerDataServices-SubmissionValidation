"""test noxlsx2json.helpers.json_schema_validator"""

import os
import pytest
import cds_template_tool
from cds_template_tool.validators.json_schema_validator import validate_json_with_schema


class TestJsonSchemaValidator(object):
    """Tests the noxlsx.helpers.jsonwriter class"""

    def test_json_validation_works_with_good_json(self):
        """
        class:      jsonschemavalidator
        function:   validate_json_with_schema
        desc:       tests that the function works with simple case
        """
        j = "tests/test_data/16355.json"
        s = "tests/test_data/schema.json"

        expected = True
        actual = validate_json_with_schema(j, s)
        assert expected == actual

    def test_json_validation_throws_error(self):
        """
        class:      jsonschemavalidator
        function:   validate_json_with_schema
        desc:       tests that the function works with simple case
        """
        j = "tests/test_data/16355.json"
        s = "tests/test_data/wrong_schema.json"

        expected = False
        actual = validate_json_with_schema(j, s)
        assert expected == actual
