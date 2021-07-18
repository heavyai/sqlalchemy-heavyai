from sqlalchemy.testing import exclusions
from sqlalchemy.testing.requirements import SuiteRequirements


class Requirements(SuiteRequirements):
    # foreign key
    foreign_key_constraint_reflection = exclusions.closed()
    cross_schema_fk_reflection = exclusions.closed()
    self_referential_foreign_keys = exclusions.closed()

    primary_key_constraint_reflection = exclusions.closed()

    # index
    index_reflection = exclusions.closed()
    temp_table_reflect_indexes = exclusions.closed()
    indexes_with_ascdesc = exclusions.closed()

    unique_constraint_reflection = exclusions.closed()

    independent_connections = exclusions.closed()

    schemas = exclusions.closed()

    # unions
    parens_in_union_contained_select_w_limit_offset = exclusions.closed()
    parens_in_union_contained_select_wo_limit_offset = exclusions.closed()
    order_by_col_from_union = exclusions.closed()
