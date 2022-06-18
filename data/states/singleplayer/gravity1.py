import pygame
import os, sys, random

vec = pygame.math.Vector2


from data.components.asteroid import Asteroid

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.states.singleplayer.normal_stages import Stage, StageSpaceship, StageText
from data.controls import spawn_particles, Timer

class Gravity1Main(Stage):
    def __init__(self):
        Stage.__init__(self)
        self.spaceship.kill()
        self.spaceship = GravitySpaceship(self, (self.elements,))

        
        self.tile_list = []
        self.actual_tile_list = []
        self.stopped_tile_list = []
        self.tile_start_time_list = []
        for _ in range(TILEWIDTH):
            self.tile_list.append(0)
            self.stopped_tile_list.append(0)
            self.actual_tile_list.append([])
            self.tile_start_time_list.append(self.start_time)

        self.scrolling = False
        self.scroll_que = 0
        self.scroll_amount = 0
        self.scroll_spd = 0
        self.scroll_cnt = 0
            
        
    def addTile(self):
        if random.randint(1, 100) <= 5:
            idx = random.randint(0, TILEWIDTH-1)
            
            for i, cnt in enumerate(self.tile_list):
                if cnt == min(self.tile_list):
                    min_idx = i
            if max(self.stopped_tile_list) >= 6:
                while idx != min_idx:
                    idx = random.randint(0, TILEWIDTH-1)
            self.tile_list[idx] += 1
            self.actual_tile_list[idx].append(GravityAsteroid(idx, self, (self.elements, self.asteroids)))
            
            
        
        # if max(self.tile_list) > min(self.tile_list) + 3:
        #     idx = self.tile_list.index(min(self.tile_list))
        #     self.tile_list[idx] += 1
        #     self.actual_tile_list[idx].append(GravityAsteroid(idx, self, (self.elements, self.asteroids)))

        # else:
        #     idx = random.randint(0, TILESIZE-1)
        #     self.tile_list[idx] += 1
        #     self.actual_tile_list[idx].append(GravityAsteroid(idx, self, (self.elements, self.asteroids)))


    def checkFullRow(self):
        if min(self.stopped_tile_list) >= 1:
            for element in self.elements:
                element.new_pos[1] += TILESIZE
            self.stopped_tile_list = list(i-1 for i in self.stopped_tile_list)
            

    def scroll(self):
        if self.scroll_que > 0:    
            self.scroll_amount += 5
            self.scroll_que -= 5
            self.scroll_cnt += 1
        if self.scroll_cnt == 50:
            self.scroll_cnt = 0

            


    def draw(self, surface, interpolate):
        super().draw(surface, interpolate)
        # for asteroid in self.asteroids:
        #     pygame.draw.rect(surface, (200, 200, 200), asteroid.rect)
        # pygame.draw.rect(surface, (200, 200, 200), self.spaceship.rect)
    
    
    def spawnAsteroid(self):
        pass

    def update(self, keys, now):
        if not self.spaceship.is_alive:
            self.done = True
        if self.state == 'running':
            self.now = now
            self.addTile()
            
            
            
            self.checkFullRow()
            self.elements.update(now)
            self.checkCollision()

    def checkCollision(self):
        # hits = pygame.sprite.spritecollide(self.spaceship, self.asteroids, False)
        # for asteroid in hits:
        #     if self.spaceship.vel.x < 0:
        #         self.spaceship.rect.left = asteroid.rect.right
        #     elif self.spaceship.vel.x > 0:
        #         self.spaceship.rect.right = asteroid.rect.left
        #     elif self.spaceship.vel.y > 0:
        #         self.spaceship.rect.bottom = asteroid.rect.top
        #     elif self.spaceship.vel.y <= 0 and asteroid.rect.bottom >= self.spaceship.rect.top:
        #         asteroid.kill()
        #         if self.spaceship.health > 10:
        #             self.spaceship.health -= 10
        #         else:
        #             self.spaceship.is_alive = False

        hits = pygame.sprite.groupcollide(self.asteroids, self.bullets, True, True)
            
        
        # if self.spaceship.vel.y > 0:
        #     hits = pg.sprite.spritecollide(self.spaceship, self.asteroids, False)
        #     if hits:
        #         lowest = hits[0]
        #         for hit in hits:
        #             if hit.rect.bottom > lowest.rect.bottom:
        #                 lowest = hit
        #         if lowest.rect.left - 7 <= self.spaceship.new_pos[0] <= lowest.rect.right + 7:
        #             if self.spaceship.new_pos[1] < lowest.rect.bottom:
        #                 self.spaceship.new_pos[1] = lowest.rect.top - self.spaceship.rect.height
        #                 self.spaceship.vel.y = 0
                        


