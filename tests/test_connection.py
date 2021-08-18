"""Tests for connection."""
import sqlalchemy
from sqlalchemy.testing import fixtures


class ConnectionTest(fixtures.TestBase):
    """Test connection."""

    def test_metis_connection(self, uri_metis):
        """Test connection to metis server using https protocol."""
        engine = sqlalchemy.create_engine(uri_metis)
        con = engine.connect()
        con.close()

    def test_local_connection(self, uri_local):
        """Test connection to local server using binary protocol."""
        engine = sqlalchemy.create_engine(uri_local)
        con = engine.connect()
        con.close()

    def test_local_setup_connection(self, uri_local_setup):
        """Test connection to local server using binary protocol."""
        engine = sqlalchemy.create_engine(uri_local_setup)
        con = engine.connect()
        con.close()
