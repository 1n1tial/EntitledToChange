# import --------------------------------------
import pygame, sys
import os

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.SETTINGS import *
from data import controls, prepare
from data.state_manager import StateManager

from data.states.splash import Splash
from data.states.title_screen import TitleScreen
from data.states.mode_selection import ModeSelection


def mainLoop():
    game = controls.MainControl(ORIG_CAPTION)
    state_dict = {
            'SPLASH': Splash(),
            'TITLE': TitleScreen(),
            'MODE_SELECTION': ModeSelection()
    }
    game.state_manager = StateManager()
    game.state_manager.createStateDict(state_dict, 'SPLASH')
    game.main()
