import os
import sys

import importlib_metadata
import pytest
from packaging.version import Version


def test_python_version():
    varname = "EXPECTED_PYTHON_VERSION"
    current = Version(sys.version_info)
    expected = os.environ.get(varname)
    if os.environ.get("CI"):
        assert expected is not None, (varname, current)
    if expected is None:
        pytest.skip(
            f"Undefined environment variable {varname},"
            f" cannot test python version (current={current})"
        )
    expected = Version(expected)
    assert expected == current


def test_sqlalchemy_version():
    varname = "EXPECTED_SQLALCHEMY_VERSION"
    current = Version(importlib_metadata.version("sqlalchemy"))
    expected = os.environ.get(varname)
    if expected is None:
        pytest.skip(
            f"Undefined environment variable {varname},"
            f" cannot test sqlalchemy version (current={current})"
        )
    expected = Version(expected)
    assert expected == current
