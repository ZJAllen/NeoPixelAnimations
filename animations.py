# Animations to add:
# Breathe
# Wheel
# Create library of standard colors
# Clock hands
# Countdown

import board
import neopixel
import time


puck = neopixel.NeoPixel(board.D18, 24)


def breathe(target_color: tuple, steps: int = 100, speed: int = 10):
    if speed <= 0:
        speed = 1
    if speed > 100:
        speed = 100

    wait_ms = 100 - speed

    step_R = target_color[0]/steps
    step_G = target_color[1]/steps
    step_B = target_color[2]/steps

    r = 0
    g = 0
    b = 0

    for x in range(steps):
        c = (int(r), int(g), int(b))
        puck.fill(c)
        puck.show()
        time.sleep(wait_ms / 1000.0)
        r += step_R
        g += step_G
        b += step_B

    for x in range(steps):
        r -= step_R
        g -= step_G
        b -= step_B
        c = (int(r), int(g), int(b))
        puck.fill(c)
        puck.show()
        time.sleep(wait_ms / 1000.0)


if __name__ == '__main__':
    while True:
        breathe((0, 33, 165))
