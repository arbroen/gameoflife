### Introduction

Came across this simple algorithm. Built my own google-less version for the 
sake of displaying some skills. 

Have fun. 

### Installation
Start by cloning this github repoitory. I won't pollute pypi for obvious 
reason. The next step is usually creating a `virtualenv` (or use the builtin
 `python -m venv`). 

This project uses [poetry] to install itself and its dependencies. It is 
an absolute improvement over the classic `setup.py && pip` approach. It is 
built by Sébastien Eustace and you can find the source [here][poetry-git].

Click on this [link][poetry-install] to see how to install poetry. After 
poetry installation run the following command to install the project itself.

```shell script
poetry install
```

Optionally, you can run a minimal package installation by running: 

```shell script
poetry install --no-dev
```

Assuming you created a virtual environment activate it and you can run the 
package directly:

```shell script
gol --help
```

To run a preset game of life scenario use the following command: 
```shell script
gol preset oscilator
```

If you for some reason omitted the creation of a `virtualenv` or forgot to 
activate it [poetry] will have created one for you. You can then run all the 
commands above by prepending `poetry run`. E.g. 

```shell script
poetry run gol --help
poetry run gol preset oscilator
```

### Testing
The suite comes fully tested. [Poetry] installs [tox] by default so you should
be ready to start testing. Simply run:

```shell script
tox
```

This runs multiple versions of python and a number of linting tools. If you 
however only want a single version run something like:

```shell script
tox -e py,linters
```

[poetry]: https://python-poetry.org/
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry-git]: https://github.com/python-poetry/poetry
[tox]: https://tox.readthedocs.io/en/latest/
