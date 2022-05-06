"""Tests for the package."""
import sqlalchemy_heavyai


def test_versioning():
    """Check if the version is set correctly."""
    assert sqlalchemy_heavyai.__version__ not in (None, "", "0.0.0")
