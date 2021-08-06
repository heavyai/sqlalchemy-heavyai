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


# TODO: check a better way to do it
XFAIL_UNSUPPORTED = [
    "CastTypeDecoratorTest_omnisci+pyomnisci.test_special_type",
    "ComponentReflectionTest_omnisci+pyomnisci.test_get_indexes[False-_exclusions0]",
    "test_get_schema_names",
    # exception about union
    "CompoundSelectTest_omnisci+pyomnisci.test_distinct_selectable_in_unions",
    "CompoundSelectTest_omnisci+pyomnisci.test_limit_offset_aliased_selectable_in_unions",
    "CompoundSelectTest_omnisci+pyomnisci.test_plain_union",
    "CompoundSelectTest_omnisci+pyomnisci.test_select_from_plain_union",
    "DeprecatedCompoundSelectTest_omnisci+pyomnisci.test_distinct_selectable_in_unions",
    "DeprecatedCompoundSelectTest_omnisci+pyomnisci.test_limit_offset_aliased_selectable_in_unions",
    "DeprecatedCompoundSelectTest_omnisci+pyomnisci.test_plain_union",
    # missing microseconds
    "DateTimeMicrosecondsTest_omnisci+pyomnisci.test_round_trip",
    "DateTimeMicrosecondsTest_omnisci+pyomnisci.test_round_trip_decorated",
    "TimeMicrosecondsTest_omnisci+pyomnisci.test_round_trip",
    "TimeMicrosecondsTest_omnisci+pyomnisci.test_round_trip_decorated",
    # omnisci doesn't have primary key
    "ExceptionTest_omnisci+pyomnisci.test_integrity_error",
    # string comparison
    "NormalizedNameTest_omnisci+pyomnisci.test_get_table_names",
    # decimal output should be decimal instead of float
    "NumericTest_omnisci+pyomnisci.test_decimal_coerce_round_trip_w_cast",
    "NumericTest_omnisci+pyomnisci.test_numeric_as_decimal",
    "NumericTest_omnisci+pyomnisci.test_render_literal_numeric",
    # empty text wrong converted to None
    "TextTest_omnisci+pyomnisci.test_text_empty_strings",
]

EXPECTED_DBAPI_ERROR = [
    # exception: Insert into a subset of columns is not supported yet
    "DateTest_omnisci+pyomnisci.test_null",
    "DateTest_omnisci+pyomnisci.test_null_bound_comparison",
    "DateTest_omnisci+pyomnisci.test_round_trip",
    "DateTest_omnisci+pyomnisci.test_round_trip_decorated",
    "DateTimeCoercedToDateTimeTest_omnisci+pyomnisci.test_null",
    "DateTimeCoercedToDateTimeTest_omnisci+pyomnisci.test_null_bound_comparison",
    "DateTimeCoercedToDateTimeTest_omnisci+pyomnisci.test_round_trip",
    "DateTimeCoercedToDateTimeTest_omnisci+pyomnisci.test_round_trip_decorated",
    "DateTimeMicrosecondsTest_omnisci+pyomnisci.test_null",
    "DateTimeMicrosecondsTest_omnisci+pyomnisci.test_null_bound_comparison",
    "DateTimeMicrosecondsTest_omnisci+pyomnisci.test_round_trip",
    "DateTimeMicrosecondsTest_omnisci+pyomnisci.test_round_trip_decorated",
    "DateTimeTest_omnisci+pyomnisci.test_null",
    "DateTimeTest_omnisci+pyomnisci.test_null_bound_comparison",
    "DateTimeTest_omnisci+pyomnisci.test_round_trip",
    "DateTimeTest_omnisci+pyomnisci.test_round_trip_decorated",
    # SQL Error: DEFAULT FROM
    "ExistsTest_omnisci+pyomnisci.test_select_exists",
    "ExistsTest_omnisci+pyomnisci.test_select_exists_false",
    # Exception: Variable length types not supported in VALUES yet.
    "ExpandingBoundInTest_omnisci+pyomnisci.test_empty_set_against_string_bindparam",
    "ExpandingBoundInTest_omnisci+pyomnisci.test_empty_set_against_string_direct",
    "ExpandingBoundInTest_omnisci+pyomnisci.test_empty_set_against_string_negation_bindparam",
    "ExpandingBoundInTest_omnisci+pyomnisci.test_empty_set_against_string_negation_direct",
    # Column data does not exist
    "CollateTest_omnisci+pyomnisci.test_collate_order_by",
    # The matching pattern must be a literal
    "LikeFunctionsTest_omnisci+pyomnisci.test_startswith_unescaped",
    "LikeFunctionsTest_omnisci+pyomnisci.test_startswith_autoescape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_startswith_sqlexpr",
    "LikeFunctionsTest_omnisci+pyomnisci.test_startswith_escape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_startswith_autoescape_escape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_endswith_unescaped",
    "LikeFunctionsTest_omnisci+pyomnisci.test_endswith_sqlexpr",
    "LikeFunctionsTest_omnisci+pyomnisci.test_endswith_autoescape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_endswith_escape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_endswith_autoescape_escape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_contains_unescaped",
    "LikeFunctionsTest_omnisci+pyomnisci.test_contains_autoescape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_contains_escape",
    "LikeFunctionsTest_omnisci+pyomnisci.test_contains_autoescape_escape",
    # empty SQL statment not allowed
    "LongNameBlowoutTest_omnisci+pyomnisci.test_long_convention_name[ix-_exclusions2]",
    # function not supported
    "OrderByLabelTest_omnisci+pyomnisci.test_composed_multiple",
]

