Introduction
============

Cooperative Multitasking for CircuitPython

`framework` for CircuitPython is a project framework for microcontrollers running CircuitPython using cooperative multitasking. It helps keep projects organized.
It makes peripherals easy and reusable.

Because framework runs on top of CircuitPython >= 7.1.0, make sure you are familiar with and set up for CircuitPython before starting. framework has been developed for and tested on RP2040, SAMD51, and SAMD21 based microcontroller boards. It has not been tested on ARM or x86/64 devices.


Installation
============

This guide assumes you have followed the excellent Welcome to CircuitPython tutorial and have a CIRCUITPY drive accessible on your computer.

Clone or download the framework bundle repository as a zip file and unzip it in a convenient location. Copy the 'framework.mpy' file from the framework bundle to the 'lib' folder on your CIRCUITPY drive. You will also need to copy the 'asyncio' library and 'adafruit_ticks.mpy' module from the Adafruit libraries bundle to the 'lib' folder on your CIRCUITPY drive.

Check to see that your CIRCUITPY drive looks like the following:

::

| CIRCUITPY
|-- lib
|---- asyncio
|---- adafruit_ticks.mpy
|---- framework.mpy


Usage Example
=============

There are four steps to making a framework project:

1. Organize your project

2. Make a configurations file and connect the peripherals to your board

3. Write an app

4. Load and launch your app

Hello World! Blink
==================

Getting Organized
-----------------

The first step to starting a framework project is to organize your CIRCUITPY drive. Make sure that you have the 'asyncio' library, the 'adafruit_ticks' module, and the 'framework' module in your 'lib' folder as described in the Installation section of this document. Next make a folder with your project name. For this example, let's use 'blink' as our project name.

We will also be using 'frk_freerun.mpy' and 'frk_digitalout.mpy' for this project, so copy those from the 'framework/peripherals' folder to your 'CIRCUITPY/lib' folder as well.

::

| CIRCUITPY
|-- blink
|-- lib
|---- asyncio
|---- adafruit_ticks.mpy
|---- framework.mpy
|---- frk_digitalout.mpy
|---- frk_freerun.mpy

Configure
---------

The next thing we need to do is make a configurations file. This contains information about our peripherals including the peripheral alias and peripheral type. Using your favorite Python (or plain text) editor, copy and paste the following configurations and save the file as 'CIRCUITPY/blink/conf.py':

.. code-block:: python

    # blink/conf.py
    conf = {
        'board_led':
            {'driver': 'DigitalOut',
             'invert': False,
             'pin':
                 {'led': 'LED'}
        },
        'clock':
            {'driver': 'FreeRun',
             't_on': 0.1,
             't_off': 0.9
        }
    }

:note: In this example, there isn't any external hardware to connect if you have an onboard LED. However, if your board does not have an onboard LED, connect an LED to a digital pin on your board and change "LED" to the name of the pin you have connected to (eg. "GP0", "D1", ...). You might also want to change the `invert` setting to `True` depending on your board.

Your Code
---------

The magic of framework is that it lets us import our peripherals into our app in a Pythonic way. It uses the peripheral aliases we used in our configurations file. framework will also handle the details of making our app run "forever". Using your favorite Python (or plain text) editor, copy and paste the following code and save the file as 'CIRCUITPY/blink/blink.py':

.. code-block:: python
    
    # blink/blink.py
    from framework import board_led, clock

    def invert(v):
        board_led.value = not board_led.value

    clock.on_event = invert

Load and Launch
---------------

Another magic thing that framework does is load our app and peripherals in a very simple way. Given our app name, it looks for our project folder, finds our configurations file and loads the peripherals, loads our app, and runs the peripherals and app. This is accomplished using AppLoader. Using your favorite Python (or plain text) editor, copy and paste the following code and save the file as 'CIRCUITPY/code.py':

.. code-block:: python

    # code.py
    from framework import run

    run('blink')

:note: If you are using the default CircuitPython settings that resets when there is a change on your CIRCUITPY drive, you should see a blinking LED on your board. If not, you may need to manually reset your board following the instructions specific to your board to do so.