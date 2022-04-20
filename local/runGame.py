"""
runs the tictactoe game
"""
#imports
import pygame, sys
from Assets.gameCode.board import Board
from Assets.gameCode.settings import *

#init
pygame.init()

#init vars
WIDTH, HEIGHT = Miscellaneous.WIDTH, Miscellaneous.HEIGHT
FPS = Miscellaneous.FPS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#start function
def startGame(WIN: pygame.surface) -> None:
    board = Board((WIDTH, HEIGHT))
    while True:#game loop
        clock.tick(FPS)#fps
        for event in pygame.event.get():#loop through events
            if event.type == pygame.QUIT:
                sys.exit()
            elif pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
                board.click()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_BACKSPACE:
                    board.goBack()
                elif event.key == pygame.K_r:
                    board.restart()

        WIN.fill((0, 0, 0))
        if board.draw(WIN):
            return
        pygame.display.update()#update screen