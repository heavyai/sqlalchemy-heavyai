#!/usr/bin/env python

import re

import sqlalchemy.types as sqltypes

# from sqlalchemy import exc as sa_exc
from sqlalchemy import util as sa_util
from sqlalchemy.engine import default, reflection
from sqlalchemy.pool import NullPool
from sqlalchemy.schema import Table
from sqlalchemy.sql import compiler, expression
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.types import (
    BIGINT,
    BINARY,
    BOOLEAN,
    CHAR,
    DATE,
    DATETIME,
    DECIMAL,
    FLOAT,
    INTEGER,
    REAL,
    SMALLINT,
    TIME,
    TIMESTAMP,
    VARCHAR,
)

# from ..connector.constants import UTF8

RESERVED_WORDS = frozenset(
    [
        "ALL",
        "ALTER",
        "AND",
        "ANY",
        "AS",
        "BETWEEN",
        "BY",
        "CHECK",
        "COLUMN",
        "CONNECT",
        "COPY",
        "CREATE",
        "CURRENT",
        "DELETE",
        "DISTINCT",
        "DROP",
        "ELSE",
        "EXISTS",
        "FOR",
        "FROM",
        "GRANT",
        "GROUP",
        "HAVING",
        "IN",
        "INSERT",
        "INTERSECT",
        "INTO",
        "IS",
        "LIKE",
        "NOT",
        "NULL",
        "OF",
        "ON",
        "OR",
        "ORDER",
        "REVOKE",
        "ROW",
        "ROWS",
        "SELECT",
        "SET",
        "START",
        "TABLE",
        "THEN",
        "TO",
        "TRIGGER",
        "UNION",
        "UNIQUE",
        "UPDATE",
        "VALUES",
        "WHENEVER",
        "WHERE",
        "WITH",
        "REGEXP",
        "RLIKE",
        "SOME",  # Snowflake Reserved words
        "MINUS",
        "INCREMENT",  # Oracle reserved words
        "COUNT",  # Omnisci reserved word
    ]
)

colspecs: dict = {}


class ARRAY(sqltypes.TypeEngine):
    __visit_name__ = "ARRAY"


ischema_names = {
    "BIGINT": BIGINT,
    "BINARY": BINARY,
    # 'BIT': BIT,
    "BOOLEAN": BOOLEAN,
    "CHAR": CHAR,
    "CHARACTER": CHAR,
    "DATE": DATE,
    "DATETIME": DATETIME,
    "DEC": DECIMAL,
    "DECIMAL": DECIMAL,
    "DOUBLE": FLOAT,
    "FIXED": DECIMAL,
    "FLOAT": FLOAT,
    "INT": INTEGER,
    "INTEGER": INTEGER,
    "NUMBER": DECIMAL,
    #    'OBJECT': ?,
    "REAL": REAL,
    "BYTEINT": SMALLINT,
    "SMALLINT": SMALLINT,
    "STRING": VARCHAR,
    "STR": VARCHAR,
    "TEXT": VARCHAR,
    "TIME": TIME,
    "TIMESTAMP": TIMESTAMP,
    # 'TIMESTAMP_LTZ': TIMESTAMP,
    # 'TIMESTAMP_TZ': TIMESTAMP,
    # 'TIMESTAMP_NTZ': TIMESTAMP,
    "TINYINT": SMALLINT,
    "VARBINARY": BINARY,
    "VARCHAR": VARCHAR,
    "ARRAY": ARRAY,
    "POINT": VARCHAR,
    "MULTIPOINT": VARCHAR,
    "LINESTRING": VARCHAR,
    "MULTILINESTRING": VARCHAR,
    "MULTIPOLYGON": VARCHAR,
}

# Omnisci DML:
# - INSERT
AUTOCOMMIT_REGEXP = re.compile(r"\s*(?:INSERT)", re.I | re.UNICODE)


class OmnisciIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = set([x.lower() for x in RESERVED_WORDS])

    def __init__(self, dialect, **kw):
        quote = '"'

        super(OmnisciIdentifierPreparer, self).__init__(
            dialect, initial_quote=quote, escape_quote=quote
        )

    def _quote_free_identifiers(self, *ids):
        """
        Unilaterally identifier-quote any number of strings.
        """
        return tuple([self.quote(i) for i in ids if i is not None])


