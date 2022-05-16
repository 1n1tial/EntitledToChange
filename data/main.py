# import --------------------------------------
from pip import main
import pygame, sys

# define game class
class Game():
    def __init__(self):
        self.running = True
    
    def run(self):
        pass

    def play(self):
        pass



# create game
mainGame = Game()

# main game loop
if mainGame.running():
    mainGame.run()
mainGame.running = False


def quit_game():
    pygame.quit()
    sys.exit()