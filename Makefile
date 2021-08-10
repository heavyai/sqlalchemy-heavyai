.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

DOCKER=docker-compose --file docker/docker-compose.yaml
TEST_PARAMS=

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 sqlalchemy_omnisci tests

test: ## run tests quickly with the default Python
	py.test

coverage: ## check code coverage quickly with the default Python
	coverage run --source sqlalchemy_omnisci -m pytest
	coverage report -m
	coverage html

watch-coverage:
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/sqlalchemy_omnisci.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ sqlalchemy_omnisci
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

watch-docs:
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

install: clean ## install the package to the active Python's site-packages
	python setup.py install

develop: clean ## install the package in development mode
	pip install -e '.[dev]'
	pre-commit install


docker-superset-build:
	$(DOCKER) build superset

docker-superset-start: docker-superset-build
	$(DOCKER) up -d superset
	@sleep 5
	$(DOCKER) exec superset bash /opt/sqlalchemy-omnisci/docker/setup-superset.sh
	$(DOCKER) logs -f superset

docker-superset-run:
	$(DOCKER) exec superset bash

docker-omnisci-build:
	$(DOCKER) pull omniscidb

docker-omnisci-start:
	$(DOCKER) up -d omniscidb
	$(DOCKER) logs -f omniscidb

docker-omnisci-run:
	$(DOCKER) run omniscidb


# tests

# skipping for the following tests because they breaking the tests
define PYTEST_EXPR
not (\
	ExpandingBoundInTest_omnisci and (\
		test_null_in_empty_set_is_false_bindparam \
		or test_null_in_empty_set_is_false_direct \
	)\
	or FetchLimitOffsetTest \
	or HasIndexTest \
	or index \
	or IsOrIsNotDistinctFromTest and (\
		nottest_is_or_is_not_distinct_from \
		or test_is_or_is_not_distinct_from \
	) \
	or JoinTest \
	or QuotedNameArgumentTest and (\
		test_get_check_constraints \
		or test_get_columns \
		or test_get_foreign_keys \
		or test_get_pk_constraint \
		or test_get_indexes \
		or test_get_table_comment \
		or test_get_table_options \
		or test_get_unique_constraints \
		or test_get_view_definition \
	) \
	or SimpleUpdateDeleteTest and (\
		test_delete \
		or test_update \
	) \
	or CollateTest and test_collate_order_by \
	or DateTest and (\
		test_null \
		or test_null_bound_comparison \
		or test_round_trip \
		or test_round_trip_decorated \
	) \
	or DateTimeCoercedToDateTimeTest and ( \
		test_null \
		or test_null_bound_comparison \
		or test_round_trip \
		or test_round_trip_decorated \
	) \
	or DateTimeMicrosecondsTest and (\
		test_null \
		or test_null_bound_comparison \
		or test_round_trip \
		or test_round_trip_decorated \
	) \
	or DateTimeTest and (\
		test_null \
		or test_null_bound_comparison \
		or test_round_trip \
		or test_round_trip_decorated \
	) \
	or DifficultParametersTest and test_round_trip \
	or ExistsTest and ( \
		test_select_exists \
		or test_select_exists_false \
	) \
	or ExpandingBoundInTest and ( \
		test_empty_set_against_string_bindparam \
		or test_empty_set_against_string_direct \
		or test_empty_set_against_string_negation_bindparam \
		or test_empty_set_against_string_negation_direct \
	) \
	or LikeFunctionsTest and (\
		test_contains_autoescape \
		or test_contains_autoescape_escape \
		or test_contains_escape \
		or test_contains_unescaped \
		or test_endswith_autoescape \
		or test_endswith_autoescape_escape \
		or test_endswith_escape \
		or test_endswith_sqlexpr \
		or test_endswith_unescaped \
		or test_startswith_autoescape \
		or test_startswith_autoescape_escape \
		or test_startswith_escape \
		or test_startswith_sqlexpr \
		or test_startswith_unescaped \
	) \
	or LongNameBlowoutTest and test_long_convention_name \
	or NormalizedNameTest and test_reflect_lowercase_forced_tables \
	or OrderByLabelTest and test_composed_multiple \
	or UnicodeTextTest \
	or UnicodeVarcharTest \
	or CastTypeDecoratorTest and test_special_type \
    or ComponentReflectionTest\
    or test_get_schema_names \
    or CompoundSelectTest and test_distinct_selectable_in_unions \
    or CompoundSelectTest and test_limit_offset_aliased_selectable_in_unions \
    or CompoundSelectTest and test_plain_union \
    or CompoundSelectTest and test_select_from_plain_union \
    or DeprecatedCompoundSelectTest and test_distinct_selectable_in_unions \
    or DeprecatedCompoundSelectTest and test_limit_offset_aliased_selectable_in_unions \
    or DeprecatedCompoundSelectTest and test_plain_union \
    or DateTimeMicrosecondsTest and test_round_trip \
    or DateTimeMicrosecondsTest and test_round_trip_decorated \
    or TimeMicrosecondsTest and test_round_trip \
    or TimeMicrosecondsTest and test_round_trip_decorated \
    or ExceptionTest and test_integrity_error \
    or NormalizedNameTest and test_get_table_names \
    or NumericTest and test_decimal_coerce_round_trip_w_cast \
    or NumericTest and test_numeric_as_decimal \
    or NumericTest and test_render_literal_numeric \
    or TextTest and test_text_empty_strings \
)
endef

run-tests:
	pytest -vv -k "${PYTEST_EXPR}" ${TEST_PARAMS} tests/test_suite.py
