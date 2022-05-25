# import -------------------------------------------------------
from tkinter import ON
import pygame
import os, sys
sys.path.append('../data')

# initialize ----------------------------------------------------------
pygame.init()

# main game window settings -----------------------------------------------
SCREENWIDTH = 700
SCREENHEIGHT = 700
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
SCREENRECT = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
ORIG_CAPTION = "asteroids"

COLOR_DICT = {}

# main game settings ----------------------------------------------------
GAME_TITLE = 'Asteroids'

# state settings ------------------------------------------------------

# splash settings
ALPHA_GRADIENT = 2

# start settings
SPACESHIP_VEL_X = 5
SPACESHIP_VEL_Y = 4

# mode selection settings
ONE_COLOR_TIME = 2000
CHANGE_TIME = 500
LOOP_TIME = 2*(ONE_COLOR_TIME + CHANGE_TIME)
MAX_COLOR = 100
SWITCH_COOLTIME = 200
SHOOT_COOLDOWN = 200

# color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# font settings
FONT_PATH = os.path.join('resources', 'font')
LOADING_FONT_PATH = os.path.join("resources", "font", 'ARCADECLASSIC.ttf')
RENDER_TITLE_FONT = pygame.font.Font(LOADING_FONT_PATH, 100)

# music settings
MUSIC_PATH = os.path.join('resources', 'snd')

# sfx settings
SFX_PATH = os.path.join('resources', 'sfx')

# icon settings
ICON_PATH = os.path.join("resources", "img", "icon", "icon.png")

# image settings
IMG_PATH = os.path.join('resources', 'img')
COLORKEY = (0, 0, 0)

# timer settings
FPS = 60
STATE_UPDATE_TIME = 16

# layer settings
Layer_dict = {
    'Spaceship': 1,
    'Text': 2}

# sprite settings ----------------------------
# player settings ------------------------------
FUEL_SIZE = 4
FUEL_DIFF = 1
FUEL_SIZE_DECREASE = 0.12
PLAYER_WIDTH = 50
FUEL_ACCELERATION = 0.1
player_particles = []