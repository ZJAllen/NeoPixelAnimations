# Animations to add:
# Breathe
# Wheel
# Create library of standard colors
# Clock hands
# Countdown

import board
import neopixel
import time
import math
from PIL import Image


anim1 = "img/Blue Breathing.bmp"
anim2 = "img/Wheel2.bmp"

pixel_pin = board.D18
num_pixels = 24
ORDER = neopixel.GRB

pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2,
                          auto_write=False, pixel_order=ORDER)


def play_anim(animation_bmp):
    wait_sec = 1 / 24  # 24 FPS

    img = Image.open(animation_bmp)
    pix = img.load()

    try:
        if img.size[0] % num_pixels != 0:
            raise ValueError(f"Width of Bitmap is not a multiple of {num_pixels}")
        else:
            for i in range(img.size[0]):
                for j in range(img.size[1]):
                    pixel[j] = pix[i, j]
                pixel.show()
                time.sleep(wait_sec)
    except ValueError:
        raise


def breathe(target_color: tuple, speed: int = 90):
    if speed <= 0:
        speed = 1
    if speed > 100:
        speed = 100

    speed_factor = speed / 100

    steps = max(target_color)

    step_R = target_color[0]/steps
    step_G = target_color[1]/steps
    step_B = target_color[2]/steps

    r = 0
    g = 0
    b = 0

    # Fade from 0 to target: each step gets a shorter delay
    # count down from steps to 0, with ln(step)
    for i in range(steps+1, 0, -1):
        c = (int(r), int(g), int(b))
        pixel.fill(c)
        pixel.show()
        r += step_R
        g += step_G
        b += step_B
        delay_ms = math.log(i) / speed_factor
        time.sleep(delay_ms / 1000)

    # Fade from target to 0: each step gets a longer delay
    # count up from 0 to steps witn ln(step)
    for i in range(1, steps+2, 1):
        r -= step_R
        g -= step_G
        b -= step_B
        c = (int(r), int(g), int(b))
        pixel.fill(c)
        pixel.show()
        delay_ms = math.log(i) / speed_factor
        time.sleep(delay_ms / 1000)

    # Pause at 'off' for a moment
    time.sleep(0.1)


def countdown(color: tuple, timer_seconds: int):
    delay_sec = timer_seconds / 24

    pixel.fill(color)

    for i in range(24):
        # Instead of jumping to off, fade to off
        steps = max(color)

        r = color[0]
        g = color[1]
        b = color[2]

        step_R = color[0]/steps
        step_G = color[1]/steps
        step_B = color[2]/steps

        for j in range(1, steps+1, 1):
            r -= step_R
            g -= step_G
            b -= step_B
            fade_color = (int(r), int(g), int(b))
            pixel[i] = fade_color
            pixel.show()
            time.sleep(math.log(j) / 1000)

        time.sleep(delay_sec)


def wheel(base_color: tuple, wheel_color: tuple, speed: int = 50):
    pixel.fill(base_color)
    pixel[0] = wheel_color

    if speed > 100:
        speed = 100
    if speed < 1:
        speed = 1

    delay_sec = 1 / speed * 10

    for i in range(1, 24):
        pixel[i-1] = base_color
        pixel[i] = wheel_color
        pixel.show()
        time.sleep(delay_sec)


if __name__ == '__main__':
    blue = (0, 33, 165)
    red = (100, 0, 0)
    orange = (250, 70, 22)
    white = (100, 100, 100)

    for i in range(3):
        play_anim(anim2)

    '''
    while True:
        for i in range(2):
            breathe((0, 33, 165))

        for i in range(2):
            wheel(white, red)
    '''
