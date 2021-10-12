# SQLAlchemy OmniSci

OmniSci SQLAlchemy Driver

The code here was initially developed and published at
https://community.omnisci.com/t/apache-superset-and-sql-alchemy-usage-with-omniscidb/2633

This SQLAlchemy dialect is still in **beta** version.


## Installation

### Stable release
--------------

To install SQLAlchemy OmniSci, run this command in your terminal:

```bash
$ conda install sqlalchemy-omnisci
```

or

```bash
$ pip install sqlalchemy-omnisci
```

These are the preferred methods to install SQLAlchemy OmniSci,
as it will always install the most recent stable release.

If you don't have conda installed, check its
[documenation page](https://docs.conda.io/en/latest/miniconda.html).

If you don't have [pip](https://pip.pypa.io) installed, this [Python
installation
guide](http://docs.python-guide.org/en/latest/starting/installation/)
can guide you through the process.

### From sources

The sources for SQLAlchemy OmniSci can be downloaded from the [Github
repo](https://github.com/omnisci/sqlalchemy-omnisci).

You can either clone the public repository:

```bash
$ git clone git://github.com/omnisci/sqlalchemy-omnisci
```

Or download the
[tarball](https://github.com/omnisci/sqlalchemy-omnisci/tarball/master):

```bash
$ curl  -OL https://github.com/omnisci/sqlalchemy-omnisci/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
$ python setup.py install
```

For information about development, check the
{contributing page}`./contributing`

## Usage

To use SQLAlchemy OmniSci to connect to a local OmniSci server:

```python
from sqlalchemy import create_engine

# uri: omnisci://<user>:<pass>@<host>:<port>/<db>?protocol=<protocol>
engine = create_engine(
    "omnisci://admin:HyperInteractive@"
    "localhost:6274/omnisci?protocol=binary"
)
con = engine.connect()
con.close()
```
