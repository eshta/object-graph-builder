object-graph-builder
====================

.. image:: https://img.shields.io/pypi/v/object-graph-builder.svg
   :target: https://pypi.org/project/object-graph-builder/
   :alt: Latest Version

.. image:: https://coveralls.io/repos/github/eshta/object-graph-builder/badge.svg
   :target: https://coveralls.io/github/eshta/object-graph-builder
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/object-graph-builder/badge/?version=latest
   :target: https://object-graph-builder.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/eshta/object-graph-builder.svg?branch=master
   :target: https://travis-ci.org/eshta/object-graph-builder



Provides a multi-step dependency injection container builder to allow adding/recreating object graphs in different stages through an app life-cycle

Features
--------

* Offering a container builder, so one can dynamically build the object graph with many apps adding their specs, classes, modules
* Dependency Injection Container (`pinject <https://github.com/google/pinject>`_)


Requirements
------------

* Python 3.6+

.. include:: docs/usage.rst

Prepare for development
-----------------------

A Python 3.6+ interpreter is required in addition to pipenv.

.. code-block:: bash

    $ make init


Now you're ready to run the tests:

.. code-block:: bash

    $ make test


Resources
---------

* `Documentation <https://object-graph-builder.readthedocs.io>`_
* `Bug Tracker <https://github.com/eshta/object-graph-builder/issues>`_
* `Code <https://github.com/eshta/object-graph-builder/>`_
