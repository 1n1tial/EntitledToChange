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

        self.elements = pygame.sprite.LayeredUpdates()

        self.spaceship = ModeSelectionSpaceship(self, (self.elements,))
        self.multiplayer = ModeText(self, 'ARCADECLASSIC', 'MULTIPLAYER', 30, WHITE, [SCREENWIDTH//2, -20], (self.elements,))
        self.speedrun = ModeText(self, 'ARCADECLASSIC', 'SPEEDRUN', 30, WHITE, [SCREENWIDTH//2, -20], (self.elements,))
        self.endless = ModeText(self, 'ARCADECLASSIC', 'ENDLESS', 30, WHITE, [SCREENWIDTH//2, -20], (self.elements,))
        self.singleplayer = ModeText(self, 'ARCADECLASSIC', 'SINGLEPLAYER', 30, WHITE,[SCREENWIDTH//2, -20], (self.elements,))

        self.text_list = ['MULTIPLAYER', 'SPEEDRUN', 'ENDLESS', 'SINGLEPLAYER']
        self.current_text = self.text_list[0]
        self.last_switch = 0

        self.bg_color = BLACK

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        surface.fill(self.bg_color)
        spawn_particles(self.spaceship, 3, 3, 3, surface, (200, 0, 20))
        self.elements.draw(surface)
        # pygame.draw.rect(surface, (0, 0, 0), self.spaceship.rect, 2)
       
    def update(self, keys, now):
        self.now = now
        if now - self.last_switch >= SWITCH_COOLTIME:
            self.last_switch = now
            self.switchText(keys)
        self.current_text = self.text_list[0]
        self.elements.update(now)
        self.changeColor(now)

    def switchText(self, keys):
        if keys[pygame.K_UP]:
            current_text = self.text_list.pop(0)
            self.text_list.append(current_text)
        elif keys[pygame.K_DOWN]:
            current_text = self.text_list.pop(3)
            self.text_list.insert(0, current_text)


    def changeColor(self, now):
        dt = now - self.start_time
        dt = dt % LOOP_TIME
        if 0 <= dt < ONE_COLOR_TIME:
            self.bg_color = BLACK
        elif ONE_COLOR_TIME <= dt < ONE_COLOR_TIME + CHANGE_TIME:
            self.bg_color = (MAX_COLOR*(dt - ONE_COLOR_TIME)/CHANGE_TIME,)*3
        elif ONE_COLOR_TIME + CHANGE_TIME <= dt < ONE_COLOR_TIME*2 + CHANGE_TIME:
            self.bg_color = (MAX_COLOR,)*3
        else:
            self.bg_color = (MAX_COLOR - MAX_COLOR*(dt - ONE_COLOR_TIME*2 - CHANGE_TIME)/CHANGE_TIME,)*3

    def getEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                self.next = self.current_text
                self.done = True



class ModeSelectionSpaceship(Spaceship):
    def __init__(self, state, *groups):
        Spaceship.__init__(self, state, *groups)
        self.particles = []

    def update(self, now, *args):
        super().update(now, *args)

    def shoot(self):
        if self.now - self.last_shot >= SHOOT_COOLDOWN:
            pass
        
    
class ModeText(BasicText):
    def __init__(self, state, font, text, size, color, pos, *groups):
        BasicText.__init__(self, state, font, text, size, color, pos, *groups)
        self.vel = 0
        self.hold = 'TOP'
        self.old_idx = 0
        
    def update(self, now, *args):
        current_idx = self.state.text_list.index(self.text)
        target_idx = self.state.text_list.index(self.state.current_text)
        if self.hold == 'TOP' and self.text == self.state.current_text:
            if self.old_idx == 3:
                self.hold = 'BOTTOM'
            else:
                self.vel += 3
                if self.pos[1] >= SCREENHEIGHT//2:
                    self.hold = 'MID'
        if self.hold == 'MID' and self.text == self.state.current_text:
            self.vel = 0
            self.pos[1] = SCREENHEIGHT//2
        if self.hold == 'MID' and self.text != self.state.text_list:
            if target_idx%4 == (current_idx + 1)%4:
                self.vel += 3
                if self.pos[1] >= SCREENHEIGHT + 20:
                    self.vel = 0
                    self.pos[1] = SCREENHEIGHT + 20
                    self.hold = 'BOTTOM'
            elif target_idx%4 == (current_idx - 1)%4:
                self.vel -= 3
                if self.pos[1] <= -20:
                    self.vel = 0
                    self.pos[1] = -20
                    self.hold = 'TOP'
        if self.hold == 'BOTTOM' and self.text == self.state.current_text:
            if self.old_idx == 1:
                self.hold = 'TOP'
            else:
                self.vel -= 3
                if self.pos[1] <= SCREENHEIGHT//2:
                    self.hold = 'MID'
        self.old_idx = current_idx
        self.pos[1] += self.vel
        super().update(now, *args)

    
        
        

