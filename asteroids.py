import pygame, sys

from data.main import mainLoop

if __name__ == '__main__':
    mainLoop()
    pygame.quit()
    sys.exit('game closed by player input')
