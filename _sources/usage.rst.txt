=====
Usage
=====

To use SQLAlchemy OmniSci to connect to a local OmniSci server::

    from sqlalchemy import create_engine

    # uri: omnisci://<user>:<pass>@<host>:<port>/<db>?protocol=<protocol>
    engine = create_engine(
        "omnisci://admin:HyperInteractive@"
        "localhost:6274/omnisci?protocol=binary"
    )
