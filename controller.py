#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nickd
#
# Created:     29/11/2018
# Copyright:   (c) nickd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import pygame
import Pacman
import Ghost
import Pellets
import BigPellets
import Walls
import random

class Controller:
    def __init__(self, width=645, height=795):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        pygame.font.init()

        self.pacman = Pacman.Pacman("Pacman", 322, 510, "assets/hero_frame1.png")
        level = 1

        self.ghosts = pygame.sprite.Group()
        numGhosts = (1 * level)
        for i in range(numGhosts):
            x = random.randrange(220, 420)
            y = random.randrange(300, 400)
            self.ghosts.add(Ghost.Ghost("Ghosts", x, y, 10, "assets/ghost.gif"))

        self.pellets = pygame.sprite.Group()
        numPellets = 100
        for i in range(numPellets):
            self.pellets.add(Pellets.Pellets("Pellets", 200, 200, "assets/dot.png"))

        self.bigpellets = pygame.sprite.Group()
        numBigpellets = 10
        for i in range(numBigpellets):
            self.bigpellets.add(BigPellets.BigPellets("BigPellets", 150, 150, "assets/bigdot.png"))

        self.walls = pygame.sprite.Group()

        self.score = 0
        self.roundIsOn = True
        self.blueTime = 10
        self.ghostIsVulnerable = False

        self.allSprites = pygame.sprite.Group((self.pacman,) + tuple(self.ghosts) + tuple(self.pellets) + tuple(self.bigpellets) + tuple(self.walls))
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        #main loop of game
        pygame.key.set_repeat(1,50)
        while self.state == "GAME":
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP):
                        self.pacman.move(0)
                    elif (event.key == pygame.K_DOWN):
                        self.pacman.move(1)
                    elif (event.key == pygame.K_LEFT):
                        self.pacman.move(2)
                    elif (event.key == pygame.K_RIGHT):
                        self.pacman.move(3)

            #checks for collisions with walls


            #checks for ghost vulnerability
            self.screen.blit(self.background, (0, 0))
            # for g in self.ghosts:
            #     if g.isBlue:
            #         g.checkIfBlue()
            getpellet = pygame.sprite.spritecollide(self.pacman, self.pellets, True)
            getBigPellet = pygame.sprite.spritecollide(self.pacman, self.bigpellets, True)
            if getBigPellet:
                self.ghostIsVulnerable = True
            if len(self.pellets) == 0 & len(self.bigpellets) == 0:
                self.roundIsOn = False
            if (self.pacman.lives == 0):
                self.roundIsOn = False

            #checks for contact betwen ghosts
            touched = pygame.sprite.spritecollide(self.pacman, self.ghosts, True)
            if touched:
                if self.ghostIsVulnerable == False:
                    self.pacman.lives -= 1
                    print(self.pacman.lives)
                    print("reset occuring")
                    self.pacman.reset()
                elif self.ghostIsVulnerable == True:
                    print("Ghost died")
            self.allSprites.draw(self.screen)
            pygame.display.flip()

            #redraws screen
            self.ghosts.update()
            self.screen.blit(self.background, (0, 0))
            if(self.pacman.lives == 0):
                self.state = "GAMEOVER"

            #displays score
            myfont = pygame.font.SysFont(None, 30)
            text = myfont.render('SCORE: ', False, (0,0,0))
            self.screen.blit(text,(600,600))
            if getpellet:
                self.score += 10
            if getBigPellet:
                self.score += 100

    def gameOver(self):
        self.pacman.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0,0,0))
        self.screen.blit(message, (self.width/2,self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
