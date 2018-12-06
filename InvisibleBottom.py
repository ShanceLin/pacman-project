import pygame
import Pacman

class InvisibleBottom(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/foreman1.png").convert_alpha()
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.x = 325
        self.rect.y = 525 + speed
        self.speed = speed

    def moveUp(self):
        self.rect.y -= self.speed
    def moveDown(self):
        self.rect.y += self.speed
    def moveLeft(self):
        self.rect.x -= self.speed
    def moveRight(self):
        self.rect.x += self.speed
