=================
CDS Template Tool
=================


Tool for working with Cancer Data Service's (CDS) Metadata Template


* Free software: MIT license

=============================
cds_template_tool
=============================

Tool for working with CDS Metadata Manifest Templates.
Includes validation, and transformation/generation of JSON/tab-separated-values (tsv)
for loading into Bento CDS or indexing with DCF


DESC:
-------
`cds_template_tool` will validate submitted metadata manifests
Will also convert from XLSX to .json and .tsv formats


TESTING:
--------
Simple: ``pytest`` (Probably want to ``pip install -r requirements_dev.txt``)



OPTIONS:
--------
::

 -i input-file.xlsx             xlsx input file, REQUIRED
 -t [UAT|DEVINT|PRODMOCK|PROD]  which tier to use 
 -o output-file.json            also save additional json file besides data/s3 folder
 -c config-file.ini             config file for runtime settings, default="etc/config.ini"
 --schema schema.json           schema file for validating json, default="etc/aurora_json_schema.json"


USAGE:
------
Example production call
::
    >$ python -m cds_template_tool -i data/input/16464.xlsx

Example development use
::
    >$ python -m cds_template_tool -i data/mock/mock_uat/15419.xlsx

Example call, output to file, specify config, and tier (e.g. UAT, PROD)
::
    >$ python3 -m noxlsx2json \
           -i data/mock/mock_test/15419.xlsx \
           -o test3.json \
           -c etc/config.ini \
           -t DEVINT

Features
--------
* TODO


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
