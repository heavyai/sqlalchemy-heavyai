#!/usr/bin/env bash

# Setup your local admin account
superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@superset.com \
    --password admin

# Migrate local DB to latest
superset db upgrade

# Load Examples
superset load_examples

# Setup roles
superset init

# install sqlalchemy
sudo -E pip install -e /opt/sqlalchemy-heavyai

# copy sqlalchemy engine to db_engine_spces folder
cp /opt/sqlalchemy-heavyai/docker/superset-heavyai.py \
  /app/superset/db_engine_specs/heavyai.py
