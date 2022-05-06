"""Dialect module for heavyai."""
from sqlalchemy_heavyai.base import HeavyAIDialect


class HeavyAIDialect_heavyai(HeavyAIDialect):
    """HeavyAIDialect for heavyai."""

    driver = "heavyai"
