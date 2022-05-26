import pygame, os, sys, random
from pygame.constants import *

sys.path.append(r"C:\Users\danyu\OneDrive - 서울과학고등학교\문서\서울과학고1학년\컴퓨터과학1\EntitledToChange")
from data import state_manager
from data.SETTINGS import *
from data.components.particles import circle_surf


# class for controlling the main flow of the game ----------
class MainControl(object):
    def __init__(self, caption):
        self.screen = pygame.display.get_surface()
        self.caption = caption
        self.over = False
        self.clock = pygame.time.Clock()
        self.fps = FPS
        self.fps_visible = True
        self.now = 0
        self.keys = pygame.key.get_pressed()
        self.state_manager = state_manager.StateManager()

    def update(self):
        self.now = pygame.time.get_ticks()
        self.state_manager.checkFlip(self.keys, self.now)
        
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
                if event.key == pygame.K_ESCAPE:
                    self.over = True
                self.keys = pygame.key.get_pressed()
                self.toggleShowFps(event.key)
            elif event.type == pygame.KEYUP:
                self.keys = pygame.key.get_pressed()
            self.state_manager.getEvent(event)

    def toggleShowFps(self, key):
        if key == pygame.K_F5:
            self.fps_visible = not self.fps_visible
            if not self.fps_visible:
                pygame.display.set_caption(self.caption)
    
    def show_fps(self):
        if self.fps_visible:
            current_fps = self.clock.get_fps()
            # pygame.display.set_caption('{} - {:.2f} frames per second'.format(self.caption, current_fps))
            pygame.display.set_caption('{} - {}'.format(self.caption, self.state_manager.state_name))
            # try:
            #     pygame.display.set_caption(f'{(self.state_manager.state.now - self.state_manager.state.last_switch)%100}')
            # except:
            #     pass


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
class Timer(object):
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
def load_img(directory, set_colorkey=COLORKEY, accept_ext=('.png', '.jpg')):
    img_dict = {}
    for img in os.listdir(directory):
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
        name, ext = os.path.splitext(music)
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
        name, ext = os.path.splitext(font)
        if ext.lower() in accept_ext:
            font_dict[name] = os.path.join(directory, font)
        else:
            print(f"{font} is not a .wav, .ogg, or .mp3 extension")
    return font_dict


# define controls
CONTROL1 = {
    'UP': pygame.K_UP,
    'DOWN': pygame.K_DOWN,
    'RIGHT': pygame.K_RIGHT,
    'LEFT': pygame.K_LEFT,
    'SHOOT': pygame.K_SPACE
}

CONTROL2 = {
    'UP': pygame.K_w,
    'DOWN': pygame.K_s,
    'RIGHT': pygame.K_d,
    'LEFT': pygame.K_a,
    'SHOOT': pygame.K_SPACE
}


# function for spawning particles
def spawn_particles(obj, number, spread, v_y, surface, color):
    for i in range(number):
        player_particles.append([[obj.rect.centerx, obj.rect.bottom], [random.randint(0, spread*100) / 100 - spread/2, v_y], random.randint(FUEL_SIZE-FUEL_DIFF, FUEL_SIZE+FUEL_DIFF)])

    for particle in player_particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.12
        particle[1][1] -= 0.1
        # pygame.draw.circle(screen, (0, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2] * 2))

        radius = particle[2] * 3
        surface.blit(circle_surf(radius, color), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGBA_ADD)

        if particle[2] <= 0:
            player_particles.remove(particle)