EXPECTED_ERROR = [
    # problems with text() when using special character
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[%percent]",
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[/slashes/]",
    r"DifficultParametersTest_omnisci+pyomnisci.test_round_trip[more :: %colons%]",
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[more/slashes]",
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[par(ens)]",
    r"DifficultParametersTest_omnisci+pyomnisci.test_round_trip[per % cent]",
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[per cent]",
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[percent%(ens)yah]",
    "DifficultParametersTest_omnisci+pyomnisci.test_round_trip[q?marks]",
    # TypeError: expected bytes, str found
    "UnicodeTextTest_omnisci+pyomnisci.test_round_trip",
    "UnicodeTextTest_omnisci+pyomnisci.test_round_trip_executemany",
    "UnicodeVarcharTest_omnisci+pyomnisci.test_round_trip",
    "UnicodeVarcharTest_omnisci+pyomnisci.test_round_trip_executemany",
    # omnisci doesn't implement primary key
    "LongNameBlowoutTest_omnisci+pyomnisci.test_long_convention_name[pk-_exclusions1]",
    # KeyError
    "NormalizedNameTest_omnisci+pyomnisci.test_reflect_lowercase_forced_tables",
]


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem, XFAIL_UNSUPPORTED=XFAIL_UNSUPPORTED):
    """Dynamically add an xfail marker for specific backends."""
    # internal function that forces the rollback
    def rollback_transaction(pyfuncitem):
        try:
            # force a rollback action
            if (
                "connection" in pyfuncitem.funcargs
                and pyfuncitem.funcargs["connection"].get_transaction()
            ):
                pyfuncitem.funcargs["connection"].get_transaction().rollback()
                warnings.warn("Rollback done.")
        except Exception as e:
            warnings.warn(e)

    outcome = yield
    success = True

    try:
        outcome.get_result()
    except (
        NotImplementedError,
        AssertionError,
    ) as e:
        if pyfuncitem.location[-1] not in XFAIL_UNSUPPORTED:
            rollback_transaction(pyfuncitem)
            raise e
        pytest.xfail(reason=repr(e))
    except sqlalchemy.exc.DBAPIError as e:
        if pyfuncitem.location[-1] not in EXPECTED_DBAPI_ERROR:
            rollback_transaction(pyfuncitem)
            raise e
        pytest.xfail(reason=repr(e))
    except Exception as e:
        if pyfuncitem.location[-1] not in EXPECTED_ERROR:
            rollback_transaction(pyfuncitem)
            raise e
        pytest.xfail(reason=repr(e))
