import sys
from collections import OrderedDict
from cds_template_tool.helpers.logger import get_logger
from cds_template_tool.models.errors import MissingDataError

logger = get_logger(__name__)

field = OrderedDict(
    [
        ('library_id','library_id'),
        ('library_strategy','library_strategy'),
        ('library_source','library_source'),
        ('library_selection','library_selection'),
        ('library_layout','library_layout'),
        ("platform", "platform"),
        ("instrument_model", "instrument_model"),
        ("design_description", "design_description"),
        ("reference_genome_assembly","reference_genome_assembly"),
    ]
)

"""used for parsing excel (ugh, wrong place, I know)"""
max_col = len(field)
required_input_fields = []

class Genomic_info:
    def __init__(self, assignments):
        # make a copy of fields, but remove 'header' label, prep for data
        self.headers = list(field.values())
        self.data = OrderedDict((k, None) for k in field.keys())
        self.type = "Genomic_info"

        # now put assignments into self.data (thank you OrderedDict!)
        for i, k in enumerate(self.data):
            self.data[k] = assignments[i]

        # TODO: move to validator, base class
        # TODO: systemize exit codes, put into config.ini
        # VALIDATION - ensure specified/required fields are populated
        # FAIL with exit status 200
        try:
            self.validate_all_required_fields_are_present()
        except MissingDataError as err:
            logger.error(f"When creating a {self.__repr__()} there was a missing field error")
            logger.error(err)
            logger.error(f'with the following data:')
            logger.error(self.data)
            sys.exit(200)

    def __repr__(self):
        return "Genomic_info()"

    def __str__(self):
        """as alternative to showing id, use self.data.items() """
        _id = list(self.data.values())[0]
        return f"member of {self.__repr__()} with id {_id}"

    def printme(self):
        for k, v in self.data.items():
            print("...{} has ordered dict {} ---> {} ".format(self.type, k, v))

    # TODO: move to validator, base class
    def validate_all_required_fields_are_present(self):
        """
        DESC:   raises MissingDataError if one of the required fields is missing from self.data
        """
        for reqd_field in required_input_fields:
            # check that field isn't None/empty or just whitespace
            # I'm converting field to string incase input is number/int before stripping all /w
            if (self.data[reqd_field] is None) or (
                not str(self.data[reqd_field]).strip()
            ):
                raise MissingDataError(reqd_field)
