import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.prestage_text import PreStageText

class Elec1(PreStageText):
    def __init__(self):
        PreStageText.__init__(self)
        self.text_list = ['이곳은 <전기의 던전>입니다.', '이곳에서는 운석이 아니라 강력한 낙뢰가 떨어집니다.', '다행히도, 작은 낙뢰는 우리의 우주선을 위협하기에는 역부족이지만,', '굵은 번개는 반드시 피하여야 됩니다.', '이곳 어딘가에 <멀티버스의 가호 - 번개>이 있을 거에요!']
        self.next = 'elec1main'

