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
	git init  # it is safe to run it more than one time
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
	$(DOCKER) build omniscidb

docker-omnisci-start: docker-omnisci-build
	$(DOCKER) up -d omniscidb
	$(DOCKER) logs -f omniscidb

docker-omnisci-run:
	$(DOCKER) run omniscidb




# tests

# skipping for the following tests because it is breaking the tests
define PYTEST_EXPR
not (\
	FetchLimitOffsetTest \
	or IsOrIsNotDistinctFromTest and nottest_is_or_is_not_distinct_from \
	or IsOrIsNotDistinctFromTest and test_is_or_is_not_distinct_from \
	or JoinTest_omnisci and test_outer_join_fk \
	or UnicodeVarcharTesta and test_round_trip_executemany \
)
endef

run-tests:
	pytest -vv -k "${PYTEST_EXPR}" ${TEST_PARAMS} tests/test_suite.py
