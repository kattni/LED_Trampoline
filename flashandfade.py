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


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


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


NUMBER_OF_LEDS = 45
COLOR_STEP = int(256 / NUMBER_OF_LEDS)

fade = fade_control()

while True:
    try:
        if vibration_switch.value is False:
            fade = fade_control()
            pixels.fill((255, 0, 0))
            pixels.show()
        next(fade)
    except StopIteration:
        pass

"""        
for i in range(NUMBER_OF_LEDS):
    pixels.brightness = 0.1
    pixels[i] = wheel(COLOR_STEP * i)
    pixels.show()
    """
