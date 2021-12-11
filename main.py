import pygame
from pygame.locals import *
import cv2
import numpy


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


def draw_aacircle(surface: pygame.Surface, color, center, radius, width):
    circle_image = numpy.zeros((radius*2 + 4, radius*2 + 4, 4), dtype=numpy.uint8)
    circle_image = cv2.circle(circle_image, (radius+2, radius+2), radius-width//2, (*color, 255), width, lineType=cv2.LINE_AA)
    circle_surface = pygame.image.frombuffer(circle_image.flatten(), (radius*2+4, radius*2+4), 'RGBA')
    surface.blit(circle_surface, circle_surface.get_rect(center=center))


class Ball(pygame.sprite.Sprite):
    """
    A ball class which player can control by changing gravity
    """

    def __init__(self):
        """
        Initializing method
        """

        pygame.sprite.Sprite.__init__(self)

        # Position and radius of the ball
        self.radius = 30
        self.pos_x = 100
        self.pos_y = 100

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw this sprite on the given surface

        :param surface: surface to draw on
        :return: None
        """

        draw_aacircle(surface, (255, 255, 255), (self.pos_x, self.pos_y), self.radius, 10)


ball = Ball()


# MAIN GAME LOOP
while running:

    # Get all kind of events
    pygame.event.get()

    # Get all kind of keyboard inputs
    keys = pygame.key.get_pressed()

    # Break the loop and exit the program when pressed ESC key
    if keys[pygame.K_ESCAPE]:
        running = False

    ball.draw(screen)

    pygame.display.flip()
    DELTA_TIME = fps_clock.tick(FPS) / 1000
