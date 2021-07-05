# SQLAlchemy

OmniSci SQLAlchemy Driver

This repository is based on https://community.omnisci.com/t/apache-superset-and-sql-alchemy-usage-with-omniscidb/2633

### Tests

#### With Apache Superset

Start an Apache Superset instance with all customization needed to run the
examples and to run sqlachemy-omnisci.

More information: https://hub.docker.com/r/apache/superset


#### Known Errors

1. apache-arrow conflict:

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.

apache-superset 0.999.0.dev0 requires pyarrow<4.1,>=4.0.1, but you have pyarrow 3.0.0 which is incompatible.
Successfully installed llvmlite-0.36.0 netifaces-0.11.0 numba-0.53.1 ply-3.11 pyarrow-3.0.0 pyomnisci-0.27.0 pyomniscidb-5.5.2 rbc-project-0.2.2 shapely-1.7.1 sqlalchemy-omnisci tblib-1.7.0 thriftpy2-0.4.14
```
