import pygame, sys
import os

pygame.init()

# main game window settings
SCREENWIDTH = 800
SCREENHEIGHT = 600
ORIG_CAPTION = "asteroids"

# color settings
COLORKEY = (255, 0, 255)

# font settings
FONT_PATH = os.path.join("data", "font")
FONT = pygame.font.Font(FONT_PATH, 50)

# icon settings


#FPS
FPS = 60
