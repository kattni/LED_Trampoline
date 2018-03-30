import board
import neopixel
import time
import digitalio

num_pixels = 180  # Number of NeoPixels
pixpin = board.D10  # Pin where NeoPixels are connected


pixels = neopixel.NeoPixel(pixpin, num_pixels, brightness=.3, auto_write=False)


big_switch = digitalio.DigitalInOut(board.D9)
big_switch.direction = digitalio.Direction.INPUT
big_switch.pull = digitalio.Pull.UP

vibration_switch = digitalio.DigitalInOut(board.D7)
vibration_switch.direction = digitalio.Direction.INPUT
vibration_switch.pull = digitalio.Pull.UP

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


def slice_rainbow(wait):
    pixels[::6] = [RED] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[1::6] = [ORANGE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[2::6] = [YELLOW] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[3::6] = [GREEN] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[4::6] = [BLUE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[5::6] = [PURPLE] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)


def slice_alternating(wait):
    pixels[::2] = [RED] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels.fill((0, 0, 0))
    pixels[1::2] = [RED] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)


while True:
    pixels.fill((0, 0, 0))
    if big_switch.value is False:
        slice_alternating(0)