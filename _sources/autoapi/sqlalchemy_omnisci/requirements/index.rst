:py:mod:`sqlalchemy_omnisci.requirements`
=========================================

.. py:module:: sqlalchemy_omnisci.requirements

.. autoapi-nested-parse::

   Requirements/Restrictions for the Dialect tests.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   sqlalchemy_omnisci.requirements.Requirements




.. py:class:: Requirements

   Bases: :py:obj:`sqlalchemy.testing.requirements.SuiteRequirements`

   Define dialect restrictions for the tests.

   .. py:attribute:: check_constraint_reflection
      

      

   .. py:attribute:: foreign_key_constraint_reflection
      

      

   .. py:attribute:: cross_schema_fk_reflection
      

      

   .. py:attribute:: self_referential_foreign_keys
      

      

   .. py:attribute:: primary_key_constraint_reflection
      

      

   .. py:attribute:: temp_table_reflect_indexes
      

      

   .. py:attribute:: index_reflection
      

      

   .. py:attribute:: index_reflects_included_columns
      

      

   .. py:attribute:: indexes_with_ascdesc
      

      

   .. py:attribute:: indexes_with_expressions
      

      

   .. py:attribute:: unique_constraint_reflection
      

      

   .. py:attribute:: independent_connections
      

      

   .. py:attribute:: schemas
      

      

   .. py:attribute:: parens_in_union_contained_select_w_limit_offset
      

      

   .. py:attribute:: parens_in_union_contained_select_wo_limit_offset
      

      

   .. py:attribute:: order_by_col_from_union
      

      

   .. py:attribute:: autoincrement_insert
      

      

   .. py:attribute:: autoincrement_without_sequence
      

      

   .. py:attribute:: insert_from_select
      

      

   .. py:attribute:: regexp_match
      

      

   .. py:attribute:: regexp_replace
      

      

   .. py:attribute:: implicit_decimal_binds
      

      

   .. py:attribute:: precision_generic_float_type
      

      

   .. py:attribute:: precision_numerics_general
      

      

   .. py:attribute:: comment_reflection
      

      

   .. py:attribute:: view_column_reflection
      

      


