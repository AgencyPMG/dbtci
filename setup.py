#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION") as version_file:
    version = version_file.read().strip()

requires = ["click==7.0", "click-default-group==1.2.1", "dbt==0.16.0"]

dev_requires = [
    "black==19.10b0",
    "coverage==4.5.4",
    "pytest==4.3.1",
    "pytest-cov==2.6.1",
    "mock==4.0.2",
]

setup(
    name="dbtci",
    version="0.1.0",
    author="Jonathan Talmi",
    author_email="jtalmi@gmail.com",
    description="CI manager for dbt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtalmi/dbtci",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    py_modules=["dbtci"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # setup_requires=['pytest-runner'],
    tests_require=dev_requires,
    install_requires=requires,
    extras_require={"dev": dev_requires,},
    entry_points={"console_scripts": ["dbtci = dbtci.cli:main"]},
)
