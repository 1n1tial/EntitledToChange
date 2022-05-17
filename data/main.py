# import --------------------------------------
import pygame, sys
import os

from data.SETTINGS import *
from . import controls, prepare
from state_manager import StateManager

from data.states.splash import Splash


def mainLoop():
    game = controls.MainControl(ORIG_CAPTION)
    state_dict = {
            'SPLASH': Splash()
    }
    game.state_manager.createStateDict(state_dict, 'SPLASH')
    game.main()
