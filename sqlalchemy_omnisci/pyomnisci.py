"""Dialect module for pyomnisci."""
from sqlalchemy_omnisci.base import OmniSciDialect


class OmniSciDialect_pyomnisci(OmniSciDialect):
    """OmniSciDialect for pyomnisci."""

    driver = "pyomnisci"
