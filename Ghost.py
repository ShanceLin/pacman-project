import pygame
import random

class Ghost(pygame.sprite.Sprite):
    def __init__(self, name, x, y, speed, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name + str(id(self))
        self.speed = speed
        self.course = []
        self.isBlue = False

    def makeBlue(self):
        self.isBlue = True
