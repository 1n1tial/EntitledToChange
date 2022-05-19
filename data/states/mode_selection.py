import pygame
import os, sys

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")

from data.SETTINGS import *
from data.prepare import *
from data.controls import *
from data.state_manager import State, StateManager

from data.components.spaceship import Spaceship


class ModeSelection(State):
    pass
