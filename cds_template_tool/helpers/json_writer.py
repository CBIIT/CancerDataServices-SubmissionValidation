"""
write data to json file
 * write_data( ... ) calls create_json_filename
"""

import os
from .settings import Settings
from .logger import get_logger
from cds_template_tool.models.metadata_json import metadata_json

logger = get_logger(__name__)
settings = (
    Settings()
)  # this is to import all parameters for settings for calling varsap!

