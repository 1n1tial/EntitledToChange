import pygame as pg
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.SETTINGS import *
from data.prepare import *
from data.state_manager import State, StateManager


class TitleScreen(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'MODE_SELECTION'

        self.title_text = GAME_TITLE

    def draw(self, surface, interpolate):
        TITLE_FONT = pg.font.Font(FONT_DICT['ARCADECLASSIC'], 200)
        surface.fill(WHITE)
        surface.blit(TITLE_FONT.render(self.title_text, 0, BLACK), TITLE_FONT.render(self.title_text, 0, BLACK).get_rect(center=SCREENRECT.center))
