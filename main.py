#imports
import pygame, sys
from Assets.gameCode.gui.board import Board

#init
pygame.init()

#init vars
WIDTH, HEIGHT = 900, 500
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#main function
def main():
    #init vars
    board = Board((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:#game loop
        clock.tick(FPS)#fps
        for event in pygame.event.get():#loop through events
            if event.type == pygame.QUIT:
                sys.exit()
            elif pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
                board.click()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    board.goBack()
                elif event.key == pygame.K_r:
                    board.restart()

        WIN.fill((0, 0, 0))
        board.draw(WIN)
        pygame.display.update()#update screen

if __name__ == '__main__':# if it is not being imported, run main
    main()