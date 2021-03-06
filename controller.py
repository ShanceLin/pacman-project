import sys
import pygame
import Pacman
import Ghost
import Pellets
import BigPellets
import Walls
import random
import Lives
import random

class Controller:
    def __init__(self, width=775, height=825):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.pacmanspeed = 25
        self.pacman = Pacman.Pacman("Pacman", 325, 525, "assets/foreman1.png", self.pacmanspeed)
        level = 5

        self.ghosts = pygame.sprite.Group()
        numGhosts = (2 * level)
        ghostspeed = 5
        for k in range(numGhosts):
            x = random.randrange(275, 350)
            self.ghosts.add(Ghost.Ghost("Ghosts", x, 325, 25, "assets/carsprite.png"))
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

        self.isVulnerable = pygame.sprite.Group()
        self.isVulnerable.add(Lives.livesRemaining(7000, 7000, "assets/ghost.gif"))

        self.font = pygame.font.SysFont("Times New Roman", 25)
        self.timer = 0
        self.roundIsOn = True
        self.blueTime = 10
        self.ghostIsVulnerable = False

        self.allSprites = pygame.sprite.Group((self.pacman,) + tuple(self.ghosts) + tuple(self.pellets) + tuple(self.bigpellets) + tuple(self.walls) + tuple(self.livesRemaining) + (self.isVulnerable,))
        self.state = "GAME"
        self.z = 0
        self.ghostKill = False
        self.colliding = False
        self.score = 0

    def mainLoop(self):
        """
        This is the main loop of the game
        arg: self
        return: None
        """
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """
        This is the main loop of the game. This checks for sprite collisions, updates sprites, redraws the screen, etc.
        arg: self
        return: None
        """
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
                    for q in self.ghosts:
                        q.reset()

                    self.allSprites.update()

                elif self.ghostIsVulnerable == True:
                    self.ghostKill = True
                    print("Ghost died")

            #redraws screen
            self.allSprites.draw(self.screen)
            pygame.display.flip()

            myfont = pygame.font.SysFont(None, 30)
            text = "%5d Points %2d Lifes" % (0, self.pacman.lives)
            text_img = self.font.render(text, True, (100, 100, 0))
            self.screen.blit(text_img, (0, 0))
            if getpellet:
                self.score += 10
            if getBigPellet:
                self.score += 100
                self.timer += 300
                for g in self.isVulnerable:
                    g.Vulnerable()

            if self.timer > 0:
                self.timer -=1
            if self.timer == 0:
                self.ghostIsVulnerable = False
                for g in self.isVulnerable:
                    g.resetVul()


            for g in self.ghosts:
                g.update()
            self.screen.blit(self.background, (0, 0))
            if(self.pacman.lives == 0):
                self.state = "GAMEOVER"


            #displays score
            myfont = pygame.font.SysFont(None, 25)
            text = myfont.render(('SCORE: '+ str(self.score)), True, (250,250,250))
            self.screen.blit(text,(650,100))
            if getpellet:
                self.score += 10
            if getBigPellet:
                self.score += 10

            self.allSprites.draw(self.screen)
            pygame.display.flip()


    def gameOver(self):
        """
        Infinite loop that will end the game and exit the system
        arg: self
        return: None
        """
        self.pacman.kill()
        self.background.fill((0, 0, 0))
        myfont = pygame.font.SysFont(None, 100)
        message = myfont.render('Game Over', False, (250,0,0))
        self.screen.blit(message, (150,300))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
