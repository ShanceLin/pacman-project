import pygame

def main():
    pygame.init()
    width = 480
    height = 640
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size()).convert()
    pygame.font.init()
    pacman = Pacman.Pacman("Pacman", 50, 50)
    state = "ON"

    while True:
        if (state == "ON"):
            pygame.key.set_repeat(1, 100)
            while (self.state == "ON"):
                
        elif (state == "OFF"):
            pass


    #Create an instance on your controller object
main()
