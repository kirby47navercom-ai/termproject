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

        if not self.pattern_transition:
            if self.pattern[self.current_pattern] == 1:
                self.needle_move(frame_time)
            elif self.pattern[self.current_pattern] == 2:
                self.water_frame = (self.water_frame + frame_time * self.speed) % 8
                self.water_wave_frame = (self.water_wave_frame + frame_time * self.speed) % 8
                self.wave_move(frame_time)
                self.ramonatowave()
            elif self.pattern[self.current_pattern] == 3:
                self.flame_frame = (self.flame_frame + frame_time * self.speed) % 5
                self.flame_ball_frame = (self.flame_ball_frame + frame_time * self.speed) % 5
                self.ball_move(frame_time)
                self.ramonatoball()

        self.falldown()

    def falldown(self):
        if ramona.Ramona_POS_Y < self.terrain_height - 10:
            if not ramona.Ramona_invincible:  # 무적 상태가 아닐 때만 피해
                ramona.CURRENT_HP -= 3
                ramona.Ramona_invincible = True
                ramona.Ramona_invincible_timer = 0.0  # 변수명 수정
                canvas_size.start_shake(0.5, 5.0)

    def needle_move(self, frame_time):
        if self.vine_needle_mode == 0:
            self.vine_needle_appear_frame = (self.vine_needle_appear_frame + frame_time * self.vine_needle_speed) % 12
            if int(self.vine_needle_appear_frame) == 11:
                self.vine_needle_mode = 1  # 지속 모드로 전환
                self.vine_needle_appear_frame = 0  # 프레임 초기화
        elif self.vine_needle_mode == 1:
            self.vine_needle_duration_timer += frame_time
            self.ramonatoneedle()
            if self.vine_needle_duration_timer >= self.vine_needle_duration_time:
                self.vine_needle_mode = 2  # 사라짐 모드로 전환
                self.vine_needle_duration_timer = 0.0  # 타이머 초기화
        elif self.vine_needle_mode == 2:
            self.vine_needle_disappear_frame = (self.vine_needle_disappear_frame + frame_time * self.vine_needle_speed) % 12
            if int(self.vine_needle_disappear_frame) == 11:
                self.vine_needle_mode = 0  # 다시 등장 모드로 전환
                self.vine_needle_disappear_frame = 0  # 프레임 초기화
                self.vine_needle_x = random.randint(558, 1422)  # 새로운 위치 설정
        self.vine_needle_getbb = [int(self.vine_needle_x) - self.camerax - 88, 140 - self.cameray - 176,
                                  int(self.vine_needle_x) - self.camerax + 88,
                                  140 - self.cameray + 146]

    def ramonatoneedle(self):
        if resource.collide2(
                [ramona.Ramona_POS_X - self.camerax, ramona.Ramona_POS_Y - self.cameray, ramona.Ramona_SIZE_X,
                 ramona.Ramona_SIZE_Y],
                self.vine_needle_getbb) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def wave_move(self, frame_time):
        self.water_wave_x += self.water_wave_speed * frame_time * self.water_wave_dir
        if self.water_wave_x > 2780:
            self.water_wave_dir = -1
        elif self.water_wave_x < -800:
            self.water_wave_dir = 1

        self.water_wave_getbb1 = [
            int(self.water_wave_x) - (130 if self.water_wave_dir == -1 else 0) - self.camerax - 20,
            260 - self.cameray - 40,
            int(self.water_wave_x) - (130 if self.water_wave_dir == -1 else 0) - self.camerax + 150,
            260 - self.cameray + 20]
        self.water_wave_getbb2 = [
            int(self.water_wave_x) - (130 if self.water_wave_dir == -1 else 0) - self.camerax + 70,
            260 - self.cameray - 50,
            int(self.water_wave_x) - (130 if self.water_wave_dir == -1 else 0) - self.camerax + 170,
            260 - self.cameray + 0]
        self.water_wave_getbb3 = [
            int(self.water_wave_x) - (130 if self.water_wave_dir == -1 else 0) - self.camerax + 10,
            260 - self.cameray - 40,
            int(self.water_wave_x) - (130 if self.water_wave_dir == -1 else 0) - self.camerax + 120,
            260 - self.cameray + 40]
        self.water_wave_getbb4 = [int(self.water_wave_x) - self.camerax - 40, 260 - self.cameray - 160,
                                  int(self.water_wave_x) - self.camerax + 60, 260 - self.cameray + 0]

    def ramonatowave(self):
        if ((resource.collide2(
                [ramona.Ramona_POS_X - self.camerax, ramona.Ramona_POS_Y - self.cameray, ramona.Ramona_SIZE_X,
                 ramona.Ramona_SIZE_Y],
                self.water_wave_getbb1) or
             resource.collide2([ramona.Ramona_POS_X - self.camerax, ramona.Ramona_POS_Y - self.cameray,
                                ramona.Ramona_SIZE_X - self.camerax, ramona.Ramona_SIZE_Y - self.cameray],
                               self.water_wave_getbb2) or
             resource.collide2([ramona.Ramona_POS_X - self.camerax, ramona.Ramona_POS_Y - self.cameray,
                                ramona.Ramona_SIZE_X - self.camerax, ramona.Ramona_SIZE_Y - self.cameray],
                               self.water_wave_getbb3) or
             resource.collide2([ramona.Ramona_POS_X - self.camerax, ramona.Ramona_POS_Y - self.cameray,
                                ramona.Ramona_SIZE_X - self.camerax, ramona.Ramona_SIZE_Y - self.cameray],
                               self.water_wave_getbb4)) and
                not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible):
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def ball_move(self, frame_time):
        self.flame_ball_y += self.flame_ball_speed * frame_time
        if self.flame_ball_y > 900:
            self.flame_ball_x = ramona.Ramona_POS_X
            self.flame_ball_y = -50
            self.flame_ball_speed = 200

        self.flame_ball_getbb1 = [int(self.flame_ball_x) - self.camerax - 34, int(self.flame_ball_y) - self.cameray + 4,
                                  int(self.flame_ball_x) - self.camerax + 34,
                                  int(self.flame_ball_y) - self.cameray + 64]
        self.flame_ball_getbb2 = [int(self.flame_ball_x) - self.camerax - 19, int(self.flame_ball_y) - self.cameray + 4,
                                  int(self.flame_ball_x) - self.camerax + 19,
                                  int(self.flame_ball_y) - self.cameray + 74]

    def draw(self):
        pass