import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.states.singleplayer.normal_stages import Stage, StageSpaceship, StageText
from data.controls import spawn_particles

class Fire1Main(Stage):
    def __init__(self):
        Stage.__init__(self)

    def draw(self, surface, interpolate):
        super().draw(surface, interpolate)
        for asteroid in self.asteroids:
            spawn_particles(asteroid, 2, 1, -5, surface, (200, 0, 20))
        