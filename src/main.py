#Python 2

import rrb2 as rrb
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

def forward():
    rr.set_motors(1, 0, 1, 0)

def stop():
    rr.set_motors(0, 0, 0, 0)

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop()
                sys.exit()
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == CONTROLLER_PAD_UP:
                    forward()
            else:
                stop()

    except KeyboardInterrupt:
        print("Interrupt Received!")
        rr.stop()
        sys.exit(1)