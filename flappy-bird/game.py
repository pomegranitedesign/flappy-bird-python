import pygame
import sys

# Initialize pygame in order to make
# everything work
pygame.init()

# Setup the variables for screen dimensions
size = width, height = 350, 200

# Setup the backgroud image


class BackgroudImage(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


bgImage = BackgroudImage()
