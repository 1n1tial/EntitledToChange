import pygame
import random
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.normal_stages import Stage, StageSpaceship, StageText
from data.SETTINGS import *

class Elec1Main(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.lightning = []
        self.lightning_spawn_rate = 1

    def draw(self, surface, interpolate):
        super().draw(surface, interpolate)
        if random.randint(0, 100) <= 1:
            self.draw_lightning(surface, generate_lightning(random.randint(0, SCREENWIDTH), random.randint(-SCREENHEIGHT//10, 0), 0, random.randint(50, 100)))
        for lightning in self.lightning:
            lightning.draw(surface)
        

    def update(self, keys, now):
        self.lightning_spawn_rate += 0.001
        super().update(keys, now)
        # spawn lightning
        if random.randint(1, 100) <= self.lightning_spawn_rate:
            self.lightning.append(Lightning(self))
        for lightning in self.lightning:
            lightning.update()
        self.checkHitByLightning()

    def checkHitByLightning(self):
        for lightning in self.lightning:
            if lightning.x - lightning.width - self.spaceship.rect.width/2 <= self.spaceship.rect.centerx <= lightning.x + lightning.width + self.spaceship.rect.width/2 and lightning.current_state == 'lightning':
                self.spaceship.damage(30)
                self.lightning.remove(lightning)

    def draw_lightning(self, surface, lightning):
        for line in lightning:
            depth = line[0]
            line = line[1:]
            for n, (point1, point2) in enumerate(zip(line, line[1:]), depth):
                c = 200-2*n
                pygame.draw.line(surface, (10,c,150), point1, point2, 12-n//6)

    def spawnAsteroid(self):
        pass

    

def generate_lightning(init_x, init_y, init_depth, length, probability=5):
    result = [[init_depth, (init_x, init_y)]]
    
    for i in range(length):
        new_x = result[0][-1][0] + random.randrange(-10, 10)
        new_y = result[0][-1][1] + random.randrange(4, 17)
        result[0].append((new_x, new_y))

        if random.randint(0, 100) <= probability:
            result.extend(generate_lightning(new_x, new_y, init_depth+i, length=length-i))
    
    return result



class Lightning():
    def __init__(self, state):
        self.state = state
        self.spawn_time = self.state.now
        self.x = random.randint(15, SCREENWIDTH - 15)
        self.y = 0
        self.width = 1
        self.current_state = 'warning' # warning, lightning

    def draw(self, surface):
        pygame.draw.line(surface, (0, 150, 200), (self.x, 0), (self.x, self.y), self.width)

    def update(self):
        if self.current_state == 'warning':
            self.y += 15
            if self.y >= SCREENHEIGHT:
                self.current_state = 'lightning'
        if self.current_state == 'lightning':
            self.width += 4
            if self.width >= 30:
                self.state.lightning.remove(self)


