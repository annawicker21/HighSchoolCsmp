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

PI = 3.141592653

# Set the height and width of the screen
size = (800, 1000)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    pygame.draw.circle(screen, SKIN, [400, 250], 100)
    pygame.draw.ellipse(screen, BLACK, [350, 200, 25, 40])
    pygame.draw.ellipse(screen, BLACK, [425, 200, 25, 40])
    pygame.draw.arc(screen, BLACK, [350, 225, 100, 80], PI, 0, 5)
    pygame.draw.line(screen, BLACK, [400, 350], [400, 700], 5) #body
    pygame.draw.line(screen, BLACK, [400, 400], [300, 475], 5) #left arm
    pygame.draw.line(screen, BLACK, [300, 475], [225, 425], 5)
    pygame.draw.line(screen, BLACK, [400, 400], [500, 475], 5) #right arm
    pygame.draw.line(screen, BLACK, [500, 475], [575, 425], 5)
    pygame.draw.line(screen, BLACK, [400, 700], [515, 825], 5) #left leg
    pygame.draw.line(screen, BLACK, [400, 700], [275, 825], 5) #right leg

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()



