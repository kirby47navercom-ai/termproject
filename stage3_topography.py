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

        self.water_frame = 0
        self.water_wave_frame = 0
        self.water_wave_x = -200
        self.water_wave_speed = 400
        self.water_wave_dir = 1
        self.water_wave_getbb1 = [int(self.water_wave_x) - self.camerax - 20, 260 - self.cameray - 40,
                                  int(self.water_wave_x) - self.camerax + 150, 260 - self.cameray + 20]
        self.water_wave_getbb2 = [int(self.water_wave_x) - self.camerax + 70, 260 - self.cameray - 50,
                                  int(self.water_wave_x) - self.camerax + 170, 260 - self.cameray + 0]
        self.water_wave_getbb3 = [int(self.water_wave_x) - self.camerax + 10, 260 - self.cameray - 40,
                                  int(self.water_wave_x) - self.camerax + 120, 260 - self.cameray + 40]
        self.water_wave_getbb4 = [int(self.water_wave_x) - self.camerax - 40, 260 - self.cameray - 160,
                                  int(self.water_wave_x) - self.camerax + 60, 260 - self.cameray + 0]

        self.flame_frame = 0
        self.flame_ball_frame = 0
        self.flame_ball_x = -100
        self.flame_ball_y = -50
        self.flame_ball_speed = 800
        self.flame_ball_getbb1 = [int(self.flame_ball_x) - self.camerax - 34, int(self.flame_ball_y) - self.cameray + 4,
                                  int(self.flame_ball_x) - self.camerax + 34,
                                  int(self.flame_ball_y) - self.cameray + 64]
        self.flame_ball_getbb2 = [int(self.flame_ball_x) - self.camerax - 19, int(self.flame_ball_y) - self.cameray + 4,
                                  int(self.flame_ball_x) - self.camerax + 19,
                                  int(self.flame_ball_y) - self.cameray + 74]

        self.pattern_transition = False
        self.pattern_start = False
        self.transition_opacity = 0.0
        self.transition_speed = 1.0
        self.transition_phase = 0

    def update(self, frame_time, events=None):
        if self.pattern[self.current_pattern] != self.old_pattern:
            if not self.pattern_transition:
                self.start_transition()

        self.update_transition(frame_time)



    def draw(self):
        pass