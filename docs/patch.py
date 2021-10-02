"""Patch to fix issues with jupyter-book."""
# https://github.com/napari/magicgui/pull/286/files
from pathlib import Path

from sphinx_jupyterbook_latex import transforms

text = Path(transforms.__file__).read_text()
text = text.replace('tocnode.attributes["hidden"]', 'tocnode.attributes.get("hidden")')
Path(transforms.__file__).write_text(text)
