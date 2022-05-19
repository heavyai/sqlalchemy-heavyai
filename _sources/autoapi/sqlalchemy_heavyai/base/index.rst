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

   sqlalchemy_heavyai.base.RESERVED_WORDS
   sqlalchemy_heavyai.base.ischema_names
   sqlalchemy_heavyai.base.AUTOCOMMIT_REGEXP
   sqlalchemy_heavyai.base.COMPOUND_KEYWORDS
   sqlalchemy_heavyai.base.colspecs
   sqlalchemy_heavyai.base.dialect
   sqlalchemy_heavyai.base.construct_arguments


.. py:data:: RESERVED_WORDS
   

   

.. py:class:: ARRAY

   Bases: :py:obj:`sqlalchemy.types.TypeEngine`

   Custom array SQL type.

   .. py:attribute:: __visit_name__
      :annotation: = ARRAY

      


.. py:class:: Boolean(create_constraint=False, name=None, _create_events=True)

   Bases: :py:obj:`sqlalchemy.types.Boolean`

   Custom Boolean type.

   .. py:method:: bind_processor(self, dialect)

      Bind processor for boolean type.



.. py:class:: BOOLEAN(create_constraint=False, name=None, _create_events=True)

   Bases: :py:obj:`Boolean`

   Custom Boolean type.

   .. py:attribute:: __visit_name__
      :annotation: = BOOLEAN

      


.. py:data:: ischema_names
   

   

.. py:data:: AUTOCOMMIT_REGEXP
   

   

.. py:data:: COMPOUND_KEYWORDS
   

   

.. py:class:: HeavyAIIdentifierPreparer(dialect, **kw)

   Bases: :py:obj:`sqlalchemy.sql.compiler.IdentifierPreparer`

   HeavyAI Identifier Preparer.

   .. py:attribute:: reserved_words
      

      

   .. py:method:: _quote_free_identifiers(self, *ids)

      Unilaterally identifier-quote any number of strings.



.. py:class:: HeavyAICompiler(dialect, statement, cache_key=None, column_keys=None, for_executemany=False, linting=NO_LINTING, **kwargs)

   Bases: :py:obj:`sqlalchemy.sql.compiler.SQLCompiler`

   SQLCompiler for HeavyAI.

   .. py:attribute:: compound_keywords
      

      

   .. py:method:: visit_true(self, expr, **kw)

      Return the value for TRUE.


   .. py:method:: visit_false(self, expr, **kw)

      Return the value for FALSE.


   .. py:method:: visit_cast(self, cast, **kwargs)

      Override the default CAST.


   .. py:method:: visit_index(self, *args, **kwargs)

      Override the default INDEX.

      HeavyDB doesn't implement INDEX yet.


   .. py:method:: visit_compound_select(self, cs, asfrom=False, compound_index=None, **kwargs)

      Override the default COMPOUND SELECT.


   .. py:method:: limit_clause(self, select, **kw)

      Override the default LIMIT CLAUSE.



.. py:class:: HeavyAIExecutionContext

   Bases: :py:obj:`sqlalchemy.engine.default.DefaultExecutionContext`

   HeavyAI Execution Context.

   .. py:method:: pre_exec(self)

      Define the pre-execution step.


   .. py:method:: should_autocommit_text(self, statement)

      Check if autocommit should be executed.


   .. py:method:: should_autocommit(self)

      Check if autocommit should be executed.



.. py:class:: HeavyAIDDLCompiler(dialect, statement, schema_translate_map=None, render_schema_translate=False, compile_kwargs=util.immutabledict())

   Bases: :py:obj:`sqlalchemy.sql.compiler.DDLCompiler`

   HeavyAIDDL Compiler.

   .. py:method:: denormalize_column_name(self, name)

      Denormalize the given column name.


   .. py:method:: get_column_specification(self, column, **kwargs)

      Get column specifications.


   .. py:method:: visit_primary_key_constraint(self, constraint, **kw)

      Override the primary key constraint implementation.

      NOTE: HeavyDB doesn't implement primary key


   .. py:method:: visit_foreign_key_constraint(self, constraint, **kw)

      Override the foreign key constraint implementation.

      NOTE: HeavyDB doesn't implement foreign key


   .. py:method:: visit_unique_constraint(self, constraint, **kw)

      Override the unique key constraint implementation.

      NOTE: HeavyDB doesn't implement unique key


   .. py:method:: visit_create_index(self, *args, **kwargs)

      Override the index constraint implementation.

      NOTE: HeavyDB doesn't implement index



.. py:class:: HeavyAITypeCompiler(dialect)

   Bases: :py:obj:`sqlalchemy.sql.compiler.GenericTypeCompiler`

   HeavyAI Type Compiler.

   .. py:method:: visit_ARRAY(selfself, type, **kw)

      Define the ARRAY compilation.


   .. py:method:: visit_numeric(self, type_, **kw)

      Override the Numeric compilation.


   .. py:method:: visit_datetime(self, type_, **kw)

      Override the Date Time compilation.



