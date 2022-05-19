import os, sys
import pygame as pg

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data.SETTINGS import *
from data import controls

pg.init()

# initialization
y_offset = (pg.display.Info().current_w - SCREENWIDTH)//2
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{y_offset}, {50}'
pg.display.set_caption(ORIG_CAPTION)
pg.display.set_icon(pg.image.load(ICON_PATH))
screen = pg.display.set_mode(SCREENSIZE)

# loading screen while blank rendering
screen.fill(BLACK)
render_title_text = RENDER_TITLE_FONT.render('Loading', 0, WHITE)
screen.blit(render_title_text, render_title_text.get_rect(center=SCREENRECT.center))
pg.display.update()

# load fonts, music, sfx, img
FONT_DICT = controls.load_font(FONT_PATH)
MUSIC_DICT = controls.load_music(MUSIC_PATH)
SFX_DICT = controls.load_sfx(SFX_PATH)
IMG_DICT = {}
SUB_DIRECTORIES = ['icon', 'splash', 'sprite']
for dir in SUB_DIRECTORIES:
    sub_dict = controls.load_img(os.path.join(IMG_PATH, dir))
    IMG_DICT[dir] = sub_dict

def render_font(font, text, size, color, center_pos, antialias=0):
    font_to_render = pygame.font.Font(FONT_DICT[font], int(size))
    rendered_font = font_to_render.render(text, antialias, color)
    rendered_font_rect = rendered_font.get_rect(center=center_pos)
    return rendered_font, rendered_font_rect
    
