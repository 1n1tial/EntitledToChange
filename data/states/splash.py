import pygame as pg
import os, sys

from data.SETTINGS import *
from data.state_manager import StateManager, State


class Splash(State):
    def __init__(self):
        State.__init__(self)
        self.next = 'TITLE'
        
        self.alpha_gradient = ALPHA_GRADIENT
