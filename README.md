[![Format](https://github.com/MitchsGreer/Swiss/actions/workflows/format.yaml/badge.svg)](https://github.com/MitchsGreer/Swiss/actions/workflows/format.yaml)[![Lint](https://github.com/MitchsGreer/Swiss/actions/workflows/lint.yaml/badge.svg)](https://github.com/MitchsGreer/Swiss/actions/workflows/lint.yaml)

# Swiss

This repository holds a swiss army knife of useful tools.

## Dependencies

This project depends on Docker and git to be installed for full functionality, but can be used without them.

## Installation

This tool depends on `uv`. The tool can be installed after cloning it down.

```
#> git clone https://github.com/MitchsGreer/Swiss.git
#> uv tool install Swiss
```

## Usage

After this script is installed it can be used to run a couple of useful commands.

```
#>swiss --help
usage: Command line swiss army knife.

positional arguments:
  {clone,docker,format,hash,ie,import,lint,project,remove,space-find,swing}
    clone               Clones down the given repository, if a directory is given, it checks out that branch.
    docker              Run docker commands for ease of use.
    format              Format the given source directory.
    hash                Hash the files in the given directory.
    ie                  Install a python package in the virtual environment as editable, don't install anything if we are not in one.
    import              Install a python package in the virtual environment, don't install anything if we are not in one.
    lint                Lint the given source directories.
    project             Run project commands for ease of use.
    remove              Remove the given python modules from the environment.
    space-find          Find the files with spaces in the given directory.
    swing               Does a `git add .`, `git commit -m `, 'git push origin <BRANCH>'

options:
  -h, --help            show this help message and exit
```
