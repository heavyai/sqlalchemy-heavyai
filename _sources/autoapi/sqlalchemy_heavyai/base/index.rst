:py:mod:`sqlalchemy_heavyai.base`
=================================

.. py:module:: sqlalchemy_heavyai.base

.. autoapi-nested-parse::

   The base module for the HeavyAI engine.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   sqlalchemy_heavyai.base.ARRAY
   sqlalchemy_heavyai.base.Boolean
   sqlalchemy_heavyai.base.BOOLEAN
   sqlalchemy_heavyai.base.HeavyAIIdentifierPreparer
   sqlalchemy_heavyai.base.HeavyAICompiler
   sqlalchemy_heavyai.base.HeavyAIExecutionContext
   sqlalchemy_heavyai.base.HeavyAIDDLCompiler
   sqlalchemy_heavyai.base.HeavyAITypeCompiler
   sqlalchemy_heavyai.base.HeavyAIDialect




Attributes
~~~~~~~~~~

.. autoapisummary::

   sqlalchemy_heavyai.base.is_sqlalchemy_v2
   sqlalchemy_heavyai.base.RESERVED_WORDS
   sqlalchemy_heavyai.base.ischema_names
   sqlalchemy_heavyai.base.AUTOCOMMIT_REGEXP
   sqlalchemy_heavyai.base.COMPOUND_KEYWORDS
   sqlalchemy_heavyai.base.colspecs
   sqlalchemy_heavyai.base.dialect
   sqlalchemy_heavyai.base.construct_arguments


.. py:data:: is_sqlalchemy_v2

   

.. py:data:: RESERVED_WORDS

   

.. py:class:: ARRAY

   Bases: :py:obj:`sqlalchemy.types.TypeEngine`

   Custom array SQL type.

   .. py:attribute:: __visit_name__
      :value: 'ARRAY'

      


.. py:class:: Boolean(create_constraint: bool = False, name: Optional[str] = None, _create_events: bool = True, _adapted_from: Optional[SchemaType] = None)

   Bases: :py:obj:`sqlalchemy.types.Boolean`

   Custom Boolean type.

   .. py:method:: bind_processor(dialect)

      Bind processor for boolean type.



.. py:class:: BOOLEAN(create_constraint: bool = False, name: Optional[str] = None, _create_events: bool = True, _adapted_from: Optional[SchemaType] = None)

   Bases: :py:obj:`Boolean`

   Custom Boolean type.

   .. py:attribute:: __visit_name__
      :value: 'BOOLEAN'

      


.. py:data:: ischema_names

   

.. py:data:: AUTOCOMMIT_REGEXP

   

.. py:data:: COMPOUND_KEYWORDS

   

.. py:class:: HeavyAIIdentifierPreparer(dialect, **kw)

   Bases: :py:obj:`sqlalchemy.sql.compiler.IdentifierPreparer`

   HeavyAI Identifier Preparer.

   .. py:attribute:: reserved_words

      

   .. py:method:: _quote_free_identifiers(*ids)

      Unilaterally identifier-quote any number of strings.



.. py:class:: HeavyAICompiler(dialect: sqlalchemy.engine.interfaces.Dialect, statement: Optional[sqlalchemy.sql.elements.ClauseElement], cache_key: Optional[sqlalchemy.sql.cache_key.CacheKey] = None, column_keys: Optional[Sequence[str]] = None, for_executemany: bool = False, linting: Linting = NO_LINTING, **kwargs: Any)

   Bases: :py:obj:`sqlalchemy.sql.compiler.SQLCompiler`

   SQLCompiler for HeavyAI.

   .. py:attribute:: compound_keywords

      

   .. py:method:: visit_true(expr, **kw)

      Return the value for TRUE.


   .. py:method:: visit_false(expr, **kw)

      Return the value for FALSE.


   .. py:method:: visit_cast(cast, **kwargs)

      Override the default CAST.


   .. py:method:: visit_index(*args, **kwargs)

      Override the default INDEX.

      HeavyDB doesn't implement INDEX yet.


   .. py:method:: visit_compound_select(cs, asfrom=False, compound_index=None, **kwargs)

      Override the default COMPOUND SELECT.


   .. py:method:: limit_clause(select, **kw)

      Override the default LIMIT CLAUSE.



.. py:class:: HeavyAIExecutionContext

   Bases: :py:obj:`sqlalchemy.engine.default.DefaultExecutionContext`

   HeavyAI Execution Context.

   .. py:method:: pre_exec()

      Define the pre-execution step.


   .. py:method:: should_autocommit_text(statement)

      Check if autocommit should be executed.


   .. py:method:: should_autocommit()

      Check if autocommit should be executed.



.. py:class:: HeavyAIDDLCompiler(dialect: sqlalchemy.engine.interfaces.Dialect, statement: Optional[sqlalchemy.sql.elements.ClauseElement], schema_translate_map: Optional[sqlalchemy.engine.interfaces.SchemaTranslateMapType] = None, render_schema_translate: bool = False, compile_kwargs: Mapping[str, Any] = util.immutabledict())

   Bases: :py:obj:`sqlalchemy.sql.compiler.DDLCompiler`

   HeavyAIDDL Compiler.

   .. py:method:: denormalize_column_name(name)

      Denormalize the given column name.


   .. py:method:: get_column_specification(column, **kwargs)

      Get column specifications.


   .. py:method:: visit_primary_key_constraint(constraint, **kw)

      Override the primary key constraint implementation.

      NOTE: HeavyDB doesn't implement primary key


   .. py:method:: visit_foreign_key_constraint(constraint, **kw)

      Override the foreign key constraint implementation.

      NOTE: HeavyDB doesn't implement foreign key


   .. py:method:: visit_unique_constraint(constraint, **kw)

      Override the unique key constraint implementation.

      NOTE: HeavyDB doesn't implement unique key


   .. py:method:: visit_create_index(*args, **kwargs)

      Override the index constraint implementation.

      NOTE: HeavyDB doesn't implement index



