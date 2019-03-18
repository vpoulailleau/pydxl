================
Python Dynamixel
================

Python package to use Dynamixel servos through a serial interface (unofficial, easier SDK).

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

.. image:: https://api.codeclimate.com/v1/badges/23eb1c39f33578ee3304/maintainability
        :target: https://codeclimate.com/github/vpoulailleau/pydxl/maintainability
        :alt: Maintainability

.. image:: https://bettercodehub.com/edge/badge/vpoulailleau/pydxl?branch=master
        :target: https://bettercodehub.com/results/vpoulailleau/pydxl
        :alt: Maintainability

Post-creation
-------------

  * read the docs

    * ça a buggé, j'ai créé le projet à la main, et ensuite tout a fonctionné

  * pepy.tech

Documentation
-------------

The full documentation can be read at https://pydxl.readthedocs.io.

Example code:

.. code:: python

    import time

    from pydxl import Mx28, SerialLink

    link = SerialLink(
        device="/dev/ttyUSB0", baudrate=1_000_000, protocol_version=1.0
    )

    servo = Mx28(identifier=1, serial_link=link)
    servo.ping()
    servo.led = True

    servo.torque_enable = True
    servo.goal_position = 2000
    print(servo.goal_position)
    time.sleep(3)
    servo.goal_position = 1500
    time.sleep(3)
    servo.torque_enable = False

    link.close()

Features
--------

* Use protocol 1.0 through a serial link, known to work with:

  * U2D2

* Support servos:

  * MX-28

* TODO: implement protocol 2.0
* TODO: add more servo types

License
-------

BSD 3-Clause license, feel free to contribute: https://pydxl.readthedocs.io/en/latest/contributing.html.

