#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Mark Benson",
    author_email='bensonml@nih.gov',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Tool for working with Cancer Data Service's (CDS) Metadata Template",
    entry_points={
        'console_scripts': [
            'cds_template_tool=cds_template_tool.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cds_template_tool',
    name='cds_template_tool',
    packages=find_packages(include=['cds_template_tool', 'cds_template_tool.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bensonml/cds_template_tool',
    version='0.1.0',
    zip_safe=False,
)
