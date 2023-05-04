"""Override some methods for the provision module."""
from sqlalchemy.testing.provision import temp_table_keyword_args


@temp_table_keyword_args.for_db("heavydb")
def _heavyai_temp_table_keyword_args(cfg, eng):
    return {"prefixes": ["TEMPORARY"]}
