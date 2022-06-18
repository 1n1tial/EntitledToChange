import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.prestage_text import PreStageText

class Fire1(PreStageText):
    def __init__(self):
        PreStageText.__init__(self)
        self.text_list = ['이곳은 <불의 던전>입니다.', '이곳의 운석들은 불타고 있어서 아주 위험합니다.', '이곳 어딘가에 <멀티버스의 가호 - 불>이 있을 거에요!']
        self.next = 'fire1main'

