import controller
import pygame
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    done = False

    fontTitle = pygame.font.SysFont("helvetica", 72)
    fontOther = pygame.font.SysFont("helvectica", 52)
    title = fontTitle.render("FOREMAN", True, (0, 0, 0))
    start = fontOther.render("Press ENTER to start", True, (0, 0, 0))
    instructions = fontOther.render("press I for instructions", True, (0, 0, 0))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        screen.fill((15, 9, 119))
        screen.blit(title, (200, 150))
        screen.blit(start, (120, 250))
        screen.blit(instructions, (200, 350))
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_i):
                instructions = fontOther.render("press I for instructions", True, (0, 0, 0))
                screen.blit(instructions, (200, 350))
                pygame.display.flip()

        pygame.display.flip()
        clock.tick(60)
    main_window = controller.Controller()
    main_window.mainLoop()

main()