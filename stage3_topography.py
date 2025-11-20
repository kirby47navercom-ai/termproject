from pico2d import *
import background_3stage
from random import randint
import canvas_size
import ramona
import resource
import random

width = 1980

class Stage3_Terrain:
    vine_image = None
    water_image = None
    flame_image = None
    vine_needle_appear_image = None
    vine_needle_disappear_image = None
    water_wave_image = None
    flame_ball_image = None
    white_background_image = None
    def __init__(self):
        self.terrain_y = [randint(100, 400) for _ in range(5)]
        self.terrain_x = [randint(100, background_3stage.width - 100) for _ in range(5)]
        self.terrain_width = 960
        self.terrain_height = 128
        self.pattern = [1, 2, 3]
        random.shuffle(self.pattern)
        self.current_pattern = 0
        self.old_pattern = 0
        self.speed = 15
        self.camerax = canvas_size.camera_x
        self.cameray = canvas_size.camera_y
    def update(self, frame_time, events=None):
        pass
    def draw(self):
        pass