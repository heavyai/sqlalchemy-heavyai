import os
import sys

import pytest
import sqlalchemy
from packaging.version import Version
from sqlalchemy.testing import fixtures


class TestCI(fixtures.TestBase):

    def compare_versions(self, expected, current):
        expected = tuple(map(int, str(expected).split('.')))
        current = tuple(map(int, str(current).split('.')))[:len(expected)]
        assert expected == current

    def test_python_version(self):
        varname = "EXPECTED_PYTHON_VERSION"
        current = Version('.'.join(map(str, tuple(sys.version_info)[:3])))
        expected = os.environ.get(varname)
        if os.environ.get("CI"):
            assert expected is not None, (varname, current)
        if expected is None:
            pytest.skip(
                f"Undefined environment variable {varname},"
                f" cannot test python version (current={current})"
            )
        expected = Version(expected)
        self.compare_versions(expected, current)

    def test_sqlalchemy_version(self):
        varname = "EXPECTED_SQLALCHEMY_VERSION"
        current = Version(sqlalchemy.__version__)
        expected = os.environ.get(varname)
        if expected is None:
            pytest.skip(
                f"Undefined environment variable {varname},"
                f" cannot test sqlalchemy version (current={current})"
            )
        expected = Version(expected)
        self.compare_versions(expected, current)
