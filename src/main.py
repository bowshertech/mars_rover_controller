#Python 2

import rrb2 as rrb
import os
import math
import sys
import pygame

#import ex_8x8_pixels

rr = rrb.RRB2(revision=2)
pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()

CONTROLLER_PAD_UP = 4
CONTROLLER_PAD_RIGHT = 5
CONTROLLER_PAD_DOWN = 6
CONTROLLER_PAD_LEFT = 7

movement = {"x1": 0, "y1": 0, "x2": 0, "y2": 0}

# def forward(lspeed, rspeed):
#     rr.set_motors(lspeed, 0, rspeed, 0)
#
# def reverse(lspeed, rspeed):
#     rr.set_motors(lspeed, 1, rspeed, 1)
#

def stop():
    rr.set_motors(0, 0, 0, 0)

def calc_dir():
    left_reverse = False
    right_reverse = False

    if movement["x2"] > 0:
        right_speed = (1 - math.sqrt(abs(movement["y1"]))) + 0.1
        left_speed = abs(movement["y1"])
    elif movement["x2"] < 0:
        left_speed = (1 - math.sqrt(abs(movement["y1"]))) + 0.1
        right_speed = abs(movement["y1"])
    else:
        right_speed = abs(movement["y1"])
        left_speed = abs(movement["y1"])

    if movement["y1"] > 0:
        left_reverse = True
        right_reverse = True

    if left_speed > 1:
        left_speed = 1
    if right_speed > 1:
        right_speed = 1

    os.system('clear')
    print(left_speed)
    print(right_speed)

    move(left_speed, left_reverse, right_speed, right_reverse)




def move(lsp, lrev, rsp, rrev):
    rr.set_motors(lsp, lrev, rsp, rrev)


while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
                sys.exit()
            elif event.type == pygame.JOYAXISMOTION:
                axis = "x1"
                if event.axis == 1:
                    axis = "y1"
                elif event.axis == 2:
                    axis = "x2"
                elif event.axis == 3:
                    axis = "y2"

                movement[axis] = round(event.value,2)
                calc_dir()

    except KeyboardInterrupt:
        print("\nInterrupt Received!")
        rr.stop()
        sys.exit(1)

