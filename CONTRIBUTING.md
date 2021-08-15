# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/omnisci/sqlalchemy-omnisci/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

SQLAlchemy OmniSci could always use more documentation, whether as part of the
official SQLAlchemy OmniSci docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/omnisci/sqlalchemy-omnisci/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

### Get Started!

Ready to contribute? Here's how to set up `sqlalchemy-omnisci` for local development.

1. Fork the `sqlalchemy-omnisci` repo on GitHub.
2. Clone your fork locally::
```sh
    $ git clone git@github.com:your_name_here/sqlalchemy-omnisci.git
```
1. Create a conda environment and set up your fork for local development::
```sh
    $ cd sqlalchemy-omnisci/
    $ conda env create --file environment.yaml
    $ conda activate sqla-omnisci
    $ make develop
```
4. Create a branch for local development::
```sh
    $ git checkout -b name-of-your-bugfix-or-feature
```
   Now you can make your changes locally.

5. Commit your changes and push your branch to GitHub (this runs pre-commit hooks automatically)::
```
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
```
6. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.


## Development

This sections aims to explain the structure of the project an how to
prepare your development environment locally.

Main of the useful commands are grouped at Makefile, so you can easily
run the make targets to prepare your environment and run tests.



## Tests

Tests were created using `pytest`. Additionally, `/tests/test_suite.py`
uses `sqlalchemy.testing.suite`, a convinient way to re-use the
`sqlalchemy` tests designed for any dialect. For more information
about that, check it out in its
[official documentation](https://github.com/sqlalchemy/sqlalchemy/blob/master/README.unittests.rst)

For the tests here, it is important to have **OmniSci** server running.
It will create a new database for tests called `sqla_testing`.

A common workflow for unit testing could be described as follows:

```sh
# in a terminal (let's call it terminal 1)
make docker-omnisci-start
```

```sh
# in anoter terminal (let's call it terminal 2)
make run-tests
```

If you are adding a new feature or changing an existent feature and
you want to create a new test file at `/tests/`, check how
`/tests/test_compiler.py` and `/tests/test_connection.py` implement
the tests.

**Tip: the class used for testing should inherit
`sqlalchemy.testing.fixtures.TestBase`!**


## Deploying

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.md).

Then run:

**TBD**
