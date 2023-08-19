# Trode Config Generator

[![CI](https://github.com/zoldello/trode_config_generator/workflows/CI/badge.svg)](https://github.com/zoldello/trode_config_generator/actions)
[![Documentation Status](https://readthedocs.org/projects/trode_config_generator/badge/?version=latest)](https://trode_config_generator.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/trode_config_generator)](https://pypi.org/project/trode_config_generator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/trode_config_generator)](https://pypi.org/project/trode_config_generator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Trodes config generator

- Documentation: https://trode-config-generator.readthedocs.io

## Installation

Install the latest version from PyPI:

```
pip install trode_config_generator
```
## Development setup

After cloning the repository, you can easily install the development environment and tools
([black](https://github.com/psf/black), [pylint](https://www.pylint.org), [mypy](http://mypy-lang.org), [pytest](https://pytest.org), [tox](https://tox.readthedocs.io))
with:

```
git clone https://github.com/zoldello/trode_config_generator.git
cd trode_config_generator
pip install -e .[dev]
```

And run the checks & tests with tox:

```
tox
```

The documentation is built with [sphinx](https://www.sphinx-doc.org):

```
cd docs

# Windows
.\make.bat clean
.\make.bat html

# Linux
make clean html
```
