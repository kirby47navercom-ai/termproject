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

        if Stage3_Terrain.vine_image == None:
            Stage3_Terrain.vine_image = resource.fox_vine_background_image
            Stage3_Terrain.water_image = resource.fox_water_background_image
            Stage3_Terrain.flame_image = resource.fox_flame_background_image
            Stage3_Terrain.vine_needle_appear_image = resource.fox_vine_needle_appear_image
            Stage3_Terrain.vine_needle_disappear_image = resource.fox_vine_needle_disappear_image
            Stage3_Terrain.water_wave_image = resource.fox_water_wave_image
            Stage3_Terrain.flame_ball_image = resource.fox_flame_ball_image
            Stage3_Terrain.white_background_image = resource.white_image[0]

        self.vine_needle_appear_frame = 0
        self.vine_needle_disappear_frame = 0
        self.vine_needle_x = random.randint(558, 1422)
        self.vine_needle_speed = 8
        self.vine_needle_duration_timer = 0.0
        self.vine_needle_duration_time = 4.0
        self.vine_needle_mode = 0  # 0: 등장 1: 지속 2: 사라짐
        self.vine_needle_getbb = [int(self.vine_needle_x) - self.camerax - 88, 140 - self.cameray - 176,
                                  int(self.vine_needle_x) - self.camerax + 88,
                                  140 - self.cameray + 146]

    def update(self, frame_time, events=None):
        pass
    def draw(self):
        pass