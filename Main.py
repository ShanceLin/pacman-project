import controller
import pygame
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False

    fontTitle = pygame.font.SysFont("crackman", 72)
    fontOther = pygame.font.SysFont("arcadeclassic", 52)
    title = fontTitle.render("FORE-MAN", True, (0, 0, 0))
    start = fontOther.render("click X to start", True, (0, 0, 0))
    instructions = fontOther.render("use ARROWKEYS to move", True, (0, 0, 0))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        screen.fill((15, 9, 119))
        screen.blit(title, (170, 150))
        screen.blit(start, (175, 300))
        screen.blit(instructions, (90, 350))
        pygame.display.flip()
        clock.tick(60)
    main_window = controller.Controller()
    main_window.mainLoop()

main()