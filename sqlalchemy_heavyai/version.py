"""
Manage the version for sqlalchemy-heavyai.

Note:
    Update this for the versions
    Don't change the forth version number from None
"""
from importlib_metadata import PackageNotFoundError, version

try:
    _version = version("sqlalchemy_heavyai")
except PackageNotFoundError:
    # package is not installed
    _version = "0.0.0"

VERSION = tuple(v for v in _version.split(".")[:3]) + (None,)
