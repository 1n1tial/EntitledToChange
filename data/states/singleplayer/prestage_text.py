import pygame
import os, sys, random

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager

class PreStageText(State):
    def __init__(self):
        State.__init__(self)
        self.next = None

        self.elements = pygame.sprite.LayeredUpdates()
        
        self.text_list = None
        self.text_interval = 50
        self.box_reveal_time = 500
        self.text_state = 'printing'
        self.text_num = 0
        self.text_counter = 0
        self.text_ch_num = 0
        
        self.max_box_width = 500
        self.box_height = 100


        self.bg_color = BLACK

    def update_text_box(self, now):
        dt = now - self.start_time
        if dt <= self.box_reveal_time:
            self.box_width = self.max_box_width*dt/self.box_reveal_time
        else:
            self.box_width = self.max_box_width
    

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        surface.fill(self.bg_color)
        pygame.draw.rect(surface, WHITE, pygame.Rect(SCREENWIDTH//2 - self.box_width//2, SCREENHEIGHT*4//5 - self.box_height//2, self.box_width, self.box_height))
        self.elements.draw(surface)
       
    def update(self, keys, now):
        self.now = now
        self.update_text_box(now)
        
        try:
            self.current_text = self.text_list[self.text_num]
            
            if self.text_state == 'printing':
                if now - self.text_counter >= self.text_interval and self.text_ch_num <= len(self.current_text):
                    self.text_counter = now
                    self.text_ch_num += 1
                    self.elements.empty()
                    BasicText(self, '나눔손글씨 바른히피', self.current_text[0:self.text_ch_num+1], 20, BLACK, [SCREENWIDTH//2, SCREENHEIGHT*4//5], (self.elements,))
                if self.text_ch_num >= len(self.current_text):
                    self.text_state = 'done'
            if self.text_state == 'done':
                self.elements.empty()
                BasicText(self, '나눔손글씨 바른히피', self.current_text, 20, BLACK, [SCREENWIDTH//2, SCREENHEIGHT*4//5], (self.elements,))
        
        except IndexError:
            self.done = True

        self.elements.update(now)


    def getEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.text_state == 'printing':
                    self.text_state = 'done'
                elif self.text_state == 'done':
                    self.text_num += 1
                    self.text_state = 'printing'
                    self.text_counter = 0
                    self.text_ch_num = 0
        
