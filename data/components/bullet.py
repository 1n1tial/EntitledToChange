import pygame, os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.controls import CONTROL1
from data.SETTINGS import *
from data.prepare import *


class Bullet(BasicSprite):
    def __init__(self, state, vel, *groups):
        self._layer = Layer_dict['Bullet']
        self.groups = (state.elements, state.bullets)
        BasicSprite.__init__(self, [state.spaceship.rect.midtop[0]-BULLET_WIDTH//2, state.spaceship.rect.midtop[1]-BULLET_HEIGHT//2], [BULLET_WIDTH, BULLET_HEIGHT], *groups)
        self.state = state
        self.image = pygame.transform.scale(IMG_DICT['sprite']['bullet'], (BULLET_WIDTH, BULLET_HEIGHT))

        self.vel = vel

    def move(self):
        self.new_pos[1] -= self.vel

    def checkOutOfScreen(self):
        if self.pos[1] >= SCREENHEIGHT + 100 or self.pos[1] <= -100:
            self.kill()

    def update(self, now, *args):
        self.old_pos = self.new_pos[:]
        self.move()
        self.rect.midtop = self.new_pos


