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
    def __init__(self, width=650, height=825):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        pygame.font.init()

        self.pacmanspeed = 5
        self.pacman = Pacman.Pacman("Pacman", 325, 525, "assets/foreman1.png", self.pacmanspeed)
        level = 1

        self.ghosts = pygame.sprite.Group()
        numGhosts = (1 * level)
        ghostspeed = 10
        for k in range(numGhosts):
            x = random.randrange(275, 350)
            self.ghosts.add(Ghost.Ghost("Ghosts", x, 325, ghostspeed, "assets/carsprite.png"))
        pelletcount = 0
        self.pellets = pygame.sprite.Group()
        pelletlocations = ((25,25),(25,50),(25,100),(25,125),(25,150),(25,175),(25,200),(50,25),(50,125),(75,25),(100,25),(125,25),(150,25),(175,25),(200,25),(225,25),(250,25),(275,25),(150,50),(150,75),(150,100),(150,150),(150,175),(150,200),(150,225),(150,250),(150,125),(150,275),(150,300),(150,325),(150,350),(150,375),(150,400),(150,425),(150,450),(150,475),(150,500),(150,525),(150,550),(150,575),(150,600),(150,675),(125,675),(100,675),(75,675),(50,675),(25,675),(175,675),(200,675),(225,675),(250,675),(275,675),(300,675),(325,675),(350,675),(375,675),(400,675),(425,675),(450,675),(475,675),(500,675),(525,675),(550,675),(575,675),(600,675),(600,650),(600,625),(600,600),(575,600),(550,600),(525,600),(500,600),(475,600),(475,575),(475,550),(475,525),(475,500),(475,475),(475,450),(475,425),(475,400),(475,375),(475,350),(475,325),(475,300),(475,275),(475,250),(475,225),(475,200),(475,175),(475,150),(475,100),(475,75),(475,50),(475,125),(475,25),(450,25),(425,25),(400,25),(375,25),(350,25),(500,25),(525,25),(550,25),(575,25),(600,25),(600,50),(600,100),(600,125),(600,150),(600,175),(600,200),(575,125),(550,125),(525,125),(500,125),(450,125),(425,125),(400,125),(375,125),(350,125),(325,125),(300,125),(275,125),(250,125),(225,125),(200,125),(175,125),(125,125),(100,125),(75,125),(350,100),(350,75),(350,50),(275,75),(275,100),(275,50),(225,150),(225,175),(225,200),(250,200),(275,200),(350,200),(375,200),(400,200),(400,175),(400,150),(75,200),(50,200),(100,200),(125,200),(575,200),(550,200),(525,200),(500,200),(275,525),(250,525),(225,525),(200,525),(175,525),(75,525),(50,525),(25,500),(25,600),(25,625),(25,650),(25,450),(25,475),(50,450),(75,450),(100,450),(125,450),(175,450),(200,450),(225,450),(250,450),(275,450),(275,475),(275,500),(275,625),(275,600),(275,650),(250,600),(225,600),(225,575),(225,550),(100,600),(125,600),(75,600),(50,600),(75,575),(75,550),(350,525),(375,525),(400,525),(425,525),(450,525),(350,500),(350,475),(350,450),(400,550),(400,575),(400,600),(375,600),(350,600),(350,625),(350,650),(400,450),(425,450),(375,450),(450,450),(500,450),(525,450),(550,450),(575,450),(600,450),(600,475),(600,500),(550,525),(575,525),(550,550),(550,575))

        for p in pelletlocations:
            self.pellets.add(Pellets.Pellets("Pellets", "assets/dot.png", p))
            pelletcount +=1
        print(pelletcount)
        self.bigpellets = pygame.sprite.Group()

        bigpelletlocations = ((25,75),(600,75), (25, 525), (600,525))
        for z in bigpelletlocations:
            self.bigpellets.add(BigPellets.BigPellets("BigPellets", "assets/bigdot.png", z))

        self.walls = pygame.sprite.Group()
        leftwall = ((0,0),(0,25),(0,50),(0,75),(0,100),(0,125),(0,150),(0,175),(0,200),(0,225),(0,250),(0,275),(0,300),(0,350),(0,375),(0,400),(0,425),(0,450),(0,475),(0,500),(0,525),(0,550),(0,575),(0,600),(0,625),(0,650),(0,675))
        for q in Walls.Walls.leftwall():
            self.walls.add(Walls.Walls("assets/wall.png", q))

        for e in Walls.Walls.topwall():
            self.walls.add(Walls.Walls("assets/wall.png", e))

        for w in Walls.Walls.rightwall():
            self.walls.add(Walls.Walls("assets/wall.png", w))

        for t in Walls.Walls.bottomwall():
            self.walls.add(Walls.Walls("assets/wall.png", t))
        for y in Walls.Walls.otherwalls():
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
            self.background.fill((250, 250, 250))

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
            touched = pygame.sprite.spritecollide(self.pacman, self.ghosts, True)
            if touched:
                if self.ghostIsVulnerable == False:
                    self.pacman.lives -= 1
                    print(self.pacman.lives)
                    print("reset occuring")

                    self.pacman.reset()

                    self.all_sprites.update()

                elif self.ghostIsVulnerable == True:
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
