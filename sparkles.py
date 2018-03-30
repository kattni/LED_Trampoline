# NeoPixie Dust Bag
# learn.adafruit.com/neopixel-pixie-dust-bag

import digitalio
import board
import neopixel
import time
import random

pixel_pin = board.D10
pixel_count = 180  # Number of NeoPixels connected to GEMMA
delay_seconds = 0  # delay between blinks, smaller numbers are faster
delay_multiplier = 0  # Randomization multiplier, delay speed of the effect


pixels = neopixel.NeoPixel(pixel_pin, pixel_count, brightness=.4, auto_write=False)


def sparkles(red_value, green_value, blue_value):
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


def gold_sparkles():
    sparkles(255, 222, 30)


def pink_sparkles():
    sparkles(242, 90, 255)


def blue_sparkles():
    sparkles(50, 255, 255)


def green_sparkles():
    sparkles(0, 255, 40)


def orange_sparkles():
    sparkles(255, 100, 0)


def sparkle_list():
    gold_sparkles()
    blue_sparkles()
    green_sparkles()
    pink_sparkles()
    orange_sparkles()


while True:
    sparkle_list()
