import pygame as pg
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.components.spaceship import Spaceship

from data.SETTINGS import *
from data.prepare import *
from data.controls import Timer
from data.state_manager import State, StateManager


class TitleScreen(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'MODE_SELECTION'

        self.title_text = GAME_TITLE

        self.spaceship = TitleSpaceship()
        self.elements = pg.sprite.LayeredUpdates()
        self.elements.add(self.spaceship, layer=1)

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now
        self.timer = Timer(1, 1)

    def draw(self, surface, interpolate):
        TITLE_FONT = pg.font.Font(FONT_DICT['ARCADECLASSIC'], 100)
        surface.fill(WHITE)
        RENDERED_TITLE_FONT = TITLE_FONT.render(self.title_text, 0, WHITE)
        surface.blit(RENDERED_TITLE_FONT, RENDERED_TITLE_FONT.get_rect(center=SCREENRECT.center))
        self.elements.draw(surface)

    def update(self, keys, now):
        self.now = now
        self.elements.update(now)

    def getEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.done = True

class TitleSpaceship(Spaceship):
    def __init__(self, *groups):
        Spaceship.__init__(self, *groups)
        
    def update(self, now, *args):
        pass
    

    

