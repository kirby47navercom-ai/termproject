from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
import ramona
import resource
import math

SIZE = 1.8


class Boss_Siho:
    def __init__(self):
        self.pattern_set = get_pattern_set()
        self.x, self.y = 1000, 300
        self.boss_hp = 800
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
        self.width, self.height = 386 * SIZE, 299 * SIZE
        self.frame = 0
        self.dir = ''
        self.timer = 0.0
        self.speed = 100
        self.shape = self.pattern_set[randint(0, resource.pattern_number)]
        self.shape.x = self.x - canvas_size.camera_x
        self.shape.y = self.y - canvas_size.camera_y + self.height * 0.2
        self.idle_frame = 0
        self.animation_speed = 8.0

        self.pattern_num = 0
        self.change_graphycs = False

        # 패턴 0
        self.appear_animation = False
        self.appear_frame = 0
        self.appear_timer = 0.0
        self.appear_time = 4.0

        # 패턴 1
        self.idle_frame = 0
        self.idle_timer = 0.0
        self.idle_time = 1.0

        # 패턴 2
        self.y_velocity = 0.0
        self.gravity = 2000.0
        self.jump_power = 200.0
        self.boss_ground_level = 300
        self.jump_duration = 1.2
        self.v_x = 0.0

        self.pattern2_state = 0
        self.pattern2_timer = 0.0
        self.pattern2_target_x = 0  # ★★★ 점프 목표 X좌표
        self.pattern2_landing_x = 0

        self.jump_frame = 0.0

        self.fireballs = []
        self.fireball_speed = 100.0
        self.fireball_jump_power = 1000.0
        self.fireball_gravity = 2500.0

    def update(self, frame_time, events=None):
        if not self.appear_animation:
            self.appear_frame = (self.appear_frame + self.animation_speed * frame_time) % 4
            self.appear_timer += frame_time
            if self.appear_timer >= self.appear_time:
                self.appear_animation = True
        else:
            pattern_method = getattr(self, f'pattern{self.pattern_num}', None)
            if pattern_method:
                pattern_method(frame_time)

        self.shape.x = self.x - canvas_size.camera_x
        self.shape.y = self.y - canvas_size.camera_y + self.height * 0.2

        if self.hit_animation:
            self.hit_shio_animation()
        if self.hit:
            self.hit_timer(frame_time)

    def pattern0(self, frame_time):
        self.appear_frame = (self.appear_frame + self.animation_speed * frame_time) % 8
        if int(self.appear_frame) == 7:
            self.pattern_num = 1

    def pattern1(self, frame_time):
        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2
        self.idle_timer += frame_time
        if self.idle_timer >= self.idle_time:
            self.pattern_num = randint(2, 5)
            self.idle_timer = 0.0
            self.dir = '' if ramona.Ramona_POS_X > self.x else 'h'
            if self.hp <= 550:
                self.pattern_num = 6

    def pattern2(self, frame_time):
        if self.pattern2_state == 0:
            self.jump_frame = (self.jump_frame + self.animation_speed * frame_time) % 3

            if self.jump_frame >= 2.9:

    def launch_fireballs(self):
        pass

    def update_fireballs(self, frame_time):
        pass

    def ramonatofireballs(self, ball):
        pass


    def draw(self):
        if not self.hit or (self.hit and (get_time() % 0.2) > 0.1):
            if not self.appear_animation:
                boss_siho_appear_image[int(self.appear_frame)].clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                                                                   self.x - canvas_size.camera_x,
                                                                                   self.y - canvas_size.camera_y,
                                                                                   64 * SIZE, 64 * SIZE)
        elif self.appear_animation and self.pattern_num == 0:
            boss_siho_appear_image[int(self.appear_frame)].clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                                                               self.x - canvas_size.camera_x,
                                                                               self.y - canvas_size.camera_y,
                                                                               64 * SIZE, 64 * SIZE)

        elif self.appear_animation and self.pattern_num == 1:
            boss_siho_idle_image[int(self.idle_frame)].clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                                                           self.x - canvas_size.camera_x,
                                                                           self.y - canvas_size.camera_y,
                                                                           64 * SIZE, 64 * SIZE)

        if self.hp >= 0 and self.pattern_num != 14:

            self.shape.draw(0.4, 0.4)
            self.hp_bar.draw(self.hp, self.boss_hp)

    def hit_shio_animation(self):
        self.shape = self.pattern_set[randint(0, resource.pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.hit_animation = False
        self.hit = True

    def hit_timer(self, frame_time):
        self.hit_time += frame_time
        if self.hit_time > 0.5:
            self.hit = False
            self.hit_time = 0.0
