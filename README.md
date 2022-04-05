# ot-harjoitustyo
This repository hosts my project for the software technology course - a simple platformer game written in python with pygame. 

## Documentation
- [Requirements specification](./documentation/requirements-specification.md)
- [Timesheet](./documentation/timesheet.md)
- [Changelog](./documentation/changelog.md)

## Setup
This project uses poetry for managing dependencies.
1. Install dependencies:
```console
poetry install 
```
## Available CLI commands
### Running the program
Run the program with:
```console
poetry run invoke start
```
### Testing
Tests can be run with:
```console
poetry run invoke test
```
A report of test coverage can be generated with:
```console
poetry run invoke coverage-report
```
The report can be found in the *htmlcov* directory.
