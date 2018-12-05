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

        self.pacman = Pacman.Pacman("Pacman", 325, 525, "assets/foreman1.png", 5)
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
        for q in leftwall:
            self.walls.add(Walls.Walls("assets/wall.png", q))
        topwall = ((25,0),(50,0),(75,0),(100,0),(125,0),(150,0),(175,0),(200,0),(225,0),(250,0),(275,0),(300,0),(325,0),(350,0),(375,0),(400,0),(425,0),(450,0),(475,0),(500,0),(525,0),(550,0),(575,0),(600,0),(625,0))
        for e in topwall:
            self.walls.add(Walls.Walls("assets/wall.png", e))
        rightwall = ((625,25),(625,50),(625,75),(625,100),(625,125),(625,150),(625,175),(625,200),(625,225),(625,250),(625,275),(625,300),(625,350),(625,375),(625,400),(625,425),(625,450),(625,475),(625,500),(625,525),(625,550),(625,575),(625,600),(625,625),(625,650),(625,675))
        for w in rightwall:
            self.walls.add(Walls.Walls("assets/wall.png", w))
        bottomwall = ((0,700),(25,700),(50,700),(75,700),(100,700),(125,700),(150,700),(175,700),(200,700),(225,700),(250,700),(275,700),(300,700),(325,700),(350,700),(375,700),(400,700),(425,700),(450,700),(475,700),(500,700),(525,700),(550,700),(575,700),(600,700),(625,700))
        for t in bottomwall:
            self.walls.add(Walls.Walls("assets/wall.png", t))
        otherwall =((25,350),(50,350),(75,350),(100,350),(125,350),(25,300),(50,300),(75,300),(100,300),(125,300),(25,375),(50,375),(75,375),(100,375),(125,375),(25,400),(50,400),(75,400),(100,400),(125,400),(25,425),(50,425),(75,425),(100,425),(125,425),(25,275),(50,275),(75,275),(100,275),(125,275),(25,250),(50,250),(75,250),(100,250),(125,250),(25,225),(50,225),(75,225),(100,225),(125,225),(325,25),(325,50),(325,75),(325,100),(300,25),(300,50),(300,75),(300,100),(75,75),(75,100),(100,100),(100,75),(50,50),(50,75),(50,100),(75,50),(100,50),(125,50),(125,75),(125,100),(125,150),(100,150),(75,150),(50,150),(50,175),(75,175),(100,175),(125,175),(175,50),(200,50),(225,50),(250,50),(175,75),(200,75),(225,75),(250,75),(175,100),(200,100),(225,100),(250,100),(175,225),(175,200),(175,175),(175,150),(175,250),(175,275),(175,300),(200,225),(200,200),(200,175),(200,150),(200,250),(200,275),(200,300),(250,150),(275,150),(300,150),(325,150),(350,150),(375,150),(500,50),(500,75),(500,100),(525,50),(550,50),(575,50),(525,75),(525,100),(550,75),(550,100),(575,75),(575,100),(450,75),(450,100),(450,50),(425,75),(425,100),(425,50),(400,75),(400,100),(400,50),(375,75),(375,100),(375,50),(575,150),(575,175),(550,150),(550,175),(525,150),(525,175),(500,150),(500,175),(450,150),(450,175),(425,175),(425,150),(450,200),(425,200),(450,225),(425,225),(425,250),(450,250),(425,275),(450,275),(425,300),(450,300),(325,200),(325,175),(300,175),(300,200),(275,175),(250,175),(350,175),(375,175),(300,225),(325,225),(250,225),(225,225),(225,250),(250,250),(400,225),(400,250),(375,250),(375,225),(325,250),(300,250),(500,250),(500,225),(500,275),(500,300),(525,225),(525,250),(525,275),(525,300),(550,225),(550,250),(550,275),(550,300),(500,225),(500,250),(500,275),(500,300),(575,225),(575,250),(575,275),(575,300),(600,300),(600,275),(600,250),(600,225),(600,375),(600,350),(600,400),(600,425),(575,350),(575,375),(575,400),(575,425),(550,350),(550,375),(550,400),(550,425),(525,425),(525,375),(525,400),(525,350),(500,350),(500,375),(500,400),(500,425),(450,425),(450,400),(450,375),(450,350),(425,350),(425,375),(425,400),(425,425),(200,350),(200,375),(200,400),(200,425),(175,375),(175,400),(175,350),(175,425),(250,425),(275,425),(300,425),(325,425),(350,425),(375,425),(250,400),(275,400),(300,400),(325,400),(350,400),(375,400),(300,450),(300,475),(325,475),(325,450),(300,500),(325,500),(250,500),(250,475),(225,500),(225,475),(200,500),(200,475),(175,500),(175,475),(375,500),(375,475),(400,500),(400,475),(425,500),(425,475),(450,475),(450,500),(500,475),(500,500),(525,475),(525,500),(550,475),(550,500),(575,475),(575,500),(525,525),(525,550),(500,525),(500,550),(425,550),(450,550),(525,575),(500,575),(450,575),(425,575),(375,575),(350,575),(325,575),(300,575),(275,575),(250,575),(250,550),(275,550),(300,550),(325,550),(350,550),(375,550),(200,550),(200,575),(175,550),(175,575),(125,550),(125,575),(100,550),(100,575),(125,525),(125,500),(125,475),(100,475),(100,500),(100,525),(75,475),(75,500),(50,475),(50,500),(25,550),(25,575),(50,550),(50,575),(575,550),(600,550),(575,575),(600,575),(450,600),(425,600),(325,600),(300,600),(200,600),(175,600),(175,625),(200,625),(150,625),(100,625),(75,625),(125,625),(300,625),(325,625),(575,625),(50,625),(550,625),(525,625),(500,625),(475,625),(450,625),(425,625),(400,625),(375,625),(250,625),(225,625),(225,650),(200,650),(175,650),(150,650),(125,650),(100,650),(75,650),(50,650),(250,650),(300,650),(325,650),(375,650),(400,650),(425,650),(450,650),(475,650),(500,650),(525,650),(550,650),(575,650),(250,300),(275,300),(250,325),(250,350),(275,350),(300,350),(325,350),(350,350),(375,350),(375,325),(375,300),(350,300))
        for y in otherwall:
            self.walls.add(Walls.Walls("assets/wall.png", y))
        #theres 478 walls rip

        self.score = 0

        numBigpellets = 10
        for i in range(numBigpellets):
            self.bigpellets.add(BigPellets.BigPellets("BigPellets", 150, 150, "assets/bigdot.png"))

        self.walls = Walls.Walls()

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
