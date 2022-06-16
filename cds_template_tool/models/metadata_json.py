import copy
import os
import json
from collections import OrderedDict
from datetime import datetime


"""
DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER
"""

class Metadata_json:
    def __init__(self, pat):
        now = datetime.now()
        currenttime = now.strftime("%m/%d/%Y, %H:%M:%S")

        self.thingy = OrderedDict(
            [
                ("sample_info", pat.data),
                ("submitted_variants", []),
                (
                    "submission_processing",
                    OrderedDict(
                        [
                            ("submitted_filename", ""),
                            ("generated_filename", ""),
                            ("generated_path_filename", ""),
                            ("submission_timestamp", currenttime),
                            ("processing_software_version", "v0.01"),
                            ("processed_date", ""),
                        ]
                    ),
                ),  # end_submission_processing
                ("errors", {}),
                ("warnings", {}),
                (
                    "debug",
                    OrderedDict(
                        [
                            ("dev_version", "0.01"),
                            ("dev_date", None),
                            ("processing_software", ""),
                        ]
                    ),
                ),  # end-debug
            ]
        )  # end-thingy

    def ordered_rename(self, old_dict, old_name, new_name):
        new_dict = OrderedDict()
        for key, _v in zip(old_dict.keys(), old_dict.values()):
            new_key = key if key != old_name else new_name
            new_dict[new_key] = old_dict[key]
        return new_dict

    # def ordered_rename(self, old_dict,old_name,new_name):
    #    new_dict = OrderedDict()
    #    for key,value in zip(old_dict.keys(),old_dict.values()):
    #        new_key = key if key != old_name else new_name
    #        new_dict[new_key] = old_dict[key]
    #    return new_dict

    def add_snv_variant(self, snv):

        # make deep-ish copy, so can leave original piece of data alone, but rename a field
        # temp = self.ordered_rename(snv.data, "protein_hgvs", "protein")
        temp = copy.deepcopy(snv.data)

        # contatenate protein fields, and then remove protein-np field
        # temp["protein"] = snv.data["protein_np"] + ":" + snv.data["protein_hgvs"]
        #
        # now remove the protein-np field
        # temp.pop("protein_np", None)

        # now add this temp data to the json structure
        self.thingy["submitted_variants"].append(temp)

    # TODO: consider moving to Cnv?
    def add_cnv_variant(self, cnv):

        # make deep copy, but leave original piece of data alone
        temp = copy.deepcopy(cnv.data)

        # if copy-number is above threshold value, then classify as 'amplification'
        # note data in structure is wrapped as str
        if float(temp["copy_number"]) > 7:
            temp["oncominevariantclass"] = "amplification"
        elif float(temp["copy_number"]) < 0.1:
            temp["oncominevariantclass"] = "deletrious"
        else:
            temp["oncominevariantclass"] = None

        # now add this temp data to the json structure
        self.thingy["submitted_variants"].append(temp)

    def add_fusion_variant(self, fusion):
        self.thingy["submitted_variants"].append(fusion.data)

    def dump_to_screen(self):
        print(json.dumps(self.thingy, indent=2, sort_keys=False))

    def save_to_file(self, file):
        self.add_processing_outfile_info(file)
        with open(file, "w") as fh:
            json.dump(self.thingy, fh, indent=None, sort_keys=False)

    def add_processing_infile_info(self, infile):
        self.thingy["submission_processing"]["submitted_filename"] = infile

    def add_processing_outfile_info(self, outfile):
        _filename = os.path.split(outfile)
        self.thingy["submission_processing"]["generated_filename"] = _filename[1]
        self.thingy["submission_processing"]["generated_path_filename"] = outfile


"""
{
example here
}
"""
