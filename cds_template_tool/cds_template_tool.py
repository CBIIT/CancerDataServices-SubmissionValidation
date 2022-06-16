#!/usr/bin/env python
"""Main module."""
"""
DESC:
    code to test CDS metadata Template

USAGE:
    # Example production call, (output to standrd location in data/s3):
    >$ python3 -m cds_template_tool -i data/input/16464.xlsx
"""
import sys
import argparse
from .helpers.settings import Settings
from .helpers.logger import get_logger
from .helpers.metadata_manifest_reader import read_metadata_manifest


def cli():
    """ return args parsed from command line """
    args = None

    parser = argparse.ArgumentParser(
        description="reads and checks CDS metadata templates (xlsx-formatted)"
    )
    parser.add_argument(
        "-i", metavar="input-file.xlsx", type=str, help="xlsx input file", required=True
    )
    parser.add_argument(
        "-c",
        metavar="config-file.ini",
        type=str,
        help="config file for runtime settings",
        default="etc/config.ini",
    )
    parser.add_argument(
        "--schema",
        dest="schema",
        metavar="aurora_json_schema.json",
        type=str,
        help="schema file for validating json files",
        default="etc/aurora_json_schema.json",
    )
    parser.add_argument(
        "-t",
        choices=["UAT", "DEV", "PRODMOCK", "PROD"],
        help="which tier to use and which s3 bucket for sync",
        default="DEV",
    )

    try:
        args = parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))

    # needed to properly set default logging level
    Settings.setup(args.c, args.schema, args.t)  # noqa

    logger = get_logger(__name__)
    logger.info("Starting cds_template_tool.py CLI with the arguments")
    logger.info(args)

    return args

def check_metadata_manifest(args):
    """ primary function """

    logger = get_logger(__name__)
    logger.info("Starting cds_template_file")

    # Getting down to business! Acutal work! get the data, then write the data

    ## types, results = get_data(args.i)
    stuff = read_metadata_manifest(args.i)

    # types, results -- types holds 'types' of variants, for ease of referencing
    #                -- results is nested data structure holding parsed xlsx variants
    # args.i         -- infile, = the input file (needed for coming up with name of output
    # args.o         -- outfile=None, this is if extra output is wanted

    ## new_json = write_data(types, results, args.i, args.o, args.screen)

    # validate newly generated json against schema (args.schema)
    ## json_is_valid = validate_json_with_schema(new_json, args.schema)


def main():
    # get arguments
    args = cli()

    # do the transform from xlsx to json
    check_metadata_manifest(args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
