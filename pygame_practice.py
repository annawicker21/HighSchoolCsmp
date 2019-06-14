"""
title: pygame_practice
author: Anna
date: 2019-06-14 09:52
"""

import pygame

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKIN = (255, 227, 197)
HAIR = (67, 43, 26)
ORANGE = (231, 145, 26)

PI = 3.141592653

# Set the height and width of the screen
size = (800, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 30


def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, ORANGE, [200 + x, 550 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, SKIN, [400 + x, 250 + y], 100)
    pygame.draw.ellipse(screen, BLACK, [350 + x, 200 + y, 25, 40])
    pygame.draw.ellipse(screen, BLACK, [425 + x, 200 + y, 25, 40])
    pygame.draw.arc(screen, BLACK, [350 + x, 225 + y, 100, 80], PI, 0, 5)
    pygame.draw.line(screen, BLACK, [400 + x, 350 + y], [400 + x, 700 + y], 5)  # body
    pygame.draw.line(screen, BLACK, [400 + x, 400 + y], [300 + x, 475 + y], 5)  # left arm
    pygame.draw.line(screen, BLACK, [300 + x, 475 + y], [225 + x, 425 + y], 5)
    pygame.draw.line(screen, BLACK, [400 + x, 400 + y], [500 + x, 475 + y], 5)  # right arm
    pygame.draw.line(screen, BLACK, [500 + x, 475 + y], [575 + x, 425 + y], 5)
    pygame.draw.line(screen, BLACK, [400 + x, 700 + y], [515 + x, 825 + y], 5)  # left leg
    pygame.draw.line(screen, BLACK, [400 + x, 700 + y], [275 + x, 825 + y], 5)  # right leg

# Loop as long as done == False
while not done:
    ball_pos += ball_change

    if ball_pos > 89:
        ball_change -= 3
    if ball_pos < 25:
        ball_change += 3

    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -10
    if keys[pygame.K_RIGHT]:
        x_speed = 10
    if keys[pygame.K_UP]:
        y_speed = -10
    if keys[pygame.K_DOWN]:
        y_speed = 10

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(90)

# Be IDLE friendly
pygame.quit()