.. py:data:: colspecs
   :annotation: :dict

   

.. py:class:: HeavyAIDialect(pool=NullPool, **kwargs)

   Bases: :py:obj:`sqlalchemy.engine.default.DefaultDialect`

   HeavyAI Dialect.

   .. py:attribute:: name
      :annotation: = heavydb

      

   .. py:attribute:: max_identifier_length
      :annotation: = 32768

      

   .. py:attribute:: default_paramstyle
      :annotation: = pyformat

      

   .. py:attribute:: colspecs
      

      

   .. py:attribute:: ischema_names
      

      

   .. py:attribute:: convert_unicode
      :annotation: = True

      

   .. py:attribute:: supports_statement_cache
      :annotation: = True

      

   .. py:attribute:: supports_unicode_statements
      :annotation: = True

      

   .. py:attribute:: supports_unicode_binds
      :annotation: = True

      

   .. py:attribute:: returns_unicode_strings
      :annotation: = True

      

   .. py:attribute:: description_encoding
      

      

   .. py:attribute:: postfetch_lastrowid
      :annotation: = False

      

   .. py:attribute:: supports_sane_rowcount
      :annotation: = False

      

   .. py:attribute:: supports_sane_multi_rowcount
      :annotation: = False

      

   .. py:attribute:: supports_native_decimal
      :annotation: = True

      

   .. py:attribute:: supports_native_boolean
      :annotation: = False

      

   .. py:attribute:: supports_alter
      :annotation: = True

      

   .. py:attribute:: supports_sequences
      :annotation: = False

      

   .. py:attribute:: supports_native_enum
      :annotation: = False

      

   .. py:attribute:: supports_empty_insert
      :annotation: = False

      

   .. py:attribute:: supports_default_values
      :annotation: = False

      

   .. py:attribute:: supports_default_metavalue
      :annotation: = False

      

   .. py:attribute:: preparer
      

      

   .. py:attribute:: ddl_compiler
      

      

   .. py:attribute:: type_compiler
      

      

   .. py:attribute:: statement_compiler
      

      

   .. py:attribute:: execution_ctx_cls
      

      

   .. py:attribute:: requires_name_normalize
      :annotation: = True

      

   .. py:method:: dbapi(cls)
      :classmethod:

      Return the database api.


   .. py:method:: set_connection_execution_options(self, connection, opts)

      Set connection execution options.


   .. py:method:: _check_unicode_returns(self, connection)


   .. py:method:: _dialect_specific_select_one(self)
      :property:


   .. py:method:: do_rollback(self, connection)

      Override the rollback method.

      Note: HeavyDB hasn't transaction implemented so it cannot rollback
      changes.


   .. py:method:: create_connect_args(self, url)

      Create a connect arguments from given url.


   .. py:method:: has_table(self, connection, table_name, schema=None)

      Check if the table exists.


   .. py:method:: has_sequence(self, connection, sequence_name, schema=None)

      Check if the sequence exists.

      Note: HeavyDB hasnt sequence objects.


   .. py:method:: normalize_name(self, name)

      Normalize given name.


   .. py:method:: denormalize_name(self, name)

      Denormalize given name.


   .. py:method:: _denormalize_quote_join(self, *idents)


   .. py:method:: _map_name_to_idx(result)
      :staticmethod:


   .. py:method:: get_indexes(self, connection, table_name, schema=None, **kw)

      Get all indexes.

      Note: index is not supported by HeavyDB.


   .. py:method:: get_primary_keys(self, connection, table_name, schema=None, **kw)

      Override function that return the list of primary keys.

      Note: primary keys aren't supported by HeavyDB.


   .. py:method:: get_pk_constraint(self, connection, table_name, schema=None, **kw)

      Override function that return the list of constraints.

      Note: constraints aren't supported by HeavyDB.


   .. py:method:: get_unique_constraint(self, connection, table_name, schema=None, **kw)

      Override function that return the list of unique keys.

      Note: unique keys arent supported by HeavyDB.


   .. py:method:: get_foreign_keys(self, connection, table_name, schema=None, **kw)

      Override function that return the list of foreign keys.

      Note: foreign keys arent supported by HeavyDB.


   .. py:method:: get_columns(self, connection, table_name, schema=None, **kw)

      Get all column info given the table info.


   .. py:method:: get_schema_names(self, connection, **kw)

      Return all database as schemas.

      Note: Maybe it would be better to return the database we are
      connected to.


   .. py:method:: get_table_names(self, connection, schema=None, **kw)

      Get all table names.


   .. py:method:: get_view_names(self, connection, schema=None, **kw)

      Get all view names.


   .. py:method:: get_view_definition(self, connection, view_name, schema=None, **kw)

      Get the view definition.


   .. py:method:: get_temp_table_names(self, connection, schema=None, **kw)

      Override function that return the list of temporary tables name.



.. py:data:: dialect
   

   

.. py:data:: construct_arguments
   :annotation: = [None]

   

