# ot-harjoitustyo
This repository hosts my project for the software technology course - a simple platformer game written in python with pygame.

## Releases
- [Week 5](https://github.com/eemilhaa/ot-harjoitustyo/releases/tag/Week5)
- [Week 6](https://github.com/eemilhaa/ot-harjoitustyo/releases/tag/Week6)

## Documentation
- [User manual](./documentation/user-manual.md)
- [Requirements specification](./documentation/requirements-specification.md)
- [Architecture description](./documentation/architecture.md)
- [Test documentation](./documentation/test-documentation.md)
- [Timesheet](./documentation/timesheet.md)
- [Changelog](./documentation/changelog.md)

## Setup
This project uses poetry for managing dependencies.
Install dependencies:
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

### Linting
Code linting with pylint can be done with:
```console
poetry run invoke lint
```

### Formatting
You can format the code using autopep8 with:
```console
poetry run invoke format
```
