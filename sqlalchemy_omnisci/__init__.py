from sqlalchemy.dialects import registry  # noqa: F401

from .base import ARRAY, OmnisciDialect  # noqa: F401
from .util import _url as URL  # noqa: F401
from .version import VERSION  # noqa: F401

registry.register("omnisci", "sqlalchemy_omnisci", "OmnisciDialect")

OMNISCI_CONNECTOR_VERSION = ".".join(chr(v) for v in VERSION[0:3])

__version__ = OMNISCI_CONNECTOR_VERSION
