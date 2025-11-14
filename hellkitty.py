import background_2stage
from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
import ramona
import resource
import math

SIZE = 1

class IdleState:
    def enter(self, event):
        self.attack_start = True  # Idle이 끝나면 바로 공격 시작
        self.frame = 0

    def exit(self, event):
        self.attack_start = False

    def do(self, frame_time):
        self.move(frame_time)  # Idle 중에도 위아래로 움직임
        if self.attack_start:
            self.change_state(Pattern0_State, None)

    def draw(self):
        bx, by = resource.boss_kitty_idle_coordinate[int(self.idle_frame)][2:4]
        self.image[int(self.idle_frame)].clip_draw(0, 0, bx, by, self.x - canvas_size.shake_x,
                                                   self.y - canvas_size.shake_y, bx * SIZE, by * SIZE)

        if canvas_size.collide_check:
            draw_rectangle(self.x - bx * SIZE,
                           self.y - by * SIZE,
                           self.x + bx * SIZE,
                           self.y + by * SIZE)

class Pattern0_State:
    def enter(self, event):
        self.attack_init = False
        self.attack1 = []
        self.attack1_num = 8
        self.attack1_effect = []

    def exit(self, event):
        self.attack1 = []
        self.attack1_effect = []

    def do(self, frame_time):
        if not self.attack_init:
            self.attack1.append([self.x, self.y, 0, ramona.Ramona_POS_X, ramona.Ramona_POS_Y, 0.0])
            canvas_size.start_shake(0.1, 5)
            self.attack_init = True

        for i in range(len(self.attack1) - 1, -1, -1):
            self.attack1[i][2] = (self.attack1[i][2] + self.attack1_speed * frame_time) % 28
            self.attack1[i][0], self.attack1[i][1], self.attack1[i][3], self.attack1[i][
                4] = canvas_size.distance_funtion2(self.attack1[i][0], self.attack1[i][1], self.attack1[i][3],
                                                   self.attack1[i][4], frame_time, self.attack1_player_speed,
                                                   self.attack1[i][3], self.attack1[i][4])
            self.attack1[i][5] += frame_time

            if self.attack1[i][5] > self.attack1_timer:
                self.attack1_effect.append([self.attack1[i][0], self.attack1[i][1], 20, 20, 0])
                self.attack1[i][5] = 0

            if self.attack1[i][0] < -50 or self.ramonatoattack0(i):
                canvas_size.start_shake(0.1, 5)
                self.attack1_num -= 1
                self.attack1.pop(i)
                if self.attack1_num > 0:
                    self.attack1.append([self.x, self.y, 0, ramona.Ramona_POS_X, ramona.Ramona_POS_Y, 0.0])

    def draw(self):
        pass

class Pattern1_State:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass

class Pattern2_State:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass

class Pattern3_State:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass

class DieState:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass



class Boss_Kitty:
    image = None
    attack1_image = None
    attack2_image = None
    little_image = None
    die_image = None
    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Boss_Kitty.image == None:
            Boss_Kitty.image = [load_image('2stage\\boss1.png'), load_image('2stage\\boss2.png')]
        if Boss_Kitty.die_image == None:
            Boss_Kitty.die_image = resource.boss_kitty_die_image
        if Boss_Kitty.attack1_image == None:
            Boss_Kitty.attack1_image = resource.boss_kitty_attack_image
        if Boss_Kitty.attack2_image == None:
            Boss_Kitty.attack2_image = resource.boss_kitty_uibim_image
        if Boss_Kitty.little_image == None:
            Boss_Kitty.little_image = load_image('2stage\\157.png')

        self.x, self.y = canvas_size.canvaswidth - 300, canvas_size.canvasheight // 2
        self.boss_hp = 240
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
        self.width, self.height = 386 * SIZE, 299 * SIZE
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 300
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.idle_frame = 0
        self.animation_speed = 4.0

        # 상태 전환 관련 변수
        self.attack_start = False
        self.attack_init = False


        self.hit = False
        self.hit_animation = False
        self.hit_time = 0.0
        self.die = False
        self.die_animation = False
        self.die_animation_speed = 2.0
        self.die_frame = 0

        self.attack1_speed = 40.0  # 공통 변수는 유지
        self.attack1_player_speed = 1200.0
        self.attack1_timer = 0.2
        self.attack1_effect_speed = 8.0
        self.attack1_effect = []

    def change_state(self, new_state, event):
        if self.cur_state != new_state:
            self.cur_state.exit(self, event)
            self.cur_state = new_state
            self.cur_state.enter(self, event)

    def update(self, frame_time, events=None):
        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2

        if self.cur_state != DieState:
            self.move(frame_time)

        self.cur_state.do(self, frame_time)

        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2

        if self.hit_animation:
            self.hit_kitty_animation()
        if self.hit:
            self.hit_timer(frame_time)

        if self.hp <= 0 and self.cur_state != DieState:
            self.change_state(DieState, None)

    def draw(self):
        bx, by = resource.boss_kitty_idle_coordinate[int(self.idle_frame)][2:4]

        if background_2stage.start:
            # 현재 상태의 draw() 로직 실행 (각 패턴 그리기)
            self.cur_state.draw(self)

            # 공통 그리기 (이펙트, 보스 본체, HP바)
            if len(self.attack1_effect) > 0 and self.hp > 0 and self.cur_state != DieState:
                for i in self.attack1_effect:
                    ex, ey = resource.boss_kitty_attack_coordinate[int(i[4])][2:4]
                    Boss_Kitty.attack1_image[int(i[2])].clip_draw(0, 0, ex, ey, i[0] - canvas_size.shake_x,
                                                                  i[1] - canvas_size.shake_y, i[2], i[3])

            if self.hit and self.cur_state != DieState:
                if (get_time() % 0.2) > 0.1:
                    self.image[int(self.idle_frame)].clip_draw(0, 0, bx, by, self.x - canvas_size.shake_x,
                                                               self.y - canvas_size.shake_y, bx * SIZE, by * SIZE)

            # DieState가 아닐 때만 보스 본체를 그림 (DieState는 스스로를 그림)
            if self.cur_state != DieState:
                self.image[int(self.idle_frame)].clip_draw(0, 0, bx, by, self.x - canvas_size.shake_x,
                                                           self.y - canvas_size.shake_y, bx * SIZE, by * SIZE)

            if self.hp > 0 and self.cur_state != DieState:
                self.shape.draw(0.6, 0.6)
                self.hp_bar.draw(self.hp, self.boss_hp)

    def move(self, frame_time):
        self.y += self.speed * frame_time * self.dir
        if self.y >= canvas_size.canvasheight - self.height // 2:
            self.dir = -1
        elif self.y <= self.height // 2:
            self.dir = 1

    def hit_kitty_animation(self):
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.hit_animation = False
        self.hit = True

    def hit_timer(self, frame_time):
        self.hit_time += frame_time
        if self.hit_time > 0.5:
            self.hit = False
            self.hit_time = 0.0