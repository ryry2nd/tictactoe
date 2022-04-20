"""
main function
"""
#imports
import pygame, sys, os
from threading import Thread
from Assets.gameCode.settings import *
from local.runGame import startGame
from Assets.gameCode.clickWindow import clickWindow
#inits
pygame.init()
pygame.font.init()

#constints
WIDTH, HEIGHT = Miscellaneous.WIDTH, Miscellaneous.HEIGHT
FPS = Miscellaneous.FPS

#set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")
#pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'textures', 'Icon.png')))

#main function
def main():
    clock = pygame.time.Clock()#defines a clock
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():#loops through the events
            if event.type == pygame.QUIT:#if it is quit, quit
                sys.exit()

            elif event.type == pygame.KEYDOWN:# runs when a key is pressed
                if event.key == pygame.K_ESCAPE:# if escape is pressed, escape
                    sys.exit()

        WIN.fill((0, 0, 0))# fills the screen

        #if the box is clicked, start a local game
        if clickWindow(WIN, (100, 100), "Local", "Game"):
            startGame(WIN)

        #if the box is clocked go to the find a game code
        elif clickWindow(WIN, (300, 100), "Join a", "Server"):
            pass

        #if the box is clicked make a server
        elif clickWindow(WIN, (500, 100), "Be a", "Server"):
            pass
        
        pygame.display.update()#update the display

print(var("r"))

#if the code is not being imported run the code
if __name__ == '__main__':
    main()