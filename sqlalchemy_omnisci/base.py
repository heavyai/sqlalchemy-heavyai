"""The base module for the OmniSci engine."""
import re

import sqlalchemy.types as sqltypes

# from sqlalchemy import exc as sa_exc
from sqlalchemy import util as sa_util
from sqlalchemy.engine import default, reflection
from sqlalchemy.pool import NullPool
from sqlalchemy.schema import Table
from sqlalchemy.sql import compiler, expression, selectable
from sqlalchemy.sql.elements import quoted_name
from sqlalchemy.types import (
    BIGINT,
    BINARY,
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
from sqlalchemy.types import Boolean as BooleanBase

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
        "VALUE",
        "VALUES",
        "WHENEVER",
        "WHERE",
        "WITH",
        "REGEXP",
        "RLIKE",
        "SOME",  # Snowflake Reserved words
        "MINUS",
        "INCREMENT",  # Oracle reserved words
        "COUNT",  # OmniSci reserved word
    ]
)


class ARRAY(sqltypes.TypeEngine):
    """Custom array SQL type."""

    __visit_name__ = "ARRAY"


class Boolean(BooleanBase):
    """Custom Boolean type."""

    def bind_processor(self, dialect):
        """Bind processor for boolean type."""
        # noqa
        _strict_as_bool = self._strict_as_bool

        def process(value):
            """Process boolean value."""
            value = _strict_as_bool(value)
            if value is not None:
                value = "'1'" if value else "'0'"
            return value

        return process


class BOOLEAN(Boolean):
    """Custom Boolean type."""

    __visit_name__ = "BOOLEAN"


