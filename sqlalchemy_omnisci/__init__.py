"""OmniSci sqlalchemy dialect."""
from sqlalchemy.dialects import registry  # noqa: F401

from . import provision  # noqa: F401
from .base import ARRAY  # noqa: F401
from .pyomnisci import OmniSciDialect_pyomnisci  # noqa: F401
from .util import _url as URL  # noqa: F401
from .version import VERSION  # noqa: F401

registry.register("omnisci", "sqlalchemy_omnisci", "OmniSciDialect_pyomnisci")

__version__ = ".".join(str(v) for v in VERSION[0:3])
