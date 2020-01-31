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


def breathe(target_color: tuple, steps: int = 500, speed: int = 90):
    if speed <= 0:
        speed = 1
    if speed > 100:
        speed = 100

    speed_factor = speed / 100

    step_R = target_color[0]/steps
    step_G = target_color[1]/steps
    step_B = target_color[2]/steps

    r = 0
    g = 0
    b = 0

    # Fade from 0 to target: each step gets a shorter delay
    # count down from steps to 0, with ln(step)
    for i in range(steps, 0, -1):
        c = (int(r), int(g), int(b))
        pixel.fill(c)
        pixel.show()
        delay_ms = math.log(i)/speed_factor
        time.sleep(delay_ms / 1000)
        r += step_R
        g += step_G
        b += step_B


    # Fade from target to 0: each step gets a longer delay
    # count up from 0 to steps witn ln(step)
    for i in range(0, steps, 1):
        r -= step_R
        g -= step_G
        b -= step_B
        c = (int(r), int(g), int(b))
        pixel.fill(c)
        pixel.show()
        delay_ms = math.log(i)/speed_factor
        time.sleep(delay_ms / 1000)
    
    '''
    for x in range(steps):
        c = (int(r), int(g), int(b))
        pixel.fill(c)
        pixel.show()
        time.sleep(wait_ms / 1000)
        r += step_R
        g += step_G
        b += step_B

    time.sleep(wait_ms / 500)

    for x in range(steps):
        r -= step_R
        g -= step_G
        b -= step_B
        c = (int(r), int(g), int(b))
        pixel.fill(c)
        pixel.show()
        time.sleep(wait_ms / 1000)

    time.sleep(wait_ms / 500)
    '''

    # Need to vary delay time logarithmically so that it's slower early in
    # the ramp up and faster at the top.


if __name__ == '__main__':
    while True:
        breathe((0, 33, 165))
