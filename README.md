# Swiss

This repository holds a swiss army knife of useful tools.

## Dependencies

This project requires setuptools and the command line utility build for
building the script.

```
#> python3 -m pip install --upgrade setuptools
#> python3 -m pip install --upgrade build
```

This project also depends on Docker or git to be installed for full
functionality.

## Build

This module can be built into a distributable python package with PDM.

```
#> python3 -m build
```

## Installation

The package can be installed several ways.

Without the wheel in editable mode:

```
#> git clone https://github.com/MitchsGreer/swiss.git
#> python3 -m pip install -e Swiss/
```

After building the wheel:

```
#> pipx install dist/swiss-1.0.0-py3-none-any.whl
```

## Usage

After this script is installed it can be used to run a couple of useful commands.

```
#> swiss -h
```
