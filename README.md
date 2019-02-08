django-pinject
==============

[![codecov.io](http://codecov.io/github/eshta/django-pinject/coverage.svg?branch=master)](http://codecov.io/github/eshta/django-pinject?branch=master)

[![Build Status](https://travis-ci.com/eshta/django-pinject.svg?branch=master)](https://travis-ci.com/eshta/django-pinject)



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
