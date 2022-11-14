==============
Configurations
==============

A configurations file is a Python (.py or .mpy) file that is found in the project folder, has name 'conf.py', and contains information about all peripherals needed for a project (ie. a peripheral configuration). There may be zero or more peripheral configurations in a configurations file. At the most base level, a configurations file is a set of nested dictionaries.

Each peripheral configuration has two requirements:

* A unique alias that identifies the individual peripheral

* A driver that identifies the functionality of the peripheral (does not need to be unique)

Optionally, a peripheral configuration may contain:

* Default settings and values


* Initialization information

* pin or pins aliases and names

For example:

::

.. code-block:: python

    conf = {
        'board_led':
            {'driver': 'DigitalOut',
             'enable': True,
             'invert': False,
             'drive_mode': 'PUSH_PULL',
             'pin':
                 {'led': 'LED'}
        },
        {
        'clk':
            {'driver': 'FreeRun',
             'initial_value': False,
             't_on': 0.1,
             't_off': 0.9
            }
        }
    }

'pin' and 'pins'
----------------

In the configurations file, framework does not differentiate between "pin" and "pins". There is no singular or plural pin in the configurations file. You should expect a different level of importance placed on pin aliases and names depending on the peripheral. In general, peripherals that use single pins will ignore the alias. Also in general, peripherals with more than one pin will place different levels of priority on the aliases and names.

In cases with multiple non-specialized pins (eg. keypads) the pin names will be reordered in alpha-numeric order (eg. D1, D3, A5 -> A5, D1, D3) before being used and the pin aliases and names will be made available by the peripheral.

For specialized pins, the pin alias is very important and attempts to follow standard conventions. For example, for I2C devices the naming convention for those pins is SCL and SDA. The pin aliases here specify which pin is SCL and which is SDA and will be used as such.

However, if used, each pin must have an alias that is unique in its scope and a name that is unique to the configurations file and compatible with the board being used. For example, the Raspberry Pi Pico uses a "GP*" (eg. GP0, GP1, ...) naming convention while other boards like the Adafruit Grand Central M4 uses an "A*"/"D*" (eg. A0, A1, D0, D1, ...) naming convention. The naming convention used in the configurations file must match the pin naming convention used on the board. If there is any question about the naming convention used on the board, enter the REPL, import board, and print(dir(board)). This will show the pin names available on the board.