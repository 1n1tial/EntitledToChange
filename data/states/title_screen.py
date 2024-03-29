import pygame as pg
import os, sys
from math import sin, pi

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.components.spaceship import Spaceship

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager


class TitleScreen(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'MODE_SELECTION'

        self.title_text = GAME_TITLE

        self.elements = pg.sprite.LayeredUpdates()
        self.spaceship = TitleSpaceship(self, (self.elements,))
        self.presskeytext = PressKeyText(self, (self.elements,))

        self.space_hold_time = 2000
        self.space_hold = False
        self.hold_space_start = 0

        self.bg_color = WHITE

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        TITLE_FONT = pg.font.Font(FONT_DICT['ARCADECLASSIC'], 100)
        surface.fill(self.bg_color)
        RENDERED_TITLE_FONT = TITLE_FONT.render(self.title_text, 0, WHITE)
        surface.blit(RENDERED_TITLE_FONT, RENDERED_TITLE_FONT.get_rect(center=SCREENRECT.center))
        self.elements.draw(surface)

    def update(self, keys, now):
        self.now = now
        self.elements.update(now)

    def checkSpaceHold(self, now, event):
        if event.type == pg.KEYDOWN:  
            self.hold_space_start = now
            print(self.hold_space_start)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE] and not self.space_hold:
            self.space_hold = True
        elif keystate[pg.K_SPACE] and self.space_hold:
            dt = now - self.hold_space_start
            self.bg_color = 3*(int(255 - (2-2**(1-dt/self.space_hold_time))*255),)
            if now - self.hold_space_start >= self.space_hold_time:
                self.done = True
        elif not keystate[pg.K_SPACE] and self.space_hold:
            self.space_hold = False
            self.bg_color = WHITE
            
    def getEvent(self, event):
        self.checkSpaceHold(self.now, event)


class TitleSpaceship(Spaceship):
    def __init__(self, state, *groups):
        Spaceship.__init__(self, state, *groups)
        
    def update(self, now, *args):
        pass


class PressKeyText(BasicText):
    def __init__(self, state, *groups):
        BasicText.__init__(self, state, 'ARCADECLASSIC', 'HOLD SPACE TO START', 30, BLACK, (SCREENWIDTH//2, SCREENHEIGHT*7//10), *groups)
        self.decrease_time = 1000
        self.decrease_rate = 0.03
    
    def update(self, now, *args):
        self.size = 40 + abs(now % (2*self.decrease_time) - self.decrease_time)*self.decrease_rate
        # self.size = 40 + int(sin(5*now/self.decrease_time)*self.decrease_diff)
        self.image, self.rect = render_font('ARCADECLASSIC', 'HOLD SPACE TO START', self.size, BLACK, (SCREENWIDTH//2, SCREENHEIGHT*7//10))
    

    

