# -*- coding: utf-8 -*-

"""Errors for Validating,Testing xlsx spreadsheets to json."""


class ValidateError(Exception):
    """ Basic Class for other exceptions """

    def __init__(self, value):
        self.value = value

    # __str__ to print() the value
    def __str__(self):
        return repr(self.value)


class XlsxWorksheetError(ValidateError):
    """ Raised when the expected sheets aren't right """

    def __init__(self, value):
        self.msg = f"XlsxWorksheetError: {value}"

    # __str__ to print() the value
    def __str__(self):
        return self.msg


class MissingDataError(ValidateError):
    """ Raised if there is missing data in worksheet """

    def __init__(self, value):
        self.msg = repr(
            "MissingDataError: The field {} is missing required data".format(value)
        )

    # __str__ to print() the value
    def __str__(self):
        return self.msg


class SchemaError(Exception):
    """ Basic Class for handling jsonschmea exceptions """

    def __init__(self, msg):
        self.msg = f"SchemaError: {msg}"

    # __str__ to print() the value
    def __str__(self):
        return self.msg
