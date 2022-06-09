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
        self.elements.draw(surface)
       
    def update(self, keys, now):
        self.now = now
        self.spawnAsteroid()
        self.checkCollision()
        self.elements.update(now)

    def spawnAsteroid(self):
        if self.now - self.last_spawn >= random.randint(1500, 3000):
            Asteroid(self, (self.elements, self.asteroids))
            self.last_spawn = self.now

    def checkCollision(self):
        hits = pygame.sprite.spritecollide(self.spaceship, self.asteroids, True, pygame.sprite.collide_circle)
        for hit in hits:
            if self.spaceship.health > 10:
                self.spaceship.health -= 10
            else:
                self.spaceship.is_alive = False

        hits = pygame.sprite.groupcollide(self.asteroids, self.bullets, True, True)
    
    def getEvent(self, event):
        if not self.spaceship.is_alive:
            self.done = True


class StageSpaceship(Spaceship):
    def __init__(self, state, *groups):
        Spaceship.__init__(self, state, *groups)

    
class StageText(BasicText):
    def __init__(self, state, font, text, size, color, pos, *groups):
        BasicText.__init__(self, state, font, text, size, color, pos, *groups)
        
    def update(self, now, *args):
        super().update(now, *args)

    
        
        

