import pygame

class Pacman(pygame.sprite.Sprite):

    def __init__(self, name, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img).convert_alpha()

        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.name = name + str(id(self))
        self.speed = 5
        self.direction = 0
        self.lives = 3


    def move(self, direction):
        if (direction == 0):
            self.rect.y -= self.speed
        if (direction == 1):
            self.rect.y += self.speed
        if (direction == 2):
            self.rect.x -= self.speed
        if (direction == 3):
            self.rect.x += self.speed
