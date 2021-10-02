# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/omnisci/sqlalchemy-omnisci/issues.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and
"help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement
it.

### Write Documentation

SQLAlchemy OmniSci could always use more documentation, whether as part
of the official **SQLAlchemy OmniSci** docs, in docstrings, or even on
the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/omnisci/sqlalchemy-omnisci/issues.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

### Get Started!

Ready to contribute? Here's how to set up `sqlalchemy-omnisci` for local
development.

1.  Fork the `sqlalchemy-omnisci` repo on GitHub.
2.  Clone your fork locally::

    ```bash
        $ git clone git@github.com:your_name_here/sqlalchemy-omnisci.git
    ```

3.  Create a conda environment and set up your fork for local
    development::

    ```bash
        $ cd sqlalchemy-omnisci/
        $ conda env create --file environment.yaml
        $ conda activate sqla-omnisci
        $ make develop
    ```

4.  Create a branch for local development::

    ```bash
        $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

5.  Commit your changes and push your branch to GitHub (this runs
    pre-commit hooks automatically):
    ```bash
        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature
    ```

6.  Submit a pull request through the GitHub website.


## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.md.

## Development

This section aims to explain the structure of the project an how to
prepare your development environment locally.

### Structure for the project

The basic structure of the project follows the specification provided by
**SQLAlchemy**. You can check the specification out in the [official
documentation](https://github.com/sqlalchemy/sqlalchemy/blob/master/README.dialects.rst).

Additionally, there are some folders and files that help the development
process, which are:

-   `/docker/`, that includes the files and scripts used for tests and
    CI.
-   `/environment.yaml`, a conda environment file used to create the
    environment for development.
-   `/.pre-commit-config.yaml`, that is used for the installation of
    `git` pre-commit hooks.
-   `/Makefile`, that groups main useful commands for development, for
    example, **docker-compose** commands and tests.

This is not an exhaustive list of useful files for development, instead,
it mentions some files that you should keep in mind that can help you
here.

### Tests

Tests were created using `pytest`. One specific test,
`/tests/,test_suite.py` uses `sqlalchemy.testing.suite`, a convinient
way to re-use the `sqlalchemy` tests designed for any dialect. For more
information about that, check it out in its [official
documentation](https://github.com/sqlalchemy/sqlalchemy/blob/master/README.unittests.rst)

For the tests here, it is important to have **OmniSci** server running.
It will create a new database for tests called `sqla_testing`.

A common workflow for unit testing could be described as follows:

```bash
# in a terminal (let's call it terminal 1)
make docker-omnisci-start
```

```bash
# in anoter terminal (let's call it terminal 2)
make run-tests
```

If you are adding a new feature or changing an existent feature and you
want to create a new test file at `/tests/`, check how
`/tests/test_compiler.py` and `/tests/test_connection.py` implement the
tests.

**Tip: the class used for testing should inherit
`sqlalchemy.testing.fixtures.TestBase`!**

### Apache Superset connector

Additionally, this repository provides a connector module for
**OmniSci** on **Apache Superset**, available at
`/docker/superset-omnisci.py`.

If you are doing the process manually, copy
`/docker/superset-omnisci.py` into the engine folder inside the **Apache
Superset** directory (e.g. `superset/db_engine_specs/`) and rename it to
`omnisci.py`. For more information, check `/docker/setup-superset.sh`
out to see the steps used to prepare the **Apache Superset** with the
**OmniSci** connector for tests on docker.

If you want to use the docker container provided here, run:

```bash
$ make docker-superset-start
```

This command should build the image for the container and will prepare
everything needed to run the **Apache Superset** with the **OmniSci**
connector.

To try it, open your web browser and enter the following **URL**:
`localhost:8080`.

**NOTE**: Due dependencies conflict with **apache-arrow**, the **Apache
Superset** version recommended is `1.1.0`.

To connect the **Apache Superset** instance to your **OmniSci** server,
assuming you are running both using their respective `make` targets
(`make docker-superset-start` and `make docker-omnisci-start`), do:

-   click on `Data/Databases` menu.
-   in the **Databases** page, click on the `+ DATABASE` button.
-   in the **Add database** popup window, add a new database with the
    following **URI**:
    `omnisci://admin:HyperInteractive@omniscidb:6274/omnisci?protocol=binary`.

For debugging purpose, you can connect to the **Apache Superset**
container using:

```bash
$ make docker-superset-bash
```

If you need another instance of **Apache Superset** for
testing/debugging purpose, run:

´´´sh flask run -p 5000 --with-threads --reload --debugger
--host=0.0.0.0 ´´´

To try it, open your web browser and enter the following **URL**:
`localhost:5000`

Use the port 5000 because it is already exposed by **docker-compose**.

**NOTE:** **Apache Superset** listening on port 8080 doens't work right
now but if you run it using the command above it should work. The
problem is being investigated.

## Releasing

The releasing is based on the GitHub release. So, all you need to do is to
create a new release and the CI will be responsible for publishing the
package on PyPi. When the package is release on PyPi, the conda-forge
bot will be triggered and a new package will be release on conda-forge
as well.
