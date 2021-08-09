"""Util functions used by OmniSci Dialect."""
from urllib.parse import quote_plus


def IS_STR(v):
    """Check if the given parameter is an instance of ``str``."""
    return isinstance(v, str)


def _url(**db_parameters):
    """Compose a connect string from the given parameters."""

    def sep(is_first):
        """Return the appropiated separator."""
        return "?" if is_first else "&"

    specified_parameters = []

    ret = "omnisci://{user}:{password}@{host}:{port}/".format(
        user=db_parameters["user"],
        password=quote_plus(db_parameters["password"]),
        host=db_parameters["host"],
        port=db_parameters["port"] if "port" in db_parameters else 6274,
    )
    specified_parameters += ["user", "password", "host", "port"]

    if "database" in db_parameters:
        ret += quote_plus(db_parameters["database"])
        specified_parameters += ["database"]

    is_first_parameter = True
    for p in sorted(db_parameters.keys()):
        v = db_parameters[p]
        if p not in specified_parameters:
            encoded_value = quote_plus(v) if IS_STR(v) else str(v)
            ret += sep(is_first_parameter) + p + "=" + encoded_value
            is_first_parameter = False

    return ret
