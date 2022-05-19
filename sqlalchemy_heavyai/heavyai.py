"""Dialect module for heavyai."""
from sqlalchemy_heavyai.base import HeavyAIDialect


class HeavyAIDialect_heavyai(HeavyAIDialect):
    """HeavyAIDialect for heavyai."""

    driver = "heavydb"
    supports_statement_cache = True
