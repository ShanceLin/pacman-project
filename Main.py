import pygame
import Pacman
import Ghost
import Pellets
import BigPellets
import random

def main():
    pygame.init()
    width = 645
    height = 795
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size()).convert()
    clock = pygame.time.Clock()
    pygame.font.init()
    pacman = Pacman.Pacman("Pacman", 322, 510, "assets/hero_frame1.png")
    level = 2
    numghosts = (1 * level)
    ghosts = pygame.sprite.Group()
    for i in range(numghosts):
        ghostx = random.randrange(220, 420)
        ghosty = random.randrange(300, 400)
        ghosts.add (Ghost.Ghost("Ghosts", ghostx, ghosty, 10, "assets/ghost.gif"))
    pellets = pygame.sprite.Group()
    pellets.add (Pellets.Pellets("Pellets", 200, 200, "assets/dot.png"))
    bigpellets = pygame.sprite.Group()
    bigpellets.add (BigPellets.BigPellets("BigPellets", 150, 150, "assets/bigdot.png"))
    gameIsOn = True
    allsprites = pygame.sprite.Group((pacman), (ghosts), (pellets), (bigpellets))
    score = 0
    ghostIsVulnerable = False
    roundIsOn = True
    bluetime = 10


    while gameIsOn == True:
        pygame.key.set_repeat(1, 100)
        while roundIsOn == True:
            background.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP):
                        pacman.move(0)
                    elif (event.key == pygame.K_DOWN):
                        pacman.move(1)
                    elif (event.key == pygame.K_LEFT):
                        pacman.move(2)
                    elif (event.key == pygame.K_RIGHT):
                        pacman.move(3)
            screen.blit(background, (0,0))
            touched = pygame.sprite.spritecollide(pacman, ghosts, True)
            if touched:
                if ghostIsVulnerable == False:
                    pacman.lives -= 1
                    print(pacman.lives)
                    print("reset occurring")
                    pacman.reset()
                elif ghostIsVulnerable == True:
                    print("Ghost died")
            for g in ghosts:
                if g.isBlue:
                    g.checkIfBlue()
            getpellet = pygame.sprite.spritecollide(pacman, pellets, True)
            if getpellet:
                score += 10
                print(score)
            getBigPellet = pygame.sprite.spritecollide(pacman, bigpellets, True)
            if getBigPellet:
                score += 10
                ghostIsVulnerable = True
            if len(pellets) == 0 & len(bigpellets) == 0:
                roundIsOn = False
            if (pacman.lives == 0):
                roundIsOn = False
            allsprites.draw(screen)
            pygame.display.flip()
    if (gameIsOn == False):
        pass


    #Create an instance on your controller object
main()
