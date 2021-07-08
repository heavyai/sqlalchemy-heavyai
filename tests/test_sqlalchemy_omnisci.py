"""
Tests for `sqlalchemy_omnisci` package.

python -c \
    "import superset; app = superset.create_app(); app.run(host='0.0.0.0')"

"""
uri = (
    "omnisci://demouser:HyperInteractive@"
    "metis.mapd.com:443/mapd?protocol=https"
)
