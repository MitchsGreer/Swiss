[![Format](https://github.com/MitchsGreer/Swiss/actions/workflows/format.yaml/badge.svg)](https://github.com/MitchsGreer/Swiss/actions/workflows/format.yaml)[![Lint](https://github.com/MitchsGreer/Swiss/actions/workflows/lint.yaml/badge.svg)](https://github.com/MitchsGreer/Swiss/actions/workflows/lint.yaml)

# Swiss

This repository holds a swiss army knife of useful tools.

## Dependencies

This project depends on the python [uv](https://docs.astral.sh/uv/getting-started/installation/) tool and the following additional executables:

| Command | executables |
|:--|:--|
| clone | [git](https://github.com/git-guides/install-git) |
| docker | [docker](https://docs.docker.com/engine/install/) |
| format | `ruff` (python), `isort` (python) |
| hash | None |
| ie | None |
| import | None |
| lint | ruff |
| project | None |
| remove | None |
| space-find | None |
| swing | [git](https://github.com/git-guides/install-git) |

## Installation

The tool can be installed using uv.

```
uv tool install https://github.com/MitchsGreer/Swiss.git
```

To install the tool with additional python executables use:
```
uv tool install https://github.com/MitchsGreer/Swiss.git --with-executables-from ruff,isort
```

Python dependency executables can be installed with the above command, for others refer to their websites (they have been linked).

## Usage

After this script is installed it can be used to run a couple of useful commands.

```
#> swiss --help
usage: Command line swiss army knife.

positional arguments:
  {clone,docker,format,hash,ie,import,lint,project,remove,space-find,swing,version}
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
    swing               Does a 'git add .', 'git commit -m " "', 'git push origin <BRANCH>'.
    version             Display the version information for this tool.

options:
  -h, --help            show this help message and exit
```
