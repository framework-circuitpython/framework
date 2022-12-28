========
Your App
========

An app is a Python (.py or .mpy) file that is in a project folder, has the same name as the project folder, and contains Python (and possibly other) code that describes the desired functionality for the project.

`framework` apps support several different design paradigms:

* Arduino-like 'setup/loop'

* asyncio-like 'run'

* Object Oriented

* Callbacks

setup/loop
----------

'setup/loop' as the title suggests uses a `setup` function and a `loop` function. `setup` is called once at the start of the app and `loop` is called at regular intervals for the lifetime of the app (run "forever"):

.. code-block:: python

    from framework import board_led, clk

    def setup():
        pass
    
    def loop():
        board_led.value = clk.value

However, using `loop` can imply that `setup` is being used without actually stating it:

.. code-block:: python

    from framework import board_led, clk

    def loop():
        board_led.value = clk.value

And using `setup` can imply that `loop` is being used without actually stating it (showing callback and optional `SLEEP` value in this example):
    
.. code-block:: python

    from framework import board_led, clk

    sleep = 0.01

    def invert():
        board_led.value = not board_led.value
    
    def setup():
        clk.register_callback('event', invert)

Or all together:

.. code-block:: python

    from framework import board_led, clk

    sleep = 0.01

    def print_clk_value():
        print(clk.value)
    
    def setup():
        clk.register_callback('event', print_clk_value)
    
    def loop():
        board_led.value = clk.value

run
----

The 'run' paradigm explicitly uses `asyncio` and `run` is the only required function in this style of app:

.. code-block:: python

    from framework import board_led, clk
    import asyncio

    async def run():
        while True:
            board_led.value = clk.value
            await asyncio.sleep(0.01)

Any initialization or setup must be done inside the `run` function before the `while True` loop (with callback):

.. code-block:: python

    from framework import board_led, clk
    import asyncio

    def print_clk_value():
        print(clk.value)
    
    def blink():
        board_led.value = clk.value
    
    async def run():
        clk.register_callback('event', print_clk_value)
        while True:
            blink()
            await asyncio.sleep(0.01)

Callbacks
---------

Callbacks are functions that are registered to be called when needed such as at the occurance of an event. In the examples above, `'event'` was the event used to trigger the callback. However, `clk` is an instance of the `FreeRun` peripheral type and, for example, `FreeRun` also has `'rising'` and `'falling'` events that can be used to trigger callbacks. Each peripheral has its own set of zero or more callback triggers that callbacks can be registered to. Refer to the peripheral code or documentation for the available callback triggers for that peripheral.

Callbacks can be registered multiple times:

.. code-block:: python

    from framework import button0, button1, board_led

    def invert():
        board_led.value = not board_led.value
    
    def print_rising():
        print('RISING')
    
    def setup():
        # button0 callbacks
        button0.register_callback('event', invert)

        # button1 callbacks
        button1.register_callback('event', invert)
        button1.register_callback('rising', print_rising)

Multiple callbacks can be registered to the same event:

.. code-block:: python

    from framework import button0, button1, board_led

    def invert():
        board_led.value = not board_led.value
    
    def print_rising():
        print('RISING')
    
    def print_event():
        print('EVENT')
    
    def setup():
        # button0 callbacks
        button0.register_callback('event', invert)
        button0.register_callback('event', print_event)

        # button1 callbacks
        button1.register_callback('event', invert)
        button1.register_callback('rising', print_rising)