import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager

from data.components.spaceship import Spaceship


class ModeSelection(State):
    def __init__(self):
        State.__init__(self)
        self.next = None

        self.spaceship = ModeSelectionSpaceship()
        self.elements = pygame.sprite.LayeredUpdates()
        self.elements.add(self.spaceship, layer=1)
        
        self.bg_color = WHITE

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        surface.fill(self.bg_color)
        self.elements.draw(surface)
        spawn_particles(self.spaceship, 3, 0.1, 4, surface)

    def update(self, keys, now):
        self.now = now
        self.elements.update(now)


class ModeSelectionSpaceship(Spaceship):
    def __init__(self, *groups):
        Spaceship.__init__(self, *groups)
        self.particles = []

    def draw(self, surface):
        super().draw()

    def update(self, now, *args):
        super().update(now, *args)
        
        

