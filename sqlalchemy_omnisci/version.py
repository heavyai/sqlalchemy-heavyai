"""
Manage the version for sqlalchemy-omnisci.

Note:
    Update this for the versions
    Don't change the forth version number from None
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("sqlalchemy_omnisci")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"

VERSION = tuple(__version__.split(".")) + (None,)
