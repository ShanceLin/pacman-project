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
import Lives

class Controller:
    def __init__(self, width=750, height=825):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.pacmanspeed = 25
        self.pacman = Pacman.Pacman("Pacman", 325, 525, "assets/foreman1.png", self.pacmanspeed)
        level = 1

        self.ghosts = pygame.sprite.Group()
        numGhosts = (2 * level)
        ghostspeed = 25
        for k in range(numGhosts):
            x = random.randrange(275, 350)
            self.ghosts.add(Ghost.Ghost("Ghosts", x, 325, ghostspeed, "assets/carsprite.png"))
        #pelletcount = 0
        self.pellets = pygame.sprite.Group()

        for p in Pellets.Pellets.pelletlocations():
            self.pellets.add(Pellets.Pellets("Pellets", "assets/dot.png", p))
            #pelletcount +=1
        #print(pelletcount)
        self.bigpellets = pygame.sprite.Group()

        bigpelletlocations = ((25,75),(600,75), (25, 525), (600,525))
        for z in bigpelletlocations:
            self.bigpellets.add(BigPellets.BigPellets("BigPellets", "assets/bigdot.png", z))

        self.walls = pygame.sprite.Group()
        for y in Walls.Walls.allwalls():
            self.walls.add(Walls.Walls("assets/wall.png", y))
        #theres 478 walls rip
        self.livesRemaining = pygame.sprite.Group()
        for i in range(self.pacman.lives):
            self.livesRemaining.add(Lives.livesRemaining(i*20+675, 10, 'assets/foreman1.png'))

        self.font = pygame.font.SysFont("Times New Roman", 25)

        self.roundIsOn = True
        self.blueTime = 10
        self.ghostIsVulnerable = False

        self.allSprites = pygame.sprite.Group((self.pacman,) + tuple(self.ghosts) + tuple(self.pellets) + tuple(self.bigpellets) + tuple(self.walls) + tuple(self.livesRemaining))
        self.state = "GAME"
        self.z = 0
        self.ghostKill = False
        self.colliding = False

        self.fontTitle = pygame.font.SysFont("helvetica", 72)
        self.fontOther = pygame.font.SysFont("helvectica", 52)

    def gameIntro(self):
        title = self.fontTitle.render("FOREMAN", True, (0, 0, 0))
        start = self.fontOther.render("Press ENTER to start", True, (0, 0, 0))
        instructions = self.fontOther.render("press ARROWKEYS to move", True, (0, 0, 0))

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

            self.scren.fill((15, 9, 119))
            self.screen.blit(title, (200, 150))
            self.screen.blit(start, (120, 250))
            self.screen.blit(instructions, (200, 350))

            pygame.display.flip()
            self.clock.tick(60)
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
            self.background.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP):
                        if self.pacman.canMove(0) == True:
                            self.pacman.moveUp()
                    elif (event.key == pygame.K_DOWN):
                        if self.pacman.canMove(1) == True:
                            self.pacman.moveDown()
                    elif (event.key == pygame.K_LEFT):
                        if self.pacman.canMove(2) == True:
                            self.pacman.moveLeft()
                    elif (event.key == pygame.K_RIGHT):
                        if self.pacman.canMove(3) == True:
                            self.pacman.moveRight()

            self.screen.blit(self.background, (0, 0))
            for g in self.ghosts:
                if g.isBlue:
                    g.checkIfBlue()
            getpellet = pygame.sprite.spritecollide(self.pacman, self.pellets, True)
            getBigPellet = pygame.sprite.spritecollide(self.pacman, self.bigpellets, True)
            if getBigPellet:
                self.ghostIsVulnerable = True
            if len(self.pellets) == 0 & len(self.bigpellets) == 0:
                self.roundIsOn = False
            if (self.pacman.lives == 0):
                self.roundIsOn = False

            touched = pygame.sprite.spritecollide(self.pacman, self.ghosts, self.ghostKill)
            if touched:
                if self.ghostIsVulnerable == False:
                    self.pacman.lives -= 1
                    lives = self.livesRemaining.sprites()
                    lives[0].kill()
                    self.pacman.reset()

                    self.allSprites.update()

                elif self.ghostIsVulnerable == True:
                    self.ghostKill = True
                    print("Ghost died")

            #redraws screen
            self.ghosts.update()
            self.screen.blit(self.background, (0, 0))
            if(self.pacman.lives == 0):
                self.state = "GAMEOVER"

            #displays score
            myfont = pygame.font.SysFont(None, 30)
            text = myfont.render('SCORE: ', True, (0,0,0))
            self.screen.blit(text,(600,600))
            if getpellet:
                self.pacman.score += 10
            if getBigPellet:
                self.pacman.score += 10

            self.allSprites.draw(self.screen)
            pygame.display.flip()

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
