# Contributing

Based on [Zoomus'](https://github.com/prschmid/zoomus) contributing code.

## Dev Environment

In order to avoid interference with global packages and present an environment 
that's easy to reproduce, please create a virtual environment. It can be created 
using the commands below:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-tests.txt
```

## Branching

In order to add features or features, utilize 
[git flow](https://github.com/nvie/gitflow). That way, everything will get
confined to a development branch and not the master one. After that, just
create a PR.

## Running the Tests

Tests should be run using [tox](https://pypi.python.org/pypi/tox), so that we
can ensure they are run the same way, in a similar isolated environment, every
time. Running this is as simple as one single command:

```sh
tox
```

Assuming all goes well, you should see a result akin to

```sh
  py38: commands succeeded
  py39: commands succeeded
  congratulations :)
```

### Multiple Python Versions

It is highly recommended, although not absolutely necessary, that you run the tests
against all of our configured Python versions. This will help ensure that no
unexpected errors come up in our CI process which might delay your changes from
being merged.

These versions are currently:

* 3.8
* 3.9

For an easy way to install and manage all of the Python versions, you may want
to look at using [pyenv](https://github.com/pyenv/pyenv).

