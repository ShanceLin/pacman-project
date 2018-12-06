import pygame

class livesRemaining(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Vulnerable(self):
        self.rect.x = 675
        self.rect.y = 50

    def resetVul(self):
        self.rect.x = 7000
        self.rect.y = 7000
