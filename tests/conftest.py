"""Pytest configuration module."""
import copy
import os
import uuid
import warnings

import pytest
import sqlalchemy
from sqlalchemy import (
    BigInteger,
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    SmallInteger,
    String,
    create_engine,
    testing,
)
from sqlalchemy.sql import column, table

from sqlalchemy_omnisci import URL

URI_TEMPLATE = (
    "omnisci://{user}:{password}@{database}:{port}/{database}"
    "?protocol={protocol}"
)

DATABASE_TESTING = "sqla_testing"

DEFAULT_PARAMETERS = {
    "user": "admin",
    "password": "HyperInteractive",
    "database": DATABASE_TESTING,
    "protocol": "binary",
    "host": "localhost",
    "port": "6274",
}

SETUP_PARAMETERS = {
    "user": "admin",
    "password": "HyperInteractive",
    "database": "omnisci",
    "protocol": "binary",
    "host": "localhost",
    "port": "6274",
}

METIS_PARAMETERS = {
    "user": "demouser",
    "password": "HyperInteractive",
    "database": "mapd",
    "protocol": "https",
    "host": "metis.mapd.com",
    "port": "443",
}


def get_db_parameters(db_params=DEFAULT_PARAMETERS):
    """Set the db connection parameters."""
    ret = copy.copy(db_params)

    # a unique table name
    ret["name"] = ("sqlalchemy_tests_" + str(uuid.uuid4())).replace("-", "_")

    return ret


def get_engine(user=None, password=None, db_params=DEFAULT_PARAMETERS):
    """Create a connection using the given parameters."""
    ret = get_db_parameters(db_params)

    if user is not None:
        ret["user"] = user
    if password is not None:
        ret["password"] = password

    from sqlalchemy.pool import NullPool

    uri = URL(
        user=ret["user"],
        password=ret["password"],
        host=ret["host"],
        port=ret["port"],
        database=ret["database"],
        protocol=ret["protocol"],
    )

    engine = create_engine(uri, poolclass=NullPool)
    return engine, ret


@pytest.fixture(autouse=True, scope="session")
def uri_metis():
    """Return a URI for metis server."""
    return URI_TEMPLATE.format(**METIS_PARAMETERS)


@pytest.fixture(autouse=True, scope="session")
def uri_local():
    """Return a URI for local server."""
    return URI_TEMPLATE.format(**DEFAULT_PARAMETERS)


@pytest.fixture(autouse=True)
def table_datatype():
    """Create a table expression for handle different datatypes."""
    return table(
        "table_datatype",
        column("_bigint", BigInteger),
        column("_bool", Boolean),
        column("_date", Date),
        column("_datetime", DateTime),
        column("_float", Float),
        column("_int", Integer),
        column("_smallint", SmallInteger),
        column("_string", String),
    )


@pytest.fixture(autouse=True)
def table1():
    """Create a table expression for table1."""
    return table(
        "table1",
        column("id", Integer),
        column("name", String),
        column("value", Integer),
    )


@pytest.fixture(autouse=True)
def table2():
    """Create a table expression for table2."""
    return table(
        "table2",
        column("id", Integer),
        column("name", String),
        column("value", Integer),
    )


@pytest.fixture()
def engine_testaccount(request):
    """Create an engine for tests."""
    engine, _ = get_engine()
    engine.connection
    request.addfinalizer(engine.dispose)
    return engine


os.environ["SQLALCHEMY_WARN_20"] = "true"

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

# this happens after pytest.register_assert_rewrite to avoid pytest warning
from sqlalchemy.testing.plugin.pytestplugin import *  # noqa: F401, E402, F403


def pytest_sessionstart(session):
    """Run a hook for pytest sessionstart."""
    engine, _ = get_engine(db_params=SETUP_PARAMETERS)
    try:
        engine.execute(f"DROP DATABASE {DATABASE_TESTING};")
    except:
        ...
    engine.execute(f"CREATE DATABASE {DATABASE_TESTING};")
    testing.plugin.pytestplugin.pytest_sessionstart(session)


def pytest_sessionfinish(session, exitstatus):
    """Run a hook for pytest sessionfinish."""
    engine, _ = get_engine(db_params=SETUP_PARAMETERS)
    # engine.execute(f"DROP DATABASE {DATABASE_TESTING};")
    testing.plugin.pytestplugin.pytest_sessionfinish(session)
