# import -------------------------------------------------------
import pygame
import os

# initialize ----------------------------------------------------------
pygame.init()

# main game window settings -----------------------------------------------
SCREENWIDTH = 800
SCREENHEIGHT = 600
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
SCREENRECT = pygame.Rect(0, 0, SCREENWIDTH, SCREENHEIGHT)
ORIG_CAPTION = "asteroids"

# state settings ------------------------------------------------------

# splash settings
ALPHA_GRADIENT = 1

# color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# font settings
FONT_PATH = os.path.join('resources', 'font')
LOADING_FONT_PATH = os.path.join("resources", "font", 'ARCADECLASSIC.ttf')
RENDER_FONT = pygame.font.Font(LOADING_FONT_PATH, 50)

# music settings
MUSIC_PATH = os.path.join('resources', 'snd')

# sfx settings
SFX_PATH = os.path.join('resources', 'sfx')

# icon settings
ICON_PATH = os.path.join("resources", "img", "icon.png")

# image settins
IMG_PATH = os.path.join('resources', 'img')
COLORKEY = (0, 0, 0)

# timer settings
FPS = 60
STATE_UPDATE_TIME = 16

# layer settings
Layer_dict = {}
