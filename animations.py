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


pixel = neopixel.NeoPixel(board.D18, 24)


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
            time.sleep(math.log(j) / 1000)
        
        time.sleep(delay_sec)


if __name__ == '__main__':
    while True:
        for i in range(2):
            breathe((0, 33, 165))

        countdown((0, 33, 165), 24)
