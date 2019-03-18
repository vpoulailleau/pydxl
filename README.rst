================
Python Dynamixel
================

Python package to use Dynamixel servos through a serial interface.

.. image:: https://img.shields.io/pypi/v/pydxl.svg
        :target: https://pypi.python.org/pypi/pydxl

.. image:: https://img.shields.io/pypi/l/pydxl.svg
        :target: https://github.com/vpoulailleau/pydxl/blob/master/LICENSE

.. image:: https://travis-ci.com/vpoulailleau/pydxl.svg?branch=master
        :target: https://travis-ci.com/vpoulailleau/pydxl

.. image:: https://readthedocs.org/projects/pydxls/badge/?version=latest
        :target: https://pydxl.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pepy.tech/badge/pydxl
        :target: https://pepy.tech/project/pydxl
        :alt: Downloads

.. image:: https://coveralls.io/repos/github/vpoulailleau/pydxl/badge.svg?branch=HEAD
        :target: https://coveralls.io/github/vpoulailleau/pydxl?branch=HEAD
        :alt: Coverage Status

.. image:: https://api.codeclimate.com/v1/badges/REPLACEME/maintainability
        :target: https://codeclimate.com/github/vpoulailleau/pydxl/maintainability
        :alt: Maintainability

.. image:: https://bettercodehub.com/edge/badge/vpoulailleau/pydxl?branch=master
        :target: https://bettercodehub.com/results/vpoulailleau/pydxl
        :alt: Maintainability

Post-creation
-------------

  * créer un environnement virtuel et installer les packages

    * python3 -m venv venv
    * source ven/bin/activate
    * *C'est important pour la suite*

  * read the docs

    * ça a buggé, j'ai créé le projet à la main, et ensuite tout a fonctionné

  * PyPI

    * attention au nommage de version
    * faut juste faire un upload : make release

  * code climate

    * dans les settings du projet, configurer pour les commentaires de pull requests
    * pour le test coverage, trouver l'ID à coller dans la config de travis

  * travis

    * pour avoir le code pour le badge, il faut cliquer sur le badge dans le dashboard

  * coveralls

    * changer le repo_token dans .coveralls.yml
    * changer la conf de tox pour utiliser coveralls (cf simplelogging ou python dev tools)

  * pepy.tech
  * dependabot
  * readme.rst

    * mettre les bons badges
    
  * mettre dans github les tags de projets

Documentation
-------------

The full documentation can be read at https://pydxl.readthedocs.io.

Features
--------

* TODO

License
-------

BSD 3-Clause license, feel free to contribute: https://pydxl.readthedocs.io/en/latest/contributing.html.

