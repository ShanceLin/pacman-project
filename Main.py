import pygame
import Pacman
import Ghost
import Pellets
import BigPellets

def main():
    pygame.init()
    width = 645
    height = 795
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size()).convert()
    pygame.font.init()
    pacman = Pacman.Pacman("Pacman", 50, 50, "assets/hero_frame1.png")
    ghosts = pygame.sprite.Group()
    ghosts.add (Ghost.Ghost("Ghosts", 100, 100, 10, "assets/ghost.gif"))
    pellets = pygame.sprite.Group()
    pellets.add (Pellets.Pellets("Pellets", 200, 200, "assets/dot.png"))
    bigpellets = pygame.sprite.Group()
    pellets.add (BigPellets.BigPellets("BigPellets", 150, 150, "assets/bigdot.png"))
    state = "ON"
    allsprites = pygame.sprite.Group((pacman), (ghosts), (pellets), (bigpellets))
    score = 0
    ghostIsVulnerable = False

    while True:
        if (state == "ON"):
            roundIsOn = True
            pygame.key.set_repeat(1, 100)
            while (state == "ON"):
                while roundIsOn == True:
                    background.fill((250, 250, 250))
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
                        ghostIsVulnerable = True
                    if (pacman.lives == 0):
                        state = "OFF"
                    allsprites.draw(screen)
                    pygame.display.flip()
        elif (state == "OFF"):
            pass


    #Create an instance on your controller object
main()