.. py:class:: HeavyAITypeCompiler(dialect: sqlalchemy.engine.interfaces.Dialect)

   Bases: :py:obj:`sqlalchemy.sql.compiler.GenericTypeCompiler`

   HeavyAI Type Compiler.

   .. py:method:: visit_ARRAY(type, **kw)

      Define the ARRAY compilation.


   .. py:method:: visit_numeric(type_, **kw)

      Override the Numeric compilation.


   .. py:method:: visit_datetime(type_, **kw)

      Override the Date Time compilation.



.. py:data:: colspecs
   :type: dict

   

.. py:class:: HeavyAIDialect(pool=NullPool, **kwargs)

   Bases: :py:obj:`sqlalchemy.engine.default.DefaultDialect`

   HeavyAI Dialect.

   .. py:property:: _dialect_specific_select_one


   .. py:attribute:: name
      :value: 'heavydb'

      

   .. py:attribute:: max_identifier_length
      :value: 32768

      

   .. py:attribute:: default_paramstyle
      :value: 'pyformat'

      

   .. py:attribute:: colspecs

      

   .. py:attribute:: ischema_names

      

   .. py:attribute:: convert_unicode
      :value: True

      

   .. py:attribute:: supports_statement_cache
      :value: True

      

   .. py:attribute:: supports_unicode_statements
      :value: True

      

   .. py:attribute:: supports_unicode_binds
      :value: True

      

   .. py:attribute:: returns_unicode_strings
      :value: True

      

   .. py:attribute:: description_encoding

      

   .. py:attribute:: postfetch_lastrowid
      :value: False

      

   .. py:attribute:: supports_sane_rowcount
      :value: False

      

   .. py:attribute:: supports_sane_multi_rowcount
      :value: False

      

   .. py:attribute:: supports_native_decimal
      :value: False

      

   .. py:attribute:: supports_native_boolean
      :value: False

      

   .. py:attribute:: supports_alter
      :value: True

      

   .. py:attribute:: supports_sequences
      :value: False

      

   .. py:attribute:: supports_native_enum
      :value: False

      

   .. py:attribute:: supports_empty_insert
      :value: False

      

   .. py:attribute:: supports_default_values
      :value: False

      

   .. py:attribute:: supports_default_metavalue
      :value: False

      

   .. py:attribute:: supports_schemas
      :value: False

      

   .. py:attribute:: preparer

      

   .. py:attribute:: ddl_compiler

      

   .. py:attribute:: type_compiler

      

   .. py:attribute:: statement_compiler

      

   .. py:attribute:: execution_ctx_cls

      

   .. py:attribute:: requires_name_normalize
      :value: True

      

   .. py:method:: set_connection_execution_options(connection, opts)

      Set connection execution options.


   .. py:method:: _check_unicode_returns(connection)


   .. py:method:: do_execute(cursor, statement, parameters, context=None)

      Override the "do_execute" method.


   .. py:method:: do_rollback(connection)

      Override the rollback method.

      Note: HeavyDB hasn't transaction implemented so it cannot rollback
      changes.


   .. py:method:: create_connect_args(url)

      Create a connect arguments from given url.


   .. py:method:: has_table(connection, table_name, schema=None, **kw)

      Check if the table exists.


   .. py:method:: has_sequence(connection, sequence_name, schema=None)

      Check if the sequence exists.

      Note: HeavyDB hasnt sequence objects.


   .. py:method:: normalize_name(name)

      Normalize given name.


   .. py:method:: denormalize_name(name)

      Denormalize given name.


   .. py:method:: _denormalize_quote_join(*idents)


   .. py:method:: _map_name_to_idx(result)
      :staticmethod:


   .. py:method:: get_indexes(connection, table_name, schema=None, **kw)

      Get all indexes.

      Note: index is not supported by HeavyDB.


   .. py:method:: get_primary_keys(connection, table_name, schema=None, **kw)

      Override function that return the list of primary keys.

      Note: primary keys aren't supported by HeavyDB.


   .. py:method:: get_pk_constraint(connection, table_name, schema=None, **kw)

      Override function that return the list of constraints.

      Note: constraints aren't supported by HeavyDB.


   .. py:method:: get_unique_constraint(connection, table_name, schema=None, **kw)

      Override function that return the list of unique keys.

      Note: unique keys arent supported by HeavyDB.


   .. py:method:: get_foreign_keys(connection, table_name, schema=None, **kw)

      Override function that return the list of foreign keys.

      Note: foreign keys arent supported by HeavyDB.


   .. py:method:: get_columns(connection, table_name, schema=None, **kw)

      Get all column info given the table info.


   .. py:method:: get_schema_names(connection, **kw)

      Return all database as schemas.

      Note: Maybe it would be better to return the database we are
      connected to.


   .. py:method:: get_table_names(connection, schema=None, **kw)

      Get all table names.


   .. py:method:: get_view_names(connection, schema=None, **kw)

      Get all view names.


   .. py:method:: get_view_definition(connection, view_name, schema=None, **kw)

      Get the view definition.


   .. py:method:: get_temp_table_names(connection, schema=None, **kw)

      Override function that return the list of temporary tables name.



.. py:data:: dialect

   

.. py:data:: construct_arguments
   :value: [()]

   

