import pytest
from sqlalchemy import (
    BigInteger,
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    SmallInteger,
    String,
)
from sqlalchemy.sql import column, table


@pytest.fixture(autouse=True)
def table_datatype():
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
    return table(
        "table1",
        column("id", Integer),
        column("name", String),
        column("value", Integer),
    )


@pytest.fixture(autouse=True)
def table2():
    return table(
        "table2",
        column("id", Integer),
        column("name", String),
        column("value", Integer),
    )
