"""Tests for connection."""
import sqlalchemy
from sqlalchemy.testing import fixtures


class ConnectionTest(fixtures.TestBase):
    """Test connection."""

    def test_metis_connection(self, uri_metis):
        """Test connection to metis server using https protocol."""
        sqlalchemy.create_engine(uri_metis)

    def test_local_connection(self, uri_local):
        """Test connection to local server using binary protocol."""
        sqlalchemy.create_engine(uri_local)
