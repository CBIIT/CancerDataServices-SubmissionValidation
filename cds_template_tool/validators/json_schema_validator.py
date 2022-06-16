"""
check that the json output is valid using the schema
"""

import json
import jsonschema
from cds_template_tool.helpers.settings import Settings
from cds_template_tool.helpers.logger import get_logger


logger = get_logger(__name__)


def validate_json_with_schema(newjsonfile, json_schema_file):
    """ validate that the generated JSON file against the schema """

    with open(json_schema_file) as _schema:
        s = json.load(_schema)

    with open(newjsonfile) as _json:
        j = json.load(_json)

    try:
        jsonschema.validate(instance=j, schema=s)
    except jsonschema.exceptions.ValidationError as ex:
        logger.info('Nelson says, "HAHA YOU FAILED JSON VALIDATION!"')
        logger.info(ex.message)
        logger.info("new json has:")
        logger.info(ex.absolute_path)
        logger.info("and you were supposed to have")
        logger.info(ex.absolute_schema_path)
        return False

    logger.info("new json passes validation")

    return True
