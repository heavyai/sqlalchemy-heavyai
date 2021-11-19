:py:mod:`sqlalchemy_omnisci`
============================

.. py:module:: sqlalchemy_omnisci

.. autoapi-nested-parse::

   OmniSci sqlalchemy dialect.



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   _version/index.rst
   base/index.rst
   provision/index.rst
   pyomnisci/index.rst
   requirements/index.rst
   util/index.rst
   version/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   sqlalchemy_omnisci.ARRAY
   sqlalchemy_omnisci.OmniSciDialect_pyomnisci



Functions
~~~~~~~~~

.. autoapisummary::

   sqlalchemy_omnisci.URL



Attributes
~~~~~~~~~~

.. autoapisummary::

   sqlalchemy_omnisci.__version__


.. py:class:: ARRAY

   Bases: :py:obj:`sqlalchemy.types.TypeEngine`

   Custom array SQL type.

   .. py:attribute:: __visit_name__
      :annotation: = ARRAY

      


.. py:class:: OmniSciDialect_pyomnisci(pool=NullPool, **kwargs)

   Bases: :py:obj:`sqlalchemy_omnisci.base.OmniSciDialect`

   OmniSciDialect for pyomnisci.

   .. py:attribute:: driver
      :annotation: = pyomnisci

      


.. py:function:: URL(**db_parameters)

   Compose a connect string from the given parameters.


.. py:data:: __version__
   

   

