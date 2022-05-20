# import -------------------------------------------------------
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

# color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
Layer_dict = {}

# sprite settings ----------------------------
# player settings ------------------------------
FUEL_SIZE = 12
FUEL_DIFF = 4
FUEL_SIZE_DECREASE = 0.1
PLAYER_WIDTH = 50