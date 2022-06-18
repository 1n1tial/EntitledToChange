import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.prestage_text import PreStageText

class FirstStage(PreStageText):
    def __init__(self):
        PreStageText.__init__(self)
        self.text_list = ['.....', '안녕하세요?', '만나서 반갑습니다!', '저는 여러분의 안전한 우주여행을 위한 가이드입니다.', '즐거운 시간 되십시오!']
        self.next = 'firststagemain'