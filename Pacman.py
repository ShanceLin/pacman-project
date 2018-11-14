import pygame

class Pacman(pygame.sprite.Sprite):
    images = [pygame.image.load ("assets/hero_frame1").convert(), pygame.image.load ("seets/hero_frame2").convert(), pygame.image.load("assets/hero_frame3").convert()]

    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surface = self.images
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name + str(id(self))
        self.speed = 5
        self.direction = 0
        

    def move(self, direction):
        pressed = pygame .key.get_pressed()
        if pressed(K_UP):
            self.rect.y -= self.speed
        if pressed(K_DOWN):
            self.rect.y += self.speed
        if pressed(K_LEFT):
            self.rect.x -= self.speed
        if pressed(K_RIGHT):
            self.rect.y += self.speed
