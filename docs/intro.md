# SQLAlchemy HeavyAI

HeavyAI SQLAlchemy Driver

The code here was initially developed and published at
https://community.heavy.ai/t/apache-superset-and-sql-alchemy-usage-with-omniscidb/2633

This SQLAlchemy dialect is still in **beta** version.


## Installation

### Stable release
--------------

To install SQLAlchemy HeavyAI, run this command in your terminal:

```bash
$ conda install sqlalchemy-heavyai
```

or

```bash
$ pip install sqlalchemy-heavyai
```

These are the preferred methods to install SQLAlchemy HeavyAI,
as it will always install the most recent stable release.

If you don't have conda installed, check its
[documenation page](https://docs.conda.io/en/latest/miniconda.html).

If you don't have [pip](https://pip.pypa.io) installed, this [Python
installation
guide](http://docs.python-guide.org/en/latest/starting/installation/)
can guide you through the process.

### From sources

The sources for SQLAlchemy HeavyAI can be downloaded from the [Github
repo](https://github.com/heavyai/sqlalchemy-heavyai).

You can either clone the public repository:

```bash
$ git clone git://github.com/heavyai/sqlalchemy-heavyai
```

Or download the
[tarball](https://github.com/heavyai/sqlalchemy-heavyai/tarball/master):

```bash
$ curl  -OL https://github.com/heavyai/sqlalchemy-heavyai/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
$ python -m pip install .
```

For information about development, check the
{contributing page}`../CONTRIBUTING`

## Usage

To use SQLAlchemy HeavyAI to connect to a local HeavyDB server:

```python
from sqlalchemy import create_engine

# uri: heavydb://<user>:<pass>@<host>:<port>/<db>?protocol=<protocol>
engine = create_engine(
    "heavydb://admin:HyperInteractive@"
    "localhost:6274/heavyai?protocol=binary"
)
con = engine.connect()
con.close()
```
