"""
Manage the version for sqlalchemy-omnisci.

Note:
    Update this for the versions
    Don't change the forth version number from None
"""
from importlib.metadata import PackageNotFoundError, version

try:
    _version = version("sqlalchemy_omnisci")
except PackageNotFoundError:
    # package is not installed
    _version = "0.0.0"

VERSION = tuple(int(v) for v in _version.split(".")) + (None,)
