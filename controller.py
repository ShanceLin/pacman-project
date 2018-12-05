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
    def __init__(self, width=750, height=825):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.pacmanspeed = 6.25
        self.pacman = Pacman.Pacman("Pacman", 325, 525, "assets/foreman1.png", self.pacmanspeed)
        level = 1

        self.ghosts = pygame.sprite.Group()
        numGhosts = (1 * level)
        ghostspeed = 10
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

        self.score = 0

        self.all_sprites = pygame.sprite.Group((self.pacman,) + tuple(self.ghosts) + tuple(self.pellets) + tuple(self.bigpellets))
        self.state = "GAME"


        self.font = pygame.font.SysFont("Times New Roman", 25)

        self.roundIsOn = True
        self.blueTime = 10
        self.ghostIsVulnerable = False

        self.allSprites = pygame.sprite.Group((self.pacman,) + tuple(self.ghosts) + tuple(self.pellets) + tuple(self.bigpellets) + tuple(self.walls))
        self.state = "GAME"
        self.z = 0
        self.ghostKill = False
        self.colliding = False

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def messageDisplay(text):
        largeText = pygame.font.Font('Times New Roman',115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        game_loop()

    def gameIntro():
        intro = True
        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(white)
            largeText = pygame.font.Font('Times New Roman',115)
            TextSurf, TextRect = text_objects("FOREMAN", largeText)
            TextRect.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(15)

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
                        self.pacman.moveUp()
                    elif (event.key == pygame.K_DOWN):
                        self.pacman.moveDown()
                    elif (event.key == pygame.K_LEFT):
                        self.pacman.moveLeft()
                    elif (event.key == pygame.K_RIGHT):
                        self.pacman.moveRight()

            #checks for collisions with walls


            #checks for ghost vulnerability
            #self.pacman.getSurface()

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

            #checks for contact betwen ghosts

            touched = pygame.sprite.spritecollide(self.pacman, self.ghosts, self.ghostKill)
            if touched:
                if self.ghostIsVulnerable == False:
                    self.pacman.lives -= 1
                    print(self.pacman.lives)
                    print("reset occuring")

                    self.pacman.reset()

                    self.all_sprites.update()

                elif self.ghostIsVulnerable == True:
                    self.ghostKill = True
                    print("Ghost died")
            self.allSprites.draw(self.screen)
            pygame.display.flip()

            #displays score
            myfont = pygame.font.SysFont(None, 30)
            text = "%5d Points %2d Lifes" % (0, self.pacman.lives)
            text_img = self.font.render(text, True, (100, 100, 0))
            self.screen.blit(text_img, (0, 0))

            if getpellet:
                self.score += 10
            if getBigPellet:
                self.score += 100


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
                self.score += 10
            if getBigPellet:
                self.score += 10

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
