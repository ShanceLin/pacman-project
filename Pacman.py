import pygame
import Walls

class Pacman(pygame.sprite.Sprite):

    def __init__(self, name, x, y, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/foreman2.png").convert_alpha()
        self.surface = self.image
        self.FirstPic = True
        self.frame = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.savedx = x
        self.savedy = y
        self.direction = 3

        self.name = name + str(id(self))
        self.speed = speed
        self.direction = 3
        self.lives = 3

    # def getSurface(self):
    #     if self.direction == 0:
    #         self.image = pygame.image
    #     elif self.direction == 1:
    #         self.image = pygame.transform.rotate (self.images, 90)
    #     elif self.direction == 2:
    #         self.image = pygame.transform.rotate (self.image, 180)
    #     elif self.direction == 3:
    #        print(self.direction)
    #        self.image = pygame.transform.rotate (self.image, 270)

    def moveUp(self):
        self.rect.y -= self.speed
    def moveDown(self):
        self.rect.y += self.speed
    def moveLeft(self):
        self.rect.x -= self.speed
    def moveRight(self):
        self.rect.x += self.speed

    def reset(self):
        self.rect.x = self.savedx
        self.rect.y = self.savedy


    def LoseScreen(self):
        global YELLOW
        return pygame.font.SysFont (None, 72).render("You Lose", True, YELLOW)

    def returnX(self):
        return self.rect.x

    def returnY(self):
        return self.rect.y


    def canMove(self, direction):
        canmovex = self.rect.x
        canmovey = self.rect.y
        #if self.rect.colliderect()
        if direction == 0:
            if (canmovex, canmovey - self.speed) in Walls.Walls.allwalls():
                return False
            return True
        if direction == 1:
            if (canmovex, canmovey + self.speed) in Walls.Walls.allwalls():
                return False
            return True
        if direction == 2:
            if (canmovex - self.speed, canmovey) in Walls.Walls.allwalls():
                return False
            return True
        if direction == 3:
            if (canmovex + self.speed, canmovey) in Walls.Walls.allwalls():
                return False
            return True
    def returnRect(self):
        return self.rect

    def returnSpeed(self):
        return self.speed

    def teleright(self):
        if self.rect.x == 0 & self.rect.y == 325:
            self.rect.x = 600

    def teleleft(self):
        if self.rect.x == 0 & self.rect.y == 600:
            self.rect.x = 0
