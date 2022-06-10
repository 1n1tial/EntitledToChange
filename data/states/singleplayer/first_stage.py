import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.states.singleplayer.prestage_text import PreStageText

class FirstStage(PreStageText):
    def __init__(self):
        PreStageText.__init__(self)
        self.text_list = ['.....', 'Hello?', 'asdf']
        self.next = 'firststagemain'