class GravitySpaceship(StageSpaceship):
    def __init__(self, state, *groups):
        StageSpaceship.__init__(self, state, *groups)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.is_still = False
        self.under_asteroid = []

    def move(self):
        # set gravitational acceleration
        self.acc = vec(0, GRAVITY)
        
        self.vel.x = 0
        keystate = pg.key.get_pressed()
        if keystate[self.controls['LEFT']]:
            self.vel.x -= SPACESHIP_VEL_X
        if keystate[self.controls['RIGHT']]:
            self.vel.x += SPACESHIP_VEL_X
        if keystate[self.controls['UP']]:
            self.acc.y = GRAVITY - SPACESHIP_ACC_Y
        if keystate[self.controls['SHOOT']]:
            self.prepare_liftoff = True

        self.checkCollision()
        self.acc.y += self.vel.y * RESISTANCE
        if keystate[self.controls['UP']]:
            self.is_still = False
            self.under_asteroid.clear()
        if not self.under_asteroid:
            self.is_still = False
        if not self.is_still:
            self.vel += self.acc


        self.new_pos[0] += self.vel.x
        self.new_pos[1] += self.vel.y

        
        

    def checkCollision(self):
        if self.rect.right > SCREENWIDTH:
            self.rect.right = SCREENWIDTH
            self.new_pos[0] = SCREENWIDTH - self.rect.width
        if self.rect.left < 0:
            self.rect.left = 0
            self.new_pos[0] = 0
        if self.rect.bottom >= SCREENHEIGHT:
            self.rect.bottom = SCREENHEIGHT
            self.new_pos[1] = SCREENHEIGHT - self.rect.height
            self.vel.y = 0
            self.is_still = True

        hits = pygame.sprite.spritecollide(self, self.state.asteroids, False)
        
        for asteroid in hits:
            if self.vel.x < 0:
                if not self.is_still:
                    self.new_pos[0] = asteroid.rect.right
                    self.rect.left = asteroid.rect.right
                    self.vel.x = 0
                else:
                    if asteroid not in self.under_asteroid:
                        self.new_pos[0] = asteroid.rect.right
                        self.rect.left = asteroid.rect.right
                        self.vel.x = 0
            elif self.vel.x > 0:
                if not self.is_still:
                    self.new_pos[0] = asteroid.rect.left - self.rect.width
                    self.rect.right = asteroid.rect.left
                    self.vel.x = 0
                else:
                    if asteroid not in self.under_asteroid:
                        self.new_pos[0] = asteroid.rect.left - self.rect.width
                        self.rect.right = asteroid.rect.left
                        self.vel.x = 0
            elif self.vel.y > 0 and not self.is_still:
                if asteroid not in self.right_asteroid and asteroid not in self.left_asteroid:
                    self.new_pos[1] = asteroid.rect.top - self.rect.height
                    self.rect.bottom = asteroid.rect.top
                    self.is_still = True
                    self.vel.y = 0
            elif self.vel.y >= 0 and self.is_still:
                if asteroid not in self.right_asteroid and asteroid not in self.left_asteroid:
                    self.new_pos[1] = asteroid.rect.top - self.rect.height
                    self.rect.bottom = asteroid.rect.top
                    self.vel.y = 0
            if asteroid.rect.bottom >= self.rect.top:
                if asteroid not in self.under_asteroid + self.right_asteroid + self.left_asteroid:
                    asteroid.kill()
                    if self.health > 10:
                        self.health -= 10
                    else:
                        self.is_alive = False

        # check asteroids under spaceship
        self.rect.bottom += TILESIZE
        self.under_asteroid = pygame.sprite.spritecollide(self, self.state.asteroids, False)
        self.rect.bottom -= TILESIZE
        self.rect.right += 1
        self.right_asteroid = list(set(pygame.sprite.spritecollide(self, self.state.asteroids, False)) - set(hits))
        self.rect.right -= 1
        self.rect.left -= 1
        self.left_asteroid = list(set(pygame.sprite.spritecollide(self, self.state.asteroids, False)) - set(hits))
        self.rect.left += 1
        

class GravityAsteroid(BasicSprite):
    def __init__(self, idx, state, *groups):
        self._layer = Layer_dict['Asteroid']
        self.groups = (state.elements, state.asteroids)
        BasicSprite.__init__(self, (idx*TILESIZE, -TILESIZE), (ASTEROID_WIDTH, ASTEROID_HEIGHT), *groups)
        self.state = state
        self.image = pygame.transform.scale(IMG_DICT['sprite']['asteroid'], (ASTEROID_WIDTH, ASTEROID_HEIGHT))
        self.idx = idx
        self.is_moving = True
        
        self.particles = []

    def move(self):
        if self.is_moving:
            self.new_pos[1] += 3 + self.state.scroll_cnt
            if self.new_pos[1] >= SCREENHEIGHT - (self.state.stopped_tile_list[self.idx] * TILESIZE + TILESIZE):
                self.new_pos[1] = SCREENHEIGHT - (self.state.stopped_tile_list[self.idx] * TILESIZE + TILESIZE)
                self.is_moving = False
                self.state.stopped_tile_list[self.idx] += 1
        if self.new_pos[1] < SCREENHEIGHT - (self.state.stopped_tile_list[self.idx] * TILESIZE + TILESIZE):
            self.is_moving = True
        # if self.is_moving and SCREENHEIGHT - (self.state.stopped_tile_list[self.idx] * TILESIZE + TILESIZE) + self.state.scroll_amount <= self.new_pos[1]:
        #     self.new_pos[1] = SCREENHEIGHT - (self.state.stopped_tile_list[self.idx] * TILESIZE + TILESIZE) + self.state.scroll_amount
        #     self.state.stopped_tile_list[self.idx] += 1
        #     self.is_moving = False
        # if self.is_moving:
        #     self.new_pos[1] += 15
        # elif not self.is_moving:
        #     try:
        #         self.new_pos[1] = SCREENHEIGHT - (self.state.actual_tile_list.index(self) * TILESIZE) + self.state.scroll_amount
        #     except:
        #         pass

    def checkOutOfScreen(self):
        if self.rect.top > SCREENHEIGHT:
            self.kill()



    def update(self, now, *args):
        self.old_pos = self.new_pos[:]
        self.move()
        self.rect.topleft = self.new_pos
        self.checkOutOfScreen()
        self.now = now
        

   
