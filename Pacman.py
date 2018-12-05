import pygame

class Pacman(pygame.sprite.Sprite):

    def __init__(self, name, x, y, img, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img).convert_alpha()

        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.savedx = x
        self.savedy = y

        self.name = name + str(id(self))
        self.speed = speed
        self.direction = 0
        self.lives = 3


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

    def move(self, direction):
        if direction == 0:
            self.rect.top -= self.speed
        elif direction == 1:
            self.rect.left -= self.speed
        elif direction == 2:
            self.rect.top += self.speed
        elif direction == 3:
            self.rect.left += self.speed 