ischema_names = {
    "BIGINT": BIGINT,
    "BINARY": BINARY,
    # 'BIT': BIT,
    "Boolean": Boolean,
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
    "NUMERIC": DECIMAL,
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

# OmniSci DML:
# - INSERT
AUTOCOMMIT_REGEXP = re.compile(r"\s*(?:INSERT)", re.I | re.UNICODE)


COMPOUND_KEYWORDS = {
    selectable.CompoundSelect.UNION_ALL: "UNION ALL",
}


class OmniSciIdentifierPreparer(compiler.IdentifierPreparer):
    """OmniSci Identifier Preparer."""

    reserved_words = set([x.lower() for x in RESERVED_WORDS])

    def __init__(self, dialect, **kw):
        """Create an instance for OmniSciIdentifierPreparer."""
        quote = '"'

        super().__init__(dialect, initial_quote=quote, escape_quote=quote)

    def _quote_free_identifiers(self, *ids):
        """Unilaterally identifier-quote any number of strings."""
        return tuple([self.quote(i) for i in ids if i is not None])


class OmniSciCompiler(compiler.SQLCompiler):
    """SQLCompiler for OmniSci."""

    compound_keywords = COMPOUND_KEYWORDS

    def default_from(selft):
        """Return the default FROM."""
        return " FROM DUAL"

    def visit_true(self, expr, **kw):
        """Return the value for TRUE."""
        return "'1'"

    def visit_false(self, expr, **kw):
        """Return the value for FALSE."""
        return "'0'"

    def visit_cast(self, cast, **kwargs):
        """Override the default CAST."""
        cast_target = cast.typeclause._compiler_dispatch(self, **kwargs)

        if any(
            [t in cast_target.lower() for t in ["string", "varchar", "text"]]
        ):
            raise NotImplementedError(
                (
                    "Casting to {} not implemented. See "
                    "See https://docs.omnisci.com/sql/data-manipulation-dml/"
                    "sql-capabilities#type-cast-support"
                ).format(cast_target)
            )

        return super().visit_cast(cast, **kwargs)

    def visit_index(self, *args, **kwargs):
        """Override the default INDEX.

        OmniSci doesn't implement INDEX yet.
        """
        return

    def visit_compound_select(
        self, cs, asfrom=False, compound_index=None, **kwargs
    ):
        """Override the default COMPOUND SELECT."""
        if cs.keyword not in self.compound_keywords:
            raise NotImplementedError(
                "Given CompoundSelect {} not found.".format(cs.keyword)
            )

        super().visit_compound_select(
            cs, asfrom=False, compound_index=None, **kwargs
        )

    def limit_clause(self, select, **kw):
        """Override the default LIMIT CLAUSE."""
        text = ""
        if select._limit_clause is not None:
            text += " \n LIMIT " + self.process(select._limit_clause, **kw)
        if select._offset_clause is not None:
            text += " OFFSET " + self.process(select._offset_clause, **kw)
        return text


class OmniSciExecutionContext(default.DefaultExecutionContext):
    """OmniSci Execution Context."""

    def pre_exec(self):
        """Define the pre-execution step."""
        parameters = []
        for i, line in enumerate(self.parameters):
            if not isinstance(line, dict):
                parameters.append(line)
                continue

            _line = {}
            for k, v in dict(line).items():
                _line[k] = v
                _v = self.compiled_parameters[i][k]
                if isinstance(_v, bool):
                    _line[k] = "true" if _v is True else "false"

            parameters.append(_line)

        self.parameters = self.parameters.__class__(parameters)

    def should_autocommit_text(self, statement):
        """Check if autocommit should be executed."""
        return AUTOCOMMIT_REGEXP.match(statement)

    @sa_util.memoized_property
    def should_autocommit(self):
        """Check if autocommit should be executed."""
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


class OmniSciDDLCompiler(compiler.DDLCompiler):
    """OmniSciDDL Compiler."""

    def denormalize_column_name(self, name):
        """Denormalize the given column name."""
        if name is None:
            return None
        elif name.lower() == name and not self.preparer._requires_quotes(
            name.lower()
        ):
            # no quote as case insensitive
            return name
        return self.preparer.quote(name)

    def get_column_specification(self, column, **kwargs):
        """Get column specifications."""
        colspec = [
            self.preparer.format_column(column),
            self.dialect.type_compiler.process(
                column.type, type_expression=column
            ),
        ]

        if not column.nullable:
            colspec.append("NOT NULL")

        return " ".join(colspec)

    def visit_primary_key_constraint(self, constraint, **kw):
        """Override the primary key constraint implementation.

        NOTE: OmniSciDB doesn't implement primary key
        """
        return

    def visit_foreign_key_constraint(self, constraint, **kw):
        """Override the foreign key constraint implementation.

        NOTE: OmniSciDB doesn't implement foreign key
        """
        return

    def visit_unique_constraint(self, constraint, **kw):
        """Override the unique key constraint implementation.

        NOTE: OmniSciDB doesn't implement unique key
        """
        return

    def visit_create_index(self, *args, **kwargs):
        """Override the index constraint implementation.

        NOTE: OmniSciDB doesn't implement index
        """
        return


class OmniSciTypeCompiler(compiler.GenericTypeCompiler):
    """OmniSci Type Compiler."""

    def visit_ARRAY(selfself, type, **kw):
        """Define the ARRAY compilation."""
        return "ARRAY"

    def visit_numeric(self, type_, **kw):
        """Override the Numeric compilation."""
        return self.visit_DECIMAL(type_, **kw)

    def visit_datetime(self, type_, **kw):
        """Override the Date Time compilation."""
        return self.visit_TIMESTAMP(type_, **kw)


colspecs: dict = {}


class OmniSciDialect(default.DefaultDialect):
    """OmniSci Dialect."""

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
    supports_native_boolean = False

    # The dialect supports ``ALTER TABLE``.
    supports_alter = True

    # The dialect supports CREATE SEQUENCE or similar.
    supports_sequences = False

    # The dialect supports a native ENUM construct.
    supports_native_enum = False

    preparer = OmniSciIdentifierPreparer
    ddl_compiler = OmniSciDDLCompiler
    type_compiler = OmniSciTypeCompiler
    statement_compiler = OmniSciCompiler
    execution_ctx_cls = OmniSciExecutionContext

    # indicates symbol names are
    # UPPERCASEd if they are case insensitive
    # within the database.
    # if this is True, the methods normalize_name()
    # and denormalize_name() must be provided.
    requires_name_normalize = True

    def __init__(self, pool=NullPool, **kwargs):
        """Create an instance for the OmniSci Dialect."""
        default.DefaultDialect.__init__(self, **kwargs)

    @classmethod
    def dbapi(cls):
        """Return the database api."""
        import pyomnisci

        return pyomnisci

    def set_connection_execution_options(self, connection, opts):
        """Set connection execution options."""
        connection.schema_for_object = None

    def _check_unicode_returns(self, connection):
        return

    @property
    def _dialect_specific_select_one(self):
        return "SELECT 1"

    def do_rollback(self, connection):
        """Override the rollback method.

        Note: OmniSci hasn't transaction implemented so it cannot rollback
        changes.
        """
        return

    def create_connect_args(self, url):
        """Create a connect arguments from given url."""
        opts = url.translate_connect_args(username="user", database="dbname")
        opts.update(url.query)
        return ([], opts)

    def has_table(self, connection, table_name, schema=None):
        """Check if the table exists."""
        return table_name in self.get_table_names(connection, schema)

    def has_sequence(self, connection, sequence_name, schema=None):
        """Check if the sequence exists.

        Note: OmniSci hasnt sequence objects.
        """
        return

    def normalize_name(self, name):
        """Normalize given name."""
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
        """Denormalize given name."""
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
        """Get all indexes.

        Note: index is not supported by OmniSci.
        """
        return []

    @reflection.cache
    def get_primary_keys(self, connection, table_name, schema=None, **kw):
        """
        Override function that return the list of primary keys.

        Note: primary keys aren't supported by OmniSci.
        """
        return []

    @reflection.cache
    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        """
        Override function that return the list of constraints.

        Note: constraints aren't supported by OmniSci.
        """
        return []

    @reflection.cache
    def get_unique_constraint(self, connection, table_name, schema=None, **kw):
        """
        Override function that return the list of unique keys.

        Note: unique keys arent supported by OmniSci.
        """
        return []

    @reflection.cache
    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        """
        Override function that return the list of foreign keys.

        Note: foreign keys arent supported by OmniSci.
        """
        return []

    @reflection.cache
    def get_columns(self, connection, table_name, schema=None, **kw):
        """Get all column info given the table info."""
        conn_api = connection.connect()
        columns_details = conn_api.connection.get_table_details(table_name)
        conn_api.close()

        columns = []
        for column_row in columns_details:
            col_type = self.ischema_names.get(column_row[1])
            extra_setting = {"default": None}
            if col_type is None:
                col_type = sqltypes.NULLTYPE
                raise Exception(
                    "Didn't recognize type '{0}' of "
                    "column '{1}'".format(column_row[1], column_row[0])
                )

            if isinstance(col_type(), sqltypes.DECIMAL):
                col_type = sqltypes.DECIMAL(
                    precision=column_row.precision, scale=column_row.scale
                )

            elif isinstance(col_type(), sqltypes.VARCHAR):
                col_type = sqltypes.VARCHAR(
                    length=(column_row.comp_param - 6) * 2
                )

            cdict = {
                "name": column_row[0],
                "type": col_type,
                "nullable": column_row[2],
            }
            cdict.update(extra_setting)
            columns.append(cdict)
        return columns

    @reflection.cache
    def get_schema_names(self, connection, **kw):
        """
        Return all database as schemas.

        Note: Maybe it would be better to return the database we are
        connected to.
        """
        schemas = []
        conn_api = connection.engine.raw_connection()
        for i in conn_api.connection._client.get_databases(
            conn_api.connection._session
        ):
            schemas.append(i.db_name)
        conn_api.close()
        return schemas

    @reflection.cache
    def get_table_names(self, connection, schema=None, **kw):
        """Get all table names."""
        conn_api = connection.engine.raw_connection()
        return [
            table_name
            for table_name in conn_api.connection._client.get_physical_tables(
                conn_api.connection._session
            )
        ]

    @reflection.cache
    def get_view_names(self, connection, schema=None, **kw):
        """Get all view names."""
        conn_api = connection.engine.raw_connection()
        return [
            view_name
            for view_name in conn_api.connection._client.get_views(
                conn_api.connection._session
            )
        ]

    @reflection.cache
    def get_view_definition(self, connection, view_name, schema=None, **kw):
        """Get the view definition."""
        view_definition = None
        conn_api = connection.engine.raw_connection()

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
        """Override function that return the list of temporary tables name."""
        # TODO: check a way to get the name of the temporary tables.
        return []


dialect = OmniSciDialect


construct_arguments = [(Table, {"clusterby": None})]
