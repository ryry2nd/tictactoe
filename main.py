#imports
import pygame

#init
pygame.init()

#init vars
WIDTH, HEIGHT = 900, 500
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    #init vars
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        WIN.fill((255, 255, 255))
        pygame.display.update()


if __name__ == '__main__':
    main()