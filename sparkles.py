# NeoPixie Dust Bag
# learn.adafruit.com/neopixel-pixie-dust-bag

import digitalio
import board
import neopixel
import time
import random
import digitalio

pixel_pin = board.D10
pixel_count = 180  # Number of NeoPixels connected to GEMMA
delay_seconds = 0  # delay between blinks, smaller numbers are faster
delay_multiplier = 0  # Randomization multiplier, delay speed of the effect


pixels = neopixel.NeoPixel(pixel_pin, pixel_count, brightness=.4, auto_write=False)

big_switch = digitalio.DigitalInOut(board.D9)
big_switch.direction = digitalio.Direction.INPUT
big_switch.pull = digitalio.Pull.UP


def sparkle_code(color_values):
    (red_value, green_value, blue_value) = color_values
    # sparkling
    # select a random pixel
    p = random.randint(0, (pixel_count - 2))
    # color value from momentary switch
    pixels[p] = (red_value, green_value, blue_value)
    pixels.show()

    # delay value randomized to up to delay_multiplier times longer
    time.sleep(delay_seconds * random.randint(0, delay_multiplier))

    # set to a dimmed version of the state color
    pixels[p] = (int(red_value / 10), int(green_value / 10), int(blue_value / 10))
    pixels.show()

    # set a neighbor pixel to an even dimmer value
    pixels[p + 1] = (int(red_value / 15), int(green_value / 15), int(blue_value / 15))
    pixels.show()


# Colors:
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
# Sparkle colors:
GOLD = (255, 222, 30)
PINK = (242, 90, 255)
AQUA = (50, 255, 255)
JADE = (0, 255, 40)
AMBER = (255, 100, 0)


def cycle_sequence(seq):
    while True:
        yield from seq


sparkle_list = [
    lambda: sparkle_code(PINK),
    lambda: sparkle_code(GOLD),
    lambda: sparkle_code(AQUA),
    lambda: sparkle_code(JADE),
    lambda: sparkle_code(AMBER)
]


def sparkle(seq):
    sparkles = cycle_sequence(sparkle_list)
    next(sparkles)()


while True:
    if big_switch.value is False:
        print("False")
        sparkle(sparkle_list)
