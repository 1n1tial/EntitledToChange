import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager

from data.components.spaceship import Spaceship
from data.states.mode_selection import ModeSelectionSpaceship



class StageSelection(State):
    def __init__(self):
        State.__init__(self)
        self.next = None

        self.elements = pygame.sprite.LayeredUpdates()

        self.spaceship = StageSelectionSpaceship(self, (self.elements,))
        
        self.fire_text_list = ['fire1', 'fire2', 'fire-boss']
        self.water_text_list = ['water1', 'water2', 'water3', 'water-boss']
        self.electricity_text_list = ['elec1', 'elec2', 'elec3', 'elec-boss']
        self.suspense_text_list = ['darkness']
        self.finalboss_text_list = ['A Wrinkle In SpaceTime']
        self.stage_text_list = [self.fire_text_list, self.water_text_list, self.electricity_text_list, self.suspense_text_list, self.finalboss_text_list]
        
        setattr(self, 'fire1', StageText(self, 'ARCADECLASSIC', 'fire1', 45, WHITE, [SCREENWIDTH//2, -20], (self.elements,)))
        setattr(self, 'elec1', StageText(self, 'ARCADECLASSIC', 'elec1', 45, WHITE, [SCREENWIDTH//2, -20], (self.elements,)))        
        self.text_list = ['fire1', 'elec1']


        self.current_text = self.text_list[0]
        self.last_switch = 0

        self.bg_color = BLACK

        self.progress_list = [self.fire1]

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        surface.fill(self.bg_color)
        spawn_particles(self.spaceship, 5, 3, 3, surface, (10, 10, 10))
        spawn_particles(self.spaceship, 3, 3, 3, surface, (200, 0, 20))
        self.elements.draw(surface)
        # pygame.draw.rect(surface, (0, 0, 0), self.spaceship.rect, 2)
       
    def update(self, keys, now):
        self.now = now
        self.switchText(keys)
        self.current_text = self.text_list[0]
        self.elements.update(now)
        # self.changeColor(now)
        self.next = self.current_text

    def switchText(self, keys):
        if self.now - self.last_switch >= SWITCH_COOLTIME:
            self.last_switch = self.now
            if keys[pygame.K_UP]:
                current_text = self.text_list.pop(0)
                self.text_list.append(current_text)
            elif keys[pygame.K_DOWN]:
                current_text = self.text_list.pop(len(self.text_list)-1)
                self.text_list.insert(0, current_text)


    def changeColor(self, now):
        pass

    def getEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.next = self.current_text
                self.done = True



class StageSelectionSpaceship(ModeSelectionSpaceship):
    def __init__(self, state, *groups):
        ModeSelectionSpaceship.__init__(self, state, *groups)
        self.particles = []        

    
class StageText(BasicText):
    def __init__(self, state, font, text, size, color, pos, *groups):
        BasicText.__init__(self, state, font, text, size, color, pos, *groups)
        self.vel = 0
        self.hold = 'TOP'
        self.old_idx = 0
        
    def update(self, now, *args):
        if len(self.state.text_list) != 1:
            current_idx = self.state.text_list.index(self.text)
            target_idx = self.state.text_list.index(self.state.current_text)
            if self.hold == 'TOP' and self.text == self.state.current_text:
                if self.old_idx == len(self.state.text_list)-1:
                    self.hold = 'BOTTOM'
                    self.pos[1] = SCREENHEIGHT + 20
                else:
                    self.vel += 2
                    if self.pos[1] >= SCREENHEIGHT//2:
                        self.hold = 'MID'
            if self.hold == 'MID' and self.text == self.state.current_text:
                self.vel = 0
                #self.pos[1] = SCREENHEIGHT//2
            if self.hold == 'MID' and self.text != self.state.text_list:
                if target_idx%len(self.state.text_list) == (current_idx + 1)%len(self.state.text_list):
                    self.vel += 2
                    if self.pos[1] >= SCREENHEIGHT + 20:
                        self.vel = 0
                        self.hold = 'BOTTOM'
                elif target_idx%len(self.state.text_list) == (current_idx - 1)%len(self.state.text_list):
                    self.vel -= 2
                    if self.pos[1] <= -20:
                        self.vel = 0
                        self.hold = 'TOP'
            if self.hold == 'BOTTOM' and self.text == self.state.current_text:
                if self.old_idx == 1:
                    self.hold = 'TOP'
                    self.pos[1] = -20
                else:
                    self.vel -= 2
                    if self.pos[1] <= SCREENHEIGHT//2 + 30:
                        self.hold = 'MID'
            self.old_idx = current_idx
        elif len(self.state.text_list) == 1:
            self.vel += 2
            if self.pos[1] >= SCREENHEIGHT//2:
                self.pos[1] = SCREENHEIGHT//2
                self.vel = 0
        self.pos[1] += self.vel
        super().update(now, *args)