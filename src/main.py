#Python 2

import rrb2 as rrb
import sys
import os
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

movement = {"x": 0, "y": 0}

def forward():
    rr.set_motors(1, 0, 1, 0)

def stop():
    rr.set_motors(0, 0, 0, 0)

def move():
    left_go = abs(movement["y"])
    left_dir = movement["y"] < 0
    right_go = abs(movement["y"])
    right_dir = movement["y"] < 0
    rr.set_motors(left_go, left_dir, right_go, right_dir)


while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
                sys.exit()
            elif event.type == pygame.JOYAXISMOTION:
                axis = "x"
                if event.axis  > 0:
                    axis = "y"
                movement[axis] = round(event.value,2)
        move()

    except KeyboardInterrupt:
        print("\nInterrupt Received!")
        rr.stop()
        sys.exit(1)