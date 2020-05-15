import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Basic setup
size = width, height = 280, 400

# Change title and logo
pygame.display.set_caption('Flappy Bird')
icon = pygame.image.load('flappy.ico')
pygame.display.set_icon(icon)

# Background image
backgroundImage = pygame.image.load('./assets/sprites/background-night.png')

# Images
pipe = pygame.image.load('./assets/sprites/pipe-green.png')

# Setup the display
screen = pygame.display.set_mode(size)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            isRunning = False
    screen.blit(backgroundImage, (0, 0))
    pygame.display.update()
