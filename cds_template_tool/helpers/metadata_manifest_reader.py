"""
Read and parse submitted xlsx files for CDS Metadata Manifest (high level entry point)
uses openpyxl
"""
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from openpyxl import load_workbook                             # noqa: E402
from cds_template_tool.helpers.logger import get_logger              # noqa: E402
from cds_template_tool.helpers.xlsx_parser import get_subfiles, get_participants, get_samples, get_f_p_s_mapping, get_genomic_infos, get_thingy


logger = get_logger(__name__)

def read_metadata_manifest(filename):
    """main entry point simple function to read template file"""

    """for now will just use xlsx_parser (until other formats are supported)"""
    """for now, just start with subfiles (submission files)"""

    # this is a starting point for iterating through all worksheets in the metadata manifest
    # get_thingy(filename)

    subfiles = get_subfiles(filename)
    #subfiles_size = len(subfiles)
    #logger.info(f'got {subfiles_size} files')

    participants = get_participants(filename)
    samples = get_samples(filename)
    mappings = get_f_p_s_mapping(filename)
    genomic_infos = get_genomic_infos(filename)

    return 'hello world'




