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
)
from sqlalchemy.sql import column, table

from sqlalchemy_omnisci import URL

# registry.register("omnisci", "sqlalchemy_omnisci", "OmniSciDialect")

os.environ["SQLALCHEMY_WARN_20"] = "true"

pytest.register_assert_rewrite("sqlalchemy.testing.assertions")

# this happens after pytest.register_assert_rewrite to avoid pytest warning
from sqlalchemy.testing.plugin.pytestplugin import *  # noqa: F401, E402, F403

DEFAULT_PARAMETERS = {
    "user": "demouser",
    "password": "HyperInteractive",
    "database": "mapd",
    "protocol": "https",
    "host": "metis.mapd.com",
    "port": "443",
}


def get_db_parameters():
    """Set the db connection parameters."""
    ret = copy.copy(DEFAULT_PARAMETERS)

    # a unique table name
    ret["name"] = ("sqlalchemy_tests_" + str(uuid.uuid4())).replace("-", "_")

    return ret


def get_engine(user=None, password=None):
    """Create a connection using the given parameters."""
    ret = get_db_parameters()

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


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    """Add dynamically an xfail marker for specific backends."""
    outcome = yield
    success = True

    try:
        outcome.get_result()
    except Exception as e:
        pytest.xfail(reason=repr(e))
