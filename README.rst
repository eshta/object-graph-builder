django-pinject
==============

.. image:: https://img.shields.io/pypi/v/django-pinject.svg
   :target: https://pypi.org/project/django-pinject/
   :alt: Latest Version

.. image:: https://coveralls.io/repos/github/eshta/django-pinject/badge.svg
   :target: https://coveralls.io/github/eshta/django-pinject
   :alt: Coverage Status

.. image:: https://readthedocs.org/projects/django-pinject/badge/?version=latest
   :target: https://django-pinject.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.org/eshta/django-pinject.svg?branch=master
   :target: https://travis-ci.org/eshta/django-pinject



This simplifies pinject (dependency injection container) integration into django


Features
--------

* Offering a builder so you can dynamically build the object graph with many apps adding their specs, classes, modules
* Dependency Injection Container (pinject)[https://github.com/google/pinject]


Requirements
------------

django-pinject supports Python 3.6+

Prepare for development
-----------------------

A Python 3.5+ interpreter is required in addition to pipenv.



    $ pipenv install --python 3.6 --dev
    $ pipenv shell
    $ pip install -e .


Now you're ready to run the tests:



    $ make test


Resources
---------

* `Documentation <https://django-pinject.readthedocs.io>`_
* `Bug Tracker <https://github.com/eshta/django-pinject/issues>`_
* `Code <https://github.com/eshta/django-pinject/>`_
