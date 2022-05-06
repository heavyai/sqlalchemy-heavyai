"""Test compiler from expressions to SQL statement."""
import pytest
from sqlalchemy import func, select
from sqlalchemy.sql import column, quoted_name, table
from sqlalchemy.testing import AssertsCompiledSQL, fixtures


class _TestCompilerHeavyai(fixtures.TestBase, AssertsCompiledSQL):
    __dialect__ = "heavyai"


class TestCompilerSelect(_TestCompilerHeavyai):
    """Test compiler for select statement."""

    def test_select_datatype_table(self, table_datatype):
        """Test compilation for different datatypes."""
        stmt = table_datatype.select().where(table_datatype.c._int == 1)
        self.assert_compile(
            stmt,
            (
                "SELECT table_datatype._bigint, table_datatype._bool, "
                "table_datatype._date, table_datatype._datetime, "
                "table_datatype._float, table_datatype._int, "
                "table_datatype._smallint, table_datatype._string "
                "FROM table_datatype "
                "WHERE table_datatype._int = %(int_1)s"
            ),
            dialect="heavyai",
        )

    @pytest.mark.parametrize(
        "sql_func",
        [
            "avg",
            "sum",
            "count",
            "max",
            "min",
            "corr",
            "covar",
            "sample",
            "stddev",
        ],
    )
    def test_select_datatype_table_avg(self, table_datatype, sql_func):
        """Test compilation for average function."""
        expr = getattr(func, sql_func)(table_datatype.c._int)
        stmt = select(expr)

        self.assert_compile(
            stmt,
            (
                f"SELECT {sql_func}(table_datatype._int) AS {sql_func}_1 "
                "FROM table_datatype"
            ),
            dialect="heavyai",
        )

    def test_quoted_name_label(self):
        """Test quoted name label."""
        test_cases = [
            # quote name
            {
                "label": quoted_name("alias", True),
                "output": (
                    'SELECT colname AS "alias" \nFROM abc GROUP BY colname'
                ),
            },
            # not quote label
            {
                "label": "alias",
                "output": (
                    "SELECT colname AS alias \nFROM abc GROUP BY colname"
                ),
            },
            # not quote mixed case label
            {
                "label": "Alias",
                "output": (
                    'SELECT colname AS "Alias" \nFROM abc GROUP BY colname'
                ),
            },
        ]

        for t in test_cases:
            col = column("colname").label(t["label"])
            sel_from_tbl = (
                select([col]).group_by(col).select_from(table("abc"))
            )
            compiled_result = sel_from_tbl.compile()
            assert str(compiled_result) == t["output"]


class TestCompilerDelete(_TestCompilerHeavyai):
    """Compilation test for delete statement."""

    def test_table_delete(self, table1):
        """Test compilation for delete statement."""
        stmt = table1.delete().where(table1.c.id == 1)
        self.assert_compile(
            stmt,
            "DELETE FROM table1 WHERE table1.id = %(id_1)s",
            dialect="heavyai",
        )


class TestCompilerUpdate(_TestCompilerHeavyai):
    """Compilation test for update statement."""

    def test_table_update(self, table1):
        """Test compilation for update statement."""
        stmt = table1.update().values(name="name1").where(table1.c.name == 1)
        self.assert_compile(
            stmt,
            "UPDATE table1 SET name=%(name)s "
            "WHERE table1.name = %(name_1)s",
            dialect="heavyai",
        )
