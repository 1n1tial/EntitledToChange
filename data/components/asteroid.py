import pygame, os, sys
from random import randint

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.controls import CONTROL1
from data.SETTINGS import *
from data.prepare import *

class Asteroid(BasicSprite):
    def __init__(self, state, *groups):
        self._layer = Layer_dict['Asteroid']
        self.groups = (state.elements, state.asteroids)
        BasicSprite.__init__(self, (randint(20, SCREENWIDTH-20), 20 ), (ASTEROID_WIDTH, ASTEROID_HEIGHT), *groups)
        self.state = state
        self.image = pygame.transform.scale(IMG_DICT['sprite']['asteroid'], (ASTEROID_WIDTH, ASTEROID_HEIGHT))

    def move(self):
        self.new_pos[1] += 9

    def checkOutOfScreen(self):
        if self.rect.top > SCREENHEIGHT:
            self.kill()

    def update(self, now, *args):
        self.old_pos = self.new_pos[:]
        self.move()
        self.rect.topleft = self.new_pos
        self.checkOutOfScreen()
        self.now = now

