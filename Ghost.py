import pygame
import Pacman
import Walls
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
        self.savedx = self.rect.x
        self.savedy = self.rect.y
        self.course = []

    def reset(self):
        self.rect.y = self.savedy
        self.rect.x = self.savedx



    def update(self):
        rando = random.randrange(5)
        if rando == 0:
            self.rect.x += 0
        if rando == 1:
            self.rect.x += 10
        if rando == 2:
            self.rect.y += 10
        if rando == 3:
            self.rect.y -= 10
        if rando == 4:
            self.rect.x -= 10

    # def moveUp(self):
    #     self.rect.y -= self.speed
    # def moveDown(self):
    #     self.rect.y += self.speed
    # def moveLeft(self):
    #     self.rect.x -= self.speed
    # def moveRight(self):
    #     self.rect.x += self.speed
    #
    # def canMove(self, direction):
    #     canmovex = self.rect.x
    #     canmovey = self.rect.y
    #     #if self.rect.colliderect()
    #     if direction == 0:
    #         if (canmovex, canmovey - self.speed) in Walls.Walls.allwalls():
    #             return False
    #         return True
    #     if direction == 1:
    #         if (canmovex, canmovey + self.speed) in Walls.Walls.allwalls():
    #             return False
    #         return True
    #     if direction == 2:
    #         if (canmovex - self.speed, canmovey) in Walls.Walls.allwalls():
    #             return False
    #         return True
    #     if direction == 3:
    #         if (canmovex + self.speed, canmovey) in Walls.Walls.allwalls():
    #             return False
    #         return True
