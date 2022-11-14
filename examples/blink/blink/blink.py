from framework import board_led, clock

def invert(v):
    board_led.value = not board_led.value

clock.on_event = invert