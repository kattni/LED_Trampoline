#
# Kaleidoscope_Eyes_NeoPixel_LED_Goggles.py
#
import board
import neopixel
import time
import random
import digitalio

num_pixels = 180  # Number of NeoPixels
pixpin = board.D10  # Pin where NeoPixels are connected

mode = 0  # Current animation effect

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


def cycle_sequence(seq):
    while True:
        yield from seq


big_switch = digitalio.DigitalInOut(board.D9)
big_switch.direction = digitalio.Direction.INPUT
big_switch.pull = digitalio.Pull.UP

vibration_switch = digitalio.DigitalInOut(board.D7)
vibration_switch.direction = digitalio.Direction.INPUT
vibration_switch.pull = digitalio.Pull.UP

pixels = neopixel.NeoPixel(pixpin, num_pixels, brightness=.3, auto_write=False)

rgb_colors = (RED,
              GREEN,
              BLUE)

rgb_idx = 0
chase_color_cycle = rgb_colors[rgb_idx]
offset = 0
prevtime = time.monotonic()

while True:
    if vibration_switch.value is False:
        for i in range(0, num_pixels):
            c = 0

            if ((offset + i) & 7) < 4:  # Every 4 pixels, light up 4 pixels
                c = chase_color_cycle  # Set the color to the current color from index
            pixels[i] = c  # start at pixel 1, and go towards the middle
            pixels[(num_pixels - 1) - i] = c  # start at the last pixel and go backwards toward middle
        pixels.show()
        offset += 1

    t = time.monotonic()

    if (t - prevtime) > 3:  # Every 3 seconds...
        if rgb_idx > 2:  # if the index goes out of range
            rgb_idx = 0  # Reset it to 0
        chase_color_cycle = rgb_colors[rgb_idx]  # gets the color list
        rgb_idx += 1  # cycles to the next color
        for i in range(0, num_pixels):
            pixels[i] = (0, 0, 0)  # turns off the pixels between colors
        prevtime = t  # resets time.monotonic()
