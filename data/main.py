# import --------------------------------------
import pygame, sys
import os
from data.states.singleplayer.gravity1 import Gravity1Main

from data.states.stage_selection import StageSelection

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.SETTINGS import *
from data import controls, prepare
from data.state_manager import StateManager

from data.states.splash import Splash
from data.states.title_screen import TitleScreen
from data.states.mode_selection import ModeSelection
# from data.states.multiplayer import MultiPlayer
from data.states.singleplayer.gravity1 import Gravity1Main
from data.states.speedrun import Speedrun
from data.states.stage_selection import StageSelection
from data.states.singleplayer.first_stage import FirstStage
from data.states.singleplayer.first_stage_main import FirstStageMain
from data.states.singleplayer.first_stage_after import FirstStageAfter
from data.states.singleplayer.fire1 import Fire1
from data.states.singleplayer.fire1_main import Fire1Main
from data.states.singleplayer.elec1 import Elec1
from data.states.singleplayer.elec1_main import Elec1Main
from data.states.singleplayer.gravity1 import Gravity1Main


def mainLoop():
    game = controls.MainControl(ORIG_CAPTION)
    state_dict = {
            'SPLASH': Splash(),
            'TITLE': TitleScreen(),
            'MODE_SELECTION': ModeSelection(),
            # 'MULTIPLAYER': MultiPlayer(),
            'SPEEDRUN': Speedrun(),
            # 'ENDLESS': Endless(),
            'ENDLESS': Elec1Main(),
            'stageselection': StageSelection(),
            'firststage': FirstStage(),
            'firststagemain': FirstStageMain(),
            'firststageafter': FirstStageAfter(), 
            'fire1': Fire1(),
            'fire1main': Fire1Main(),
            'elec1': Elec1(),
            'elec1main': Elec1Main(),
            'gravity1main': Gravity1Main()
    }
    game.state_manager = StateManager()
    game.state_manager.createStateDict(state_dict, 'SPLASH')
    game.main()
