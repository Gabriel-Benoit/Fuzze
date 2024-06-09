from setuptools import find_packages, setup

setup(
    name="fuzze",
    packages=find_packages(),
    version="0.1.0",
    description="""Fuzze is a fuzzing tool for Odoo's tour scripts. 
    It mutates a tour script to inject unexpected data into forms with the goal of finding bugs in the Odoo project.
    Some utilities are also provided to help with the process of creating tests cases that runs multiples mutated tours inside one test and tracing failures.""",
    author="Gabriel Benoit",
    install_requires=[
        "antlr4-python3-runtime==4.9.3",
        "antlr4-tools",
        "jsbeautifier",
        "simple_parsing",
    ],
)
