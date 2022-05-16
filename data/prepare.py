from os import path
import pygame as pg

from .SETTINGS import *

pg.init()

# initialization
y_offset = (pg.display.Info().current_w - SCREENWIDTH)//2
os.environ['SDL_WINDOW_DIV_POS']
pg.display.set_caption(ORIG_CAPTION)
pg.display.set_icon(pg.image.load(ICON_PATH))
screen = pg.display.set_mode(SCREENSIZE)

# loading screen while blank rendering
screen.fill(BLACK)
render_text = RENDER_FONT.render('Loading... please wait', 0, WHITE)
screen.blit(render_text, render_text.get_rect(center=))
pg.display.update()