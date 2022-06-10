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
    


# template class for all sprites -------------------------------------
class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.rect = pygame.Rect(pos, size)
        self.pos_basis = 'topleft'
        self.new_pos = list(self.rect.topleft)
        self.old_pos = self.new_pos[:]

    def update_pos(self, value, basis='topleft'):
        setattr(self.rect, basis, value)
        self.new_pos = list(self.rect.topleft)
        self.old_pos = self.new_pos[:]

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class BasicText(pygame.sprite.Sprite):
    def __init__(self, state, font, text, size, color, pos, *groups):
        self._layer = Layer_dict['Text']
        self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.state = state
        self.image, self.rect = render_font(font, text, size, color, pos)
        self.font = font
        self.size = size
        self.text = text
        self.color = color
        self.pos = pos
        
    def update(self, now, *args):
        self.image, self.rect = render_font(self.font, self.text, self.size, self.color, self.pos)
    
        