# Fuzze

Fuzze is a fuzzing tool for Odoo's tours. It mutates a tour script to inject unexpected data into forms with the goal of finding bugs in the Odoo project. Some utilities are also provided to help with the process of creating tests cases that runs multiples mutated tours inside one test and tracing failures.

## Installation

To install the tool, the build script can be used. Run the following command to install the tool as a module in the current user's profile:

```pwsh
pwsh ./build.ps1
```

## Run the evaluation

To make mutants of a tour, several scripts are available in the `scripts` directory. Each script is a stub for the main flow tour using each strategy of the tool.

After the mutants are generated, simply run odoo using the config file `odoo_config.cfg` and add the argument `--test-tags fuzze` to run the tests.
