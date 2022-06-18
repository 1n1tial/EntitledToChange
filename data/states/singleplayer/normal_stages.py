import pygame
import os, sys, random

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager

from data.components.spaceship import Spaceship
from data.components.asteroid import Asteroid
from data.components.bars import draw_health_bar


class Stage(State):
    def __init__(self):
        State.__init__(self)
        self.next = None

        self.state = 'running' 
        # text printing related-------------
        self.current_text_list_idx = 0
        self.text_list_array = [['asdf'], ['asdf']]
        self.text_list = self.text_list_array[self.current_text_list_idx]
        self.text_interval = 50
        self.box_reveal_time = 500
        self.text_state = 'printing'
        self.text_num = 0
        self.text_counter = 0
        self.text_ch_num = 0
        
        self.max_box_width = 500
        self.box_height = 100
        self.print_texts = pygame.sprite.Group()

        self.elements = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        self.spaceship = StageSpaceship(self, (self.elements,))

        self.last_spawn = 0

        self.bg_color = BLACK

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def draw(self, surface, interpolate):
        surface.fill(self.bg_color)
        spawn_particles(self.spaceship, 5, 3, 3, surface, (10, 10, 10))
        spawn_particles(self.spaceship, 3, 3, 3, surface, (20, 0, 200))
        for bullet in self.bullets:
            for i in range(10):
                screen.blit(circle_surf(BULLET_LIGHTING_RADIUS*i, (20, 20, 20)), (bullet.rect.centerx - BULLET_LIGHTING_RADIUS*i, bullet.rect.y), special_flags=BLEND_RGBA_ADD)
        draw_health_bar(surface, 30, 30, 20, 400, self.spaceship)
        if self.state == 'texting':
            pygame.draw.rect(surface, WHITE, pygame.Rect(SCREENWIDTH//2 - self.box_width//2, SCREENHEIGHT*4//5 - self.box_height//2, self.box_width, self.box_height))
            self.print_texts.draw(surface)
        self.elements.draw(surface)
       
    def print_text(self, now):
        pass

    def update(self, keys, now):
        if not self.spaceship.is_alive:
            self.done = True
        self.print_text(now)
        if self.state == 'running':
            self.now = now
            self.spawnAsteroid()
            self.checkCollision()
            self.elements.update(now)
        elif self.state == 'texting':
            self.now = now
            self.update_text_box(now)
            
            try:
                self.current_text = self.text_list[self.text_num]
                
                if self.text_state == 'printing':
                    if now - self.text_counter >= self.text_interval and self.text_ch_num <= len(self.current_text):
                        self.text_counter = now
                        self.text_ch_num += 1
                        self.print_texts.empty()
                        BasicText(self, '나눔손글씨 바른히피', self.current_text[0:self.text_ch_num+1], 20, BLACK, [SCREENWIDTH//2, SCREENHEIGHT*4//5], (self.print_texts,))
                    if self.text_ch_num >= len(self.current_text):
                        self.text_state = 'done'
                if self.text_state == 'done':
                    self.print_texts.empty()
                    BasicText(self, '나눔손글씨 바른히피', self.current_text, 20, BLACK, [SCREENWIDTH//2, SCREENHEIGHT*4//5], (self.print_texts,))
            
            except IndexError:
                self.state = 'running'
                self.print_texts.empty()
                try:
                    self.current_text_list_idx += 1
                    self.text_list = self.text_list_array[self.current_text_list_idx]
                except IndexError:
                    print(1)
                self.text_ch_num = 0
                self.text_num = 0

            self.print_texts.update(now)



    def spawnAsteroid(self):
        if self.now - self.last_spawn >= random.randint(1500, 3000):
            Asteroid(self, (self.elements, self.asteroids))
            self.last_spawn = self.now

    def checkCollision(self):
        hits = pygame.sprite.spritecollide(self.spaceship, self.asteroids, True, pygame.sprite.collide_circle)
        for hit in hits:
            self.spaceship.damage(10)

        hits = pygame.sprite.groupcollide(self.asteroids, self.bullets, True, True)
    
    def getEvent(self, event):
        if self.state == 'texting':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.text_state == 'printing':
                        self.text_state = 'done'
                    elif self.text_state == 'done':
                        self.text_num += 1
                        self.text_state = 'printing'
                        self.text_counter = 0
                        self.text_ch_num = 0

    def update_text_box(self, now):
        dt = now - self.text_start_time
        if dt <= self.box_reveal_time:
            self.box_width = self.max_box_width*dt/self.box_reveal_time
        else:
            self.box_width = self.max_box_width


class StageSpaceship(Spaceship):
    def __init__(self, state, *groups):
        Spaceship.__init__(self, state, *groups)

    
class StageText(BasicText):
    def __init__(self, state, font, text, size, color, pos, *groups):
        BasicText.__init__(self, state, font, text, size, color, pos, *groups)
        
    def update(self, now, *args):
        super().update(now, *args)



    
        
        

