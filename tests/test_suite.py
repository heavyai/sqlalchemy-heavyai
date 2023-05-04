"""
Re-use the sqlalchemy test suite.

# isort:skip_file
"""
import pytest
import sqlalchemy
from packaging.version import Version

from sqlalchemy.testing.suite import *  # noqa: F403, F401
from sqlalchemy.testing.suite import (
    BinaryTest as _BinaryTest,
    CastTypeDecoratorTest as _CastTypeDecoratorTest,
    ComponentReflectionTest as _ComponentReflectionTest,
    CompoundSelectTest as _CompoundSelectTest,
    DateTimeMicrosecondsTest as _DateTimeMicrosecondsTest,
    DeprecatedCompoundSelectTest as _DeprecatedCompoundSelectTest,
    DifficultParametersTest as _DifficultParametersTest,
    ExceptionTest as _ExceptionTest,
    ExistsTest as _ExistsTest,
    ExpandingBoundInTest as _ExpandingBoundInTest,
    FetchLimitOffsetTest as _FetchLimitOffsetTest,
    HasTableTest as _HasTableTest,
    HasIndexTest as _HasIndexTest,
    IntegerTest as _IntegerTest,
    LikeFunctionsTest as _LikeFunctionsTest,
    LongNameBlowoutTest as _LongNameBlowoutTest,
    NormalizedNameTest as _NormalizedNameTest,
    NumericTest as _NumericTest,
    QuotedNameArgumentTest as _QuotedNameArgumentTest,
    TextTest as _TextTest,
    TimeTest as _TimeTest,
    TimeMicrosecondsTest as _TimeMicrosecondsTest,
    UnicodeTextTest as _UnicodeTextTest,
    UnicodeVarcharTest as _UnicodeVarcharTest,
)


is_sqlalchemy_v2 = Version(sqlalchemy.__version__).major == 2

if is_sqlalchemy_v2:
    from sqlalchemy.testing.suite import (
        TrueDivTest as _TrueDivTest,
    )


pytest.mark.skip(_ComponentReflectionTest)
pytest.mark.skip(_HasIndexTest)
pytest.mark.skip(_QuotedNameArgumentTest)


class FetchLimitOffsetTest(_FetchLimitOffsetTest):
    """Skip tests for ExpandingBoundInTest."""

    @pytest.mark.skip()
    def test_limit_render_multiple_times(self, *args, **kwargs):
        """Skip test."""
        assert True


class UnicodeTextTest(_UnicodeTextTest):
    """Skip tests for ExpandingBoundInTest."""

    @pytest.mark.skip()
    def test_empty_strings_text(self, *args, **kwargs):
        """Skip test."""
        assert True

    if not is_sqlalchemy_v2:

        @pytest.mark.skip()
        def test_literal(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_literal_non_ascii(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_null_strings_text(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_round_trip(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_round_trip_executemany(self, *args, **kwargs):
            """Skip test."""
            assert True


class UnicodeVarcharTest(_UnicodeVarcharTest):
    """Skip tests for ExpandingBoundInTest."""

    @pytest.mark.skip()
    def test_empty_strings_varchar(self, *args, **kwargs):
        """Skip test."""
        assert True

    if not is_sqlalchemy_v2:

        @pytest.mark.skip()
        def test_literal(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_literal_non_ascii(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_round_trip(self, *args, **kwargs):
            """Skip test."""
            assert True

        @pytest.mark.skip()
        def test_round_trip_executemany(self, *args, **kwargs):
            """Skip test."""
            assert True


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


class IntegerTest(_IntegerTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_huge_int_auto_accommodation(self, *args, **kwargs):
        """Skip test."""
        return


class DateTimeMicrosecondsTest(_DateTimeMicrosecondsTest):
    """Skip test."""

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
    def test_standalone_bindparam_escape(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_standalone_bindparam_escape_expanding(self, *args, **kwargs):
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

    @pytest.mark.skip()
    def test_select_direct(self, *args, **kwargs):
        """Skip test."""
        return


class TimeTest(_TimeTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_select_direct(self, *args, **kwargs):
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
    def test_enotation_decimal_large(self, *args, **kwargs):
        """Skip test."""
        return


class TextTest(_TextTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_text_empty_strings(self, *args, **kwargs):
        """Skip test."""
        return


class BinaryTest(_BinaryTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_binary_roundtrip(self, *args, **kwargs):
        """Skip test."""
        return

    @pytest.mark.skip()
    def test_pickle_roundtrip(self, *args, **kwargs):
        """Skip test."""
        return


class HasTableTest(_HasTableTest):
    """Skip test."""

    @pytest.mark.skip()
    def test_has_table_cache(self, *args, **kwargs):
        """Skip test."""
        return


if is_sqlalchemy_v2:

    class TrueDivTest(_TrueDivTest):
        """Skip test."""

        @pytest.mark.skip()
        def test_truediv_float(self, *args, **kwargs):
            """Skip test."""
            return

        @pytest.mark.skip()
        def test_truediv_integer(self, *args, **kwargs):
            """Skip test."""
            return

        @pytest.mark.skip()
        def test_truediv_integer_bound(self, *args, **kwargs):
            """Skip test."""
            return
