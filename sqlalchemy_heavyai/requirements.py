"""Requirements/Restrictions for the Dialect tests."""
from sqlalchemy.testing import exclusions
from sqlalchemy.testing.requirements import SuiteRequirements


class Requirements(SuiteRequirements):
    """Define dialect restrictions for the tests."""

    # constraints
    check_constraint_reflection = exclusions.closed()
    table_reflection = exclusions.closed()

    # database
    unusual_column_name_characters = exclusions.closed()

    # foreign key
    foreign_key_constraint_reflection = exclusions.closed()
    cross_schema_fk_reflection = exclusions.closed()
    self_referential_foreign_keys = exclusions.closed()

    primary_key_constraint_reflection = exclusions.closed()

    # index
    temp_table_reflect_indexes = exclusions.closed()
    index_reflection = exclusions.closed()
    index_reflects_included_columns = exclusions.closed()
    indexes_with_ascdesc = exclusions.closed()
    indexes_with_expressions = exclusions.closed()

    unique_constraint_reflection = exclusions.closed()

    independent_connections = exclusions.closed()

    # schemas = exclusions.closed()

    # unions
    parens_in_union_contained_select_w_limit_offset = exclusions.closed()
    parens_in_union_contained_select_wo_limit_offset = exclusions.closed()
    order_by_col_from_union = exclusions.closed()

    # autoincrement
    autoincrement_insert = exclusions.closed()
    autoincrement_without_sequence = exclusions.closed()

    # insert
    insert_from_select = exclusions.closed()

    # regex
    regexp_match = exclusions.closed()
    regexp_replace = exclusions.closed()

    # decimal
    implicit_decimal_binds = exclusions.closed()
    precision_generic_float_type = exclusions.closed()
    precision_numerics_general = exclusions.closed()

    # datatime
    datetime_implicit_bound = exclusions.closed()
    date_implicit_bound = exclusions.closed()

    # comment
    comment_reflection = exclusions.closed()

    # views
    view_column_reflection = exclusions.closed()

    # types
    array_type = exclusions.closed()
    uuid_data_type = exclusions.closed()

    # target database can render LIMIT and/or OFFSET with a complete
    # SQL expression, such as one that uses the addition operator.
    # parameter
    sql_expression_limit_offset = exclusions.closed()
