====================
Project Organization
====================

Project organization is strictly enforced by framework. Projects consist of three main parts:

* A project folder in the root directory of CIRCUITPY. The folder name is the name of your project, eg. 'my_app'

* A configurations file that has the same name as the project folder and is in the project folder. It must be a Python (.py or .mpy) file.

* An application file that has the same name as the project folder and is in the project folder. It must be a Python (.py or .mpy) file.

Optionally there may be other files in the project folder, eg. data files, fonts, etc. framework will only look in a specified folder for the configurations file and application file and ignore all else.

A minimal example:

::

CIRCUITPY
|-- code.py
|-- lib
|-- my_app
|---- conf.py
|---- my_app.py

==========
lib folder
==========

In order for your framework project to work, the following libraries/modules must be in the 'CIRCUITPY/lib' folder:

* asyncio

* adafruit_ticks

* framework

There will also be other `frk_*` driver files required for your project.

:note: asyncio and adafruit_ticks can be found in the `Adafruit libraries bundle <https://circuitpython.org/libraries>`_.