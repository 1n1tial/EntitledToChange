import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.normal_stages import Stage, StageSpaceship, StageText

class Fire1Main(Stage):
    def __init__(self):
        Stage.__init__(self)

