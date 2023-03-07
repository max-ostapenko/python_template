# Python project template

This repository contains an opinionated version of a Python project template.
It's not a complete with all software engineering best practices, but provides a quick and easy start for medium level projects.

## Development

### Package management

[`pip`](https://pypi.org/project/pip/) - default package manager that comes with Python and does a great job managing packages for a single environment.

Use recommended packages to quickstart your project:

1. [`requirements_general.txt`](requirements_general.txt) - general Python development suggestions
2. [`requirements_google.txt`](requirements_google.txt) - Google services
3. [`requirements_data.txt`](requirements_data.txt) - data analysis or transformantions


### Utilities

[`Makefile`](https://www.gnu.org/software/make/manual/make.html) - a utility that helps to have shortcuts for various actions, e.g. building, linting, testing.

### Code review

[`black`](https://black.readthedocs.io/en/stable/) - the best Python formatting package that requires minimum manual effort to maintain uniformal code style.

[`flake8`](https://flake8.pycqa.org/en/latest/) - Python code style guide checks

### Testing

[`pytest`](https://docs.pytest.org/en/latest) - testing module that is simple and scalable to support most use cases.
