import neopixel
import board
import digitalio
import time

num_pixels = 180

pixels = neopixel.NeoPixel(board.D10, num_pixels, auto_write=False)

big_switch = digitalio.DigitalInOut(board.D9)
big_switch.direction = digitalio.Direction.INPUT
big_switch.pull = digitalio.Pull.UP

vibration_switch = digitalio.DigitalInOut(board.D7)
vibration_switch.direction = digitalio.Direction.INPUT
vibration_switch.pull = digitalio.Pull.UP


led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


def cycle_sequence(seq):
    while True:
        yield from seq


def fade_control():
    brightness_value = iter([r / 15 for r in range(15, -1, -1)])
    while True:
        # pylint: disable=stop-iteration-return
        pixels.brightness = next(brightness_value)
        pixels.show()
        yield


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (255, 255, 255)


color = cycle_sequence([RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA, WHITE])

fade = fade_control()

while True:
    try:
        if vibration_switch.value is False:
            fade = fade_control()
            pixels.fill(next(color))
            pixels.show()
        next(fade)
    except StopIteration:
        pass
