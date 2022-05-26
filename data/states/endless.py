import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager

from data.components.spaceship import Spaceship


class Endless(State):
    def __init__(self):
        State.__init__(self)
        self.next = None
        self.elements = pygame.sprite.LayeredUpdates()
        self.spaceship = EndlessSpaceship(self, (self.elements,))
        
        self.bg_color = BLACK

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        surface.fill(self.bg_color)
        spawn_particles(self.spaceship, 3, 3, 3, surface, (200, 0, 20))
        self.elements.draw(surface)

    def update(self, keys, now):
        self.now = now
        if keys[pygame.K_SPACE]:
            self.spaceship.shoot()
        self.elements.update(now)

    def getEvent(self, event):
        pass


class EndlessSpaceship(Spaceship):
    def __init__(self, state, *groups):
        Spaceship.__init__(self, state, *groups)
        self.particles = []

    def update(self, now, *args):
        super().update(now, *args)

    