class OmnisciCompiler(compiler.SQLCompiler):
    def default_from(selft):
        return " FROM DUAL"


class OmnisciExecutionContext(default.DefaultExecutionContext):
    def should_autocommit_text(self, statement):
        return AUTOCOMMIT_REGEXP.match(statement)

    @sa_util.memoized_property
    def should_autocommit(self):
        autocommit = self.execution_options.get(
            "autocommit",
            not self.compiled
            and self.statement
            and expression.PARSE_AUTOCOMMIT
            or False,
        )

        if autocommit is expression.PARSE_AUTOCOMMIT:
            return self.should_autocommit_text(self.unicode_statement)
        else:
            return autocommit and not self.isddl


class OmnisciDDLCompiler(compiler.DDLCompiler):
    def denormalize_column_name(self, name):
        if name is None:
            return None
        elif name.lower() == name and not self.preparer._requires_quotes(
            name.lower()
        ):
            # no quote as case insensitive
            return name
        return self.preparer.quote(name)

    def get_column_specification(self, column, **kwargs):
        """
        Gets Column specifications
        """
        colspec = [
            self.preparer.format_column(column),
            self.dialect.type_compiler.process(
                column.type, type_expression=column
            ),
        ]

        if not column.nullable:
            colspec.append("NOT NULL")

        return " ".join(colspec)


class OmnisciTypeCompiler(compiler.GenericTypeCompiler):
    def visit_ARRAY(selfself, type, **kw):
        return "ARRAY"


