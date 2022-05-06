"""HeavyAI sqlalchemy dialect."""
from sqlalchemy.dialects import registry  # noqa: F401

from . import provision  # noqa: F401
from .base import ARRAY  # noqa: F401
from .heavyai import HeavyAIDialect_heavyai  # noqa: F401
from .util import _url as URL  # noqa: F401
from .version import _version as __version__  # noqa: F401

registry.register("heavyai", "sqlalchemy_heavyai", "HeavyAIDialect_heavyai")
