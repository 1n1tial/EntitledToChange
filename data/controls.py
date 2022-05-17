import pygame, os

from data import state_manager
from data.SETTINGS import *


# class for controlling the main flow of the game ----------
class MainControl():
    def __init__(self, caption):
        self.screen = pygame.display.get_surface()
        self.caption = caption
        self.over = False
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.fps_visible = True
        self.now = 0
        self.keys = pygame.key.get_pressed()
        self.state_manager = state_manager.StateManager

    def update(self):
        self.now = pygame.time.get_ticks()
        self.state_manager.update(self.keys, self.now)
        
    def draw(self, interpolate):
        if not self.state_manager.state.done:
            self.state_manager.draw(self.screen, interpolate)
            pygame.display.update()
            self.show_fps()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.over = True
            elif event.type == pygame.KEYDOWN:
                self.keys = pygame.key.get_pressed()
                self.toggleShowFps(event.key)
            elif event.type == pygame.KEYUP:
                self.keys = pygame.key.get_pressed()
            self.state_manager.getEvent(event)

    def toggleShowFps(self, key):
        if key == pygame.K_F5:
            self.fps_visible = not self.fps_visible
            if not self.fps.visible:
                pygame.display.set_caption(self.caption)
    
    def show_fps(self):
        if self.fps_visible:
            current_fps = self.clock.get_fps()
            pygame.display.set_caption('{} - {:.2f} frames per second'.format(self.caption, current_fps))

    def main(self):
        lag = 0
        while not self.over:
            lag += self.clock.tick(self.fps)
            self.event()
            while lag >= STATE_UPDATE_TIME:
                self.update()
                lag -= STATE_UPDATE_TIME
            self.draw(lag/STATE_UPDATE_TIME)


# basic timer ------------ 
class Timer():
    def __init__(self, unit_ms, ticks=-1):
        self.unit_ms = unit_ms
        self.ticks = ticks
        self.tick_count = 0
        self.time_start = None
        self.time_out = False

    def checkTime(self, now):
        if not self.time_start:
            self.time_start = now
            return True
        elif not self.time_out and now - self.time_start > self.unit_ms:
            self.tick_count += 1
            self.time_start = now
            if self.ticks != -1 and self.tick_count >= self.ticks:
                self.time_out = True
            return True


# loading functions ------------------------------------------------------------
def load_img(directory, set_colorkey=(COLORKEY), accept_ext=('.png', 'jpg')):
    img_dict = {}
    for img in os.listdr(directory):
        name, ext = os.path.splitext(img)
        if ext.lower() in accept_ext:
            loaded_img = pygame.image.load(os.path.join(directory, img))
            if loaded_img.get_alpha():
                loaded_img = loaded_img.convert_alpha()
            else:
                loaded_img = loaded_img.convert()
                loaded_img.set_colorkey(set_colorkey)
            img_dict[name] = loaded_img
        else:
            print(f"{img} is not a .png or .jpg extension")
    return img_dict

def load_music(directory, accept_ext=('.wav', '.ogg', '.mp3')):
    music_dict = {}
    for music in os.listdir(directory):
        name, ext = os.path.splittext(music)
        if ext.lower() in accept_ext:
            music_dict[name] = os.path.join(directory, music)
        else:
            print(f"{music} is not a .wav, .ogg, or .mp3 extension")
    return music_dict

def load_sfx(directory, accept_ext=('.wav', '.ogg')):
    sfx_dict = {}
    for sfx in os.listdir(directory):
        name, ext = os.path.splitext(sfx)
        if ext.lower() in accept_ext:
            sfx_dict[name] = pygame.mixer.Sound(os.path.join(directory, sfx))
        else:
            print(f"{sfx} is not a .wav, .ogg extension")
    return sfx_dict

def load_font(directory, accept_ext=('.ttf')):
    font_dict = {}
    for font in os.listdir(directory):
        name, ext = os.path.splittext(font)
        if ext.lower() in accept_ext:
            font_dict[name] = os.path.join(directory, font)
        else:
            print(f"{font} is not a .wav, .ogg, or .mp3 extension")
    return font_dict




