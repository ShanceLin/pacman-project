import pygame   

class Pellets(pygame.sprite.Sprite):

    def __init__(self, name, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img).convert_alpha()

        self.surface = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def pelletslist(self):
        pelletslist = []
        pellets.append((x,y))
        
