#
# Kaleidoscope_Eyes_NeoPixel_LED_Goggles.py
#
import board
import neopixel
import time
import random
import digitalio

numpix = 180  # Number of NeoPixels
pixpin = board.D10  # Pin where NeoPixels are connected

mode = 0  # Current animation effect
offset = 0  # Position of spinny eyes

rgb_colors = ([255, 0, 0],  # red
              [0, 255, 0],  # green
              [0, 0, 255])  # blue

rgb_idx = 0  # index counter - primary color we are on
color = rgb_colors[rgb_idx]

big_switch = digitalio.DigitalInOut(board.D9)
big_switch.direction = digitalio.Direction.INPUT
big_switch.pull = digitalio.Pull.UP

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=.3, auto_write=False)

prevtime = time.monotonic()

while True:
    i = 0
    t = 0

    if big_switch.value is False:
        for i in range(0, numpix):
            c = 0

            # 4 pixels on...
            if ((offset + i) & 7) < 4:
                c = color
            pixels[i] = c
            pixels[(numpix - 1) - i] = c

        pixels.show()
        offset += 1

    t = time.monotonic()

    if (t - prevtime) > 8:  # Every 8 seconds...
        mode += 1  # Next mode
        if mode > 1:  # End of modes?
            mode = 0  # Start modes over

        if rgb_idx > 2:  # reset R-->G-->B rotation
            rgb_idx = 0

        color = rgb_colors[rgb_idx]  # next color assignment
        rgb_idx += 1

        for i in range(0, numpix):
            pixels[i] = (0, 0, 0)

        prevtime = t
