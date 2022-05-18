import pygame as pg
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.SETTINGS import *
from data.prepare import *
from data.state_manager import StateManager, State


class Splash(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'TITLE'
        
        self.alpha = 0
        self.time_out = 4
        self.alpha_gradient = ALPHA_GRADIENT

        self.image = IMG_DICT['splash']['pygame_logo'].copy().convert()
        self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect(center=SCREENRECT.center)

    def update(self, keys, now):
        self.now = now
        self.alpha = min(255, self.alpha + self.alpha_gradient) 
        self.image.set_alpha(self.alpha)
        if self.now - self.start_time > 1000 * self.time_out:
            self.done = True

    def draw(self, surface, interpolate):
        surface.fill(BLACK)
        surface.blit(self.image, self.rect)

    def getEvent(self, event):
        self.done = event.type == pygame.KEYDOWN