class OmnisciDialect(default.DefaultDialect):
    name = "omnisci"
    max_identifier_length = 32768

    #    encoding = UTF8
    default_paramstyle = "pyformat"
    colspecs = colspecs
    ischema_names = ischema_names

    # all str types must be converted in Unicode
    convert_unicode = True

    # Indicate whether the DB-API can receive SQL statements as Python
    #  unicode strings
    supports_unicode_statements = True
    supports_unicode_binds = True
    returns_unicode_strings = True
    description_encoding = None

    # No lastrowid support. See SNOW-11155
    postfetch_lastrowid = False

    # Indicate whether the dialect properly implements rowcount for
    #  ``UPDATE`` and ``DELETE`` statements.
    supports_sane_rowcount = False

    # Indicate whether the dialect properly implements rowcount for
    # ``UPDATE`` and ``DELETE`` statements when executed via
    # executemany.
    supports_sane_multi_rowcount = False

    # NUMERIC type returns decimal.Decimal
    supports_native_decimal = True

    # The dialect supports a native boolean construct.
    # This will prevent types.Boolean from generating a CHECK
    # constraint when that type is used.
    supports_native_boolean = True

    # The dialect supports ``ALTER TABLE``.
    supports_alter = True

    # The dialect supports CREATE SEQUENCE or similar.
    supports_sequences = False

    # The dialect supports a native ENUM construct.
    supports_native_enum = False

    preparer = OmnisciIdentifierPreparer
    ddl_compiler = OmnisciDDLCompiler
    type_compiler = OmnisciTypeCompiler
    statement_compiler = OmnisciCompiler
    execution_ctx_cls = OmnisciExecutionContext

    # indicates symbol names are
    # UPPERCASEd if they are case insensitive
    # within the database.
    # if this is True, the methods normalize_name()
    # and denormalize_name() must be provided.
    requires_name_normalize = True

    def __init__(self, pool=NullPool, **kwargs):
        default.DefaultDialect.__init__(self, **kwargs)

    @classmethod
    def dbapi(cls):
        import pyomnisci

        return pyomnisci

    def set_connection_execution_options(self, connection, opts):
        connection.schema_for_object = None

    def _check_unicode_returns(self, connection):
        return

    def _dialect_specific_select_one(self):
        return str("1")

    def do_rollback(self, connection):
        # Omnisci hasnt transaction implemented so it cannot rollback changes
        return

    def create_connect_args(self, url):
        opts = url.translate_connect_args(username="user", database="dbname")
        return ([], opts)

    def get_tables(self):
        # TODO
        return []

    def has_table(self, connection, table_name, schema=None):
        """
        Checks if the table exists
        """
        return table_name in self.get_tables()

    def has_sequence(self, connection, sequence_name, schema=None):
        """
        Checks if the sequence exists
        """
        # Omnisci hasnt sequence objects
        return

    def normalize_name(self, name):
        if name is None:
            return None
        if (
            name.upper() == name
            and not self.identifier_preparer._requires_quotes(name.lower())
        ):
            return name.lower()
        elif name.lower() == name:
            return quoted_name(name, quote=True)
        else:
            return name

    def denormalize_name(self, name):
        if name is None:
            return None
        elif (
            name.lower() == name
            and not self.identifier_preparer._requires_quotes(name.lower())
        ):
            name = name.upper()
        return name

    def _denormalize_quote_join(self, *idents):
        return ".".join(
            self.identifier_preparer._quote_free_identifiers(*idents)
        )

    @staticmethod
    def _map_name_to_idx(result):
        name_to_idx = {}
        for idx, col in enumerate(result.cursor.description):
            name_to_idx[col[0]] = idx
        return name_to_idx

    @reflection.cache
    def get_indexes(self, connection, table_name, schema=None, **kw):
        """
        Gets all indexes
        """
        # no index is supported by Omnisci
        return []

    @reflection.cache
    def get_primary_keys(self, connection, table_name, schema=None, **kw):
        # primary keys arent supported by Omnisci
        return []

    @reflection.cache
    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        """
        Gets all foreign keys
        """
        # foreign keys arent supported by Omnisci
        return []

    @reflection.cache
    def get_columns(self, connection, table_name, schema=None, **kw):
        """
        Gets all column info given the table info
        """
        conn_api = connection.connect()
        columns_details = conn_api.connection.get_table_details(table_name)
        conn_api.close()

        columns = []
        for column_row in columns_details:
            col_type = self.ischema_names.get(column_row[1])
            if col_type is None:
                col_type = sqltypes.NULLTYPE
                raise Exception(
                    "Didn't recognize type '{0}' of "
                    "column '{1}'".format(column_row[1], column_row[0])
                )

            cdict = {
                "name": column_row[0],
                "type": col_type,
                "nullable": column_row[2],
            }
            columns.append(cdict)
        return columns

    @reflection.cache
    def get_schema_names(self, connection, **kw):
        """
        Return all database as schemas. Maybe it would be better to return
        the database we are connected to
        """
        schemas = []
        conn_api = connection.raw_connection()
        for i in conn_api.connection._client.get_databases(
            conn_api.connection._session
        ):
            schemas.append(i.db_name)
        conn_api.close()
        return schemas

    @reflection.cache
    def get_table_names(self, connection, schema=None, **kw):
        """
        Gets all table names.
        """
        conn_api = connection.raw_connection()
        return [
            table_name
            for table_name in conn_api.connection._client.get_physical_tables(
                conn_api.connection._session
            )
        ]

    @reflection.cache
    def get_view_names(self, connection, schema=None, **kw):
        # there isnt support on API to
        """
        Gets all view names
        """
        conn_api = connection.raw_connection()
        return [
            view_name
            for view_name in conn_api.connection._client.get_views(
                conn_api.connection._session
            )
        ]

    @reflection.cache
    def get_view_definition(self, connection, view_name, schema=None, **kw):
        """
        Gets the view definition
        """
        view_definition = None
        conn_api = connection.raw_connection()

        # TODO
        table_name = ""

        if view_name in conn_api.connection._client.get_views(
            conn_api.connection._session
        ):
            view_definition = (
                "create view "
                + view_name
                + " as "
                + conn_api.connection.get_table_details(table_name).view_sql
            )
        conn_api.close()
        return view_definition

    def get_temp_table_names(self, connection, schema=None, **kw):
        # there arent temp tables in Mpad
        return []


dialect = OmnisciDialect

construct_arguments = [(Table, {"clusterby": None})]
