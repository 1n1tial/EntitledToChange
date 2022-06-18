import pygame, random
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.states.singleplayer.normal_stages import Stage, StageSpaceship, StageText
from data.components.asteroid import Asteroid

class FirstStageMain(Stage):
    def __init__(self):
        
        Stage.__init__(self)
        # text printing related-------------
        self.text_list_array = [['좋아요, 그럼 시작해봅시다!'], ['컨트롤부터 익혀보자구요.', '방향키로 좌우로 움직이고, ', '<SPACE>로 총을 쏠 수 있습니다.'], ['참 쉽죠?'], ['앗, 저기에 운석들이 날라옵니다.', '피하세요!'], ['어라, 운석이 비정상적으로 많이 포착되고 있습니다!', '비상!!', '비상!!!', '비상!!!!!!']]
        self.text_list = self.text_list_array[self.current_text_list_idx]
        self.text_interval = 50
        self.box_reveal_time = 500
        self.text_state = 'printing'
        self.text_num = 0
        self.text_counter = 0
        self.text_ch_num = 0
        
        self.next = 'firststageafter'
        self.asteroid_spawn_rate = 0

    
    def spawnAsteroid(self):
        self.asteroid_spawn_rate += 0.005
        if random.randrange(1, 100) <= self.asteroid_spawn_rate:
            Asteroid(self, (self.elements, self.asteroids))
            self.last_spawn = self.now

    def print_text(self, now):
        if now - self.start_time == 0 or 3000 <= now - self.start_time <= 3100 or 10000 <= now - self.start_time <= 10100 or 18000 <= now - self.start_time <= 18100 or 35000 <= now - self.start_time <= 35100:
            self.state = 'texting'
            self.text_start_time = now


