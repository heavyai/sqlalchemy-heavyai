"""
Re-use the sqlalchemy test suite.

# isort:skip_file
"""
import pytest

from sqlalchemy.testing.suite import *  # noqa: F403, F401
from sqlalchemy.testing.suite import (
    CastTypeDecoratorTest as _CastTypeDecoratorTest,
    CollateTest as _CollateTest,
    ComponentReflectionTest as _ComponentReflectionTest,
    CompoundSelectTest as _CompoundSelectTest,
    DateTest as _DateTest,
    DateTimeCoercedToDateTimeTest as _DateTimeCoercedToDateTimeTest,
    DateTimeMicrosecondsTest as _DateTimeMicrosecondsTest,
    DateTimeTest as _DateTimeTest,
    DeprecatedCompoundSelectTest as _DeprecatedCompoundSelectTest,
    DifficultParametersTest as _DifficultParametersTest,
    ExceptionTest as _ExceptionTest,
    ExistsTest as _ExistsTest,
    ExpandingBoundInTest as _ExpandingBoundInTest,
    FetchLimitOffsetTest as _FetchLimitOffsetTest,
    HasIndexTest as _HasIndexTest,
    IsOrIsNotDistinctFromTest as _IsOrIsNotDistinctFromTest,
    JoinTest as _JoinTest,
    LikeFunctionsTest as _LikeFunctionsTest,
    LongNameBlowoutTest as _LongNameBlowoutTest,
    NormalizedNameTest as _NormalizedNameTest,
    NumericTest as _NumericTest,
    OrderByLabelTest as _OrderByLabelTest,
    QuotedNameArgumentTest as _QuotedNameArgumentTest,
    SimpleUpdateDeleteTest as _SimpleUpdateDeleteTest,
    TextTest as _TextTest,
    TimeMicrosecondsTest as _TimeMicrosecondsTest,
    UnicodeTextTest as _UnicodeTextTest,
    UnicodeVarcharTest as _UnicodeVarcharTest,
)


pytest.mark.skip(_UnicodeTextTest)
pytest.mark.skip(_UnicodeVarcharTest)
pytest.mark.skip(_ComponentReflectionTest)
pytest.mark.skip(_JoinTest)
pytest.mark.skip(_FetchLimitOffsetTest)
pytest.mark.skip(_HasIndexTest)


class ExpandingBoundInTest(_ExpandingBoundInTest):
    """Skip tests for ExpandingBoundInTest."""

    @pytest.mark.skip()
    def test_null_in_empty_set_is_false_bindparam(self, *args, **kwargs):
        """Skip test."""
        assert True

    @pytest.mark.skip()
    def test_null_in_empty_set_is_false_direct(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_empty_set_against_string_bindparam(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_empty_set_against_string_direct(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_empty_set_against_string_negation_bindparam(
        self, *args, **kwargs
    ):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_empty_set_against_string_negation_direct(self, *args, **kwargs):
        """Skip test."""
        return


class IsOrIsNotDistinctFromTest(_IsOrIsNotDistinctFromTest):
    """Skip test."""

    @pytest.mark.skip()
    def nottest_is_or_is_not_distinct_from(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_is_or_is_not_distinct_from(self, *args, **kwargs):
        """Skip test."""
        return


class QuotedNameArgumentTest(_QuotedNameArgumentTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_get_check_constraints(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_columns(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_foreign_keys(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_pk_constraint(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_indexes(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_table_comment(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_table_options(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_unique_constraints(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_view_definition(self, *args, **kwargs):
        """Skip test."""
        return


class SimpleUpdateDeleteTest(_SimpleUpdateDeleteTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_delete(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_update(self, *args, **kwargs):
        """Skip test."""
        return


class CollateTest(_CollateTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_collate_order_by(self, *args, **kwargs):
        """Skip test."""
        return


class DateTest(_DateTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_null(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_null_bound_comparison(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip_decorated(self, *args, **kwargs):
        """Skip test."""
        return


class DateTimeCoercedToDateTimeTest(_DateTimeCoercedToDateTimeTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_null(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_null_bound_comparison(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip_decorated(self, *args, **kwargs):
        """Skip test."""
        return


class DateTimeMicrosecondsTest(_DateTimeMicrosecondsTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_null(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_null_bound_comparison(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip_decorated(self, *args, **kwargs):
        """Skip test."""
        return


class DateTimeTest(_DateTimeTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_null(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_null_bound_comparison(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip_decorated(self, *args, **kwargs):
        """Skip test."""
        return


class DifficultParametersTest(_DifficultParametersTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_round_trip(self, *args, **kwargs):
        """Skip test."""
        return


class ExistsTest(_ExistsTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_select_exists(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_select_exists_false(self, *args, **kwargs):
        """Skip test."""
        return


class LikeFunctionsTest(_LikeFunctionsTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_contains_autoescape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_contains_autoescape_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_contains_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_contains_unescaped(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_endswith_autoescape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_endswith_autoescape_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_endswith_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_endswith_sqlexpr(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_endswith_unescaped(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_startswith_autoescape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_startswith_autoescape_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_startswith_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_startswith_sqlexpr(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_startswith_unescaped(self, *args, **kwargs):
        """Skip test."""
        return


class LongNameBlowoutTest(_LongNameBlowoutTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_long_convention_name(self, *args, **kwargs):
        """Skip test."""
        return


class NormalizedNameTest(_NormalizedNameTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_reflect_lowercase_forced_tables(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_get_table_names(self, *args, **kwargs):
        """Skip test."""
        return


class OrderByLabelTest(_OrderByLabelTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_composed_multiple(self, *args, **kwargs):
        """Skip test."""
        return


class CastTypeDecoratorTest(_CastTypeDecoratorTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_special_type(self, *args, **kwargs):
        """Skip test."""
        return


class CompoundSelectTest(_CompoundSelectTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_distinct_selectable_in_unions(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_limit_offset_aliased_selectable_in_unions(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_plain_union(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_select_from_plain_union(self, *args, **kwargs):
        """Skip test."""
        return


class DeprecatedCompoundSelectTest(_DeprecatedCompoundSelectTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_distinct_selectable_in_unions(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_limit_offset_aliased_selectable_in_unions(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_plain_union(self, *args, **kwargs):
        """Skip test."""
        return


class TimeMicrosecondsTest(_TimeMicrosecondsTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_round_trip(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_round_trip_decorated(self, *args, **kwargs):
        """Skip test."""
        return


class ExceptionTest(_ExceptionTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_integrity_error(self, *args, **kwargs):
        """Skip test."""
        return


class NumericTest(_NumericTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_decimal_coerce_round_trip_w_cast(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_numeric_as_decimal(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_render_literal_numeric(self, *args, **kwargs):
        """Skip test."""
        return


class TextTest(_TextTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_text_empty_strings(self, *args, **kwargs):
        """Skip test."""
        return
