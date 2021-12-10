import pygame
from pygame.locals import *


import ctypes
ctypes.windll.user32.SetProcessDPIAware()


# Initialize pygame
pygame.init()


# Set game title
pygame.display.set_caption("")

# Create the screen
screen_width, screen_height = 1920, 1080
flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((screen_width, screen_height), flags, 16)

# Frame control
FPS = 60
fps_clock = pygame.time.Clock()
DELTA_TIME = 0

# Indicates whether continue game
running = True


# MAIN GAME LOOP
while running:
    pass
