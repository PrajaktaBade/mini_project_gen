import pytest
from db import get_connection
import psycopg2


def test_database_connection():
    try:
        conn = get_connection()
        assert conn is not None, "Connection object is None"
        assert isinstance(conn, psycopg2.extensions.connection), "Not a psycopg2 connection"
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")
