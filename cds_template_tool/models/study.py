import sys
from collections import OrderedDict
from cds_template_tool.helpers.logger import get_logger
from cds_template_tool.models.errors import MissingDataError

logger = get_logger(__name__)

field = OrderedDict(
    [
        ('phs_accession','phs_accession'),
        ('study_name','study_name'),
        ('study_description','study_description'),
        ('primary_investigator_name','primary_investigator_name'),
        ('primary_investigator_email','primary_investigator_email'),
        ('co_primary_investigator_name','co_primary_investigator_name'),
        ('co_primary_investigator_email','co_primary_investigator_email'),
        ('cds_primary_bucket','cds_primary_bucket'),
        ('cds_secondary_bucket','cds_secondary_bucket'),
        ('cds_tertiary_bucket','cds_tertiary_bucket'),
        ('bioproject_accession','bioproject_accession'),
        ('funding_agency','funding_agency'),
        ('funding_source_program_name','funding_source_program_name'),
        ('grant_id','grant_id'),
        ('clinical_trial_system','clinical_trial_system'),
        ('clinical_trial_identifier','clinical_trial_identifier'),
        ('clinical_trial_arm','clinical_trial_arm'),
        ('organism_species','organism_species'),
        ('adult_or_childhood_study','adult_or_childhood_study'),
        ('number_of_participant','number_of_participant'),
        ('number_of_samples','number_of_samples'),
        ('study_data_types','study_data_types'),
        ('experimental_strategy_and_data_subtype','experimental_strategy_and_data_subtype'),
        ('acl','acl'),
        ('file_types_and_format','file_types_and_format'),
        ('size_of_data_being_uploaded','size_of_data_being_uploaded'),
    ]
)

max_row = len(field)
required_input_fields = ["phs_accession", "study_name", 'acl']

class Study:
    def __init__(self, assignments):
        # make a copy of fields, but remove 'header' label, prep for data
        self.headers = list(field.values())
        self.data = OrderedDict((k, None) for k in field.keys())
        self.type = "Study"

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
        return "Study()"

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
