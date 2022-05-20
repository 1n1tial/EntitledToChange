import pygame, os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.controls import CONTROL1, BasicSprite, spawn_particles
from data.SETTINGS import *
from data.prepare import *

class Spaceship(BasicSprite):
    def __init__(self, *groups):
        BasicSprite.__init__(self, (SCREENWIDTH//2 - PLAYER_WIDTH//2, SCREENHEIGHT*8//10), (PLAYER_WIDTH, PLAYER_WIDTH), *groups)
        self.controls = CONTROL1
        self.image = pygame.transform.scale(IMG_DICT['sprite']['spaceship'], (PLAYER_WIDTH, PLAYER_WIDTH))

    def move(self):
        self.vel_x = 0
        keystate = pg.key.get_pressed()
        if keystate[self.controls['LEFT']]:
            self.vel_x -= SPACESHIP_VEL_X
        if keystate[self.controls['RIGHT']]:
            self.vel_x += SPACESHIP_VEL_X
        if keystate[self.controls['SHOOT']]:
            self.prepare_liftoff = True

        self.new_pos[0] += self.vel_x

    def checkCollision(self):
        if self.rect.right > SCREENWIDTH:
            self.rect.right = SCREENWIDTH
            self.new_pos[0] = SCREENWIDTH - self.rect.width
        if self.rect.left < 0:
            self.rect.left = 0
            self.new_pos[0] = 0

    def update(self, now, *args):
        self.old_pos = self.new_pos[:]
        self.move()
        self.rect.topleft = self.new_pos
        self.checkCollision()