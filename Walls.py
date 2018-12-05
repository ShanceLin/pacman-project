import pygame

class Walls(pygame.sprite.Sprite):
    def __init__(self, image, tup):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = tup
