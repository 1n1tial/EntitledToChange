# import --------------------------------------
from os import stat
import pygame, sys

from data.SETTINGS import *
from . import controls, prepare

from states.splash import Splash


def mainLoop():
    game = controls.MainControl(ORIG_CAPTION)
    state_dict = {
            'SPLASH': Splash()
    }
    game.state_manager.createStateDict(state_dict, 'SPLASH')
    game.main()
