:py:mod:`sqlalchemy_heavyai`
============================

.. py:module:: sqlalchemy_heavyai

.. autoapi-nested-parse::

   HeavyAI sqlalchemy dialect.



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   base/index.rst
   heavyai/index.rst
   provision/index.rst
   requirements/index.rst
   util/index.rst
   version/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   sqlalchemy_heavyai.ARRAY
   sqlalchemy_heavyai.HeavyAIDialect_heavyai



Functions
~~~~~~~~~

.. autoapisummary::

   sqlalchemy_heavyai.URL



Attributes
~~~~~~~~~~

.. autoapisummary::

   sqlalchemy_heavyai.__version__


.. py:class:: ARRAY

   Bases: :py:obj:`sqlalchemy.types.TypeEngine`

   Custom array SQL type.

   .. py:attribute:: __visit_name__
      :value: 'ARRAY'

      


.. py:class:: HeavyAIDialect_heavyai(pool=NullPool, **kwargs)

   Bases: :py:obj:`sqlalchemy_heavyai.base.HeavyAIDialect`

   HeavyAIDialect for heavyai.

   .. py:attribute:: driver
      :value: 'heavydb'

      

   .. py:attribute:: supports_statement_cache
      :value: True

      


.. py:function:: URL(**db_parameters)

   Compose a connect string from the given parameters.


.. py:data:: __version__

   

