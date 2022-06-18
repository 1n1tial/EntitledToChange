import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.prestage_text import PreStageText

class FirstStageAfter(PreStageText):
    def __init__(self):
        PreStageText.__init__(self)
        self.text_list = ['.....', '으으으윽....', '여기가 어디지?', '아아... 안타깝게도 저희의 정규 코스에서 한참을 벗어난 것 같아요.', '그리고 우리의 고향 유니버스로 돌아갈 수 있는 방법은 하나뿐이에요.','우리는 각각의 원소들을 장관하는 던전에 들어가,', '전설의 <멀티버스의 가호>를 얻어야 해요.', '그래요, 아직 희망을 버리지 맙시다!']
        self.next = 'stageselection'