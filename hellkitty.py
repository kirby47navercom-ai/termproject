from pico2d import *

import background_2stage
from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
import random
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
        pass

    def do(self, frame_time):
        self.move(frame_time)  # Idle 중에도 위아래로 움직임
        # (필요하다면 Idle 상태에서 다음 패턴으로 넘어가는 타이머 추가)
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


class Pattern0_State:  # 하트 유도탄
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

        if self.attack1_num == 0:
            self.change_state(Pattern1_State, None)

    def draw(self):
        if len(self.attack1) > 0:
            for i in self.attack1:
                ax, ay = resource.boss_kitty_attack_coordinate[int(i[2])][2:4]
                Boss_Kitty.attack1_image[int(i[2])].clip_draw(0, 0, ax, ay, i[0] - canvas_size.shake_x,
                                                              i[1] - canvas_size.shake_y, ax * 1.5, ay * 1.5)
                if canvas_size.collide_check:
                    draw_rectangle(i[0] - ax * 1.5 / 2,
                                   i[1] - ay * 1.5 / 2,
                                   i[0] + ax * 1.5 / 2,
                                   i[1] + ay * 1.5 / 2)
        # (이펙트 그리기 로직은 Boss_Kitty.draw()로 이동)


class Pattern1_State:  # 레이저
    def enter(self, event):
        self.attack_init = True
        self.attack2_init = True
        self.attack2_init_time = 0.0
        self.attack2_num = 3
        self.attack2 = []

    def exit(self, event):
        self.attack2_init = False
        self.attack2 = []

    def do(self, frame_time):
        if self.attack_init:
            x, self.y = canvas_size.distance_funtion(0, self.y, 0, ramona.Ramona_POS_Y, frame_time,
                                                     self.attack2_init_speed)
            self.attack2_init_time += frame_time
            if self.attack2_init_time > self.attack2_init_timer:
                self.attack_init = False
                self.attack2_init_time = 0.0
                self.attack2.append([ramona.Ramona_POS_Y, 0, 0.0, 0])
        else:
            for i in range(len(self.attack2) - 1, -1, -1):
                if self.attack2[i][3] == 0:
                    self.attack2[i][2] += frame_time
                    if self.attack2[i][2] > self.attack2_timer:
                        self.attack2_init = False
                        self.attack2[i][3] = 1
                        self.attack2[i][2] = 0.0
                        self.attack2[i][1] = 0
                        canvas_size.start_shake(1, 10)
                        if self.attack2_num > 0:
                            self.attack2_num -= 1
                            self.attack2.append([ramona.Ramona_POS_Y, 0, 0.0, 0])
                elif self.attack2[i][3] == 1:
                    if self.attack2[i][2] < self.attack2_timer - 1.0:
                        if self.attack2[i][1] < 3:
                            self.attack2[i][1] = (self.attack2[i][1] + self.attack2_speed * frame_time)
                        self.ramonatoattack1(self.attack2[i])
                        self.attack2[i][2] += frame_time
                    else:
                        self.attack2[i][1] = (self.attack2[i][1] + self.attack2_speed * frame_time * 0.7)
                        if int(self.attack2[i][1]) > 6:
                            self.attack2.pop(i)

            if self.attack2_num == 0 and len(self.attack2) == 0:
                self.change_state(Pattern2_State, None)

    def draw(self):
        if len(self.attack2) > 0:
            for i in self.attack2:
                ax, ay = resource.boss_kitty_uibim_coordinate[int(i[1])][2:4]
                Boss_Kitty.attack2_image[int(i[1])].clip_draw(0, 0, ax, ay, self.x - 100 - canvas_size.shake_x,
                                                              i[0] - canvas_size.shake_y, ax * 1.5, ay * 0.7)

                if canvas_size.collide_check:
                    draw_rectangle(self.x - 100 - ax * 1.5 / 2,
                                   i[0] - ay * 1.5 / 2,
                                   self.x - 100 + ax * 1.5 / 2,
                                   i[0] + ay * 1.5 / 2)


class Pattern2_State:  # 꼬마 키티
    def enter(self, event):
        self.attack_init = False
        self.attack3_time = 0.0
        self.attack3_spawned_count = 0
        self.attack3 = []

    def exit(self, event):
        self.attack3 = []

    def do(self, frame_time):

        self.attack3_time += frame_time
        if self.attack3_spawned_count < self.attack3_num and self.attack3_time >= self.attack3_spawn_interval:
            origin_x = randint(5, canvas_size.canvaswidth // 2 - 20)
            self.attack3.append([origin_x, canvas_size.canvasheight + 50, 0.0])
            self.attack3_time = 0.0
            self.attack3_spawned_count += 1

        for i in range(len(self.attack3) - 1, -1, -1):
            kitty = self.attack3[i]
            kitty[2] += frame_time
            kitty[1] -= self.attack3_vertical_speed * frame_time
            current_x = kitty[0] + self.attack3_dance_amplitude * math.sin(kitty[2] * self.attack3_dance_frequency)

            kitty_w, kitty_h = self.attack3_kitty_size
            kitty_box = (current_x, kitty[1], kitty_w, kitty_h)
            player_box = (ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y)

            if resource.collide(player_box,
                                kitty_box) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                canvas_size.start_shake(0.5, 5.0)

            elif kitty[1] < -50:
                self.attack3.pop(i)

        if self.attack3_spawned_count == self.attack3_num and len(self.attack3) == 0:
            self.change_state(Pattern3_State, None)

    def draw(self):
        if len(self.attack3) > 0:
            w, h = self.attack3_kitty_size
            left, bottom, width, height, jx, jy = resource.little_kitty_idle_coordinate
            for kitty in self.attack3:
                origin_x, current_y, internal_time = kitty
                current_x = origin_x + self.attack3_dance_amplitude * math.sin(
                    internal_time * self.attack3_dance_frequency)
                self.little_image.clip_draw(left, bottom, width, height, current_x - canvas_size.shake_x,
                                            current_y - canvas_size.shake_y, w * 1.5, h * 1.5)
                if canvas_size.collide_check:
                    draw_rectangle(current_x - w * 1.5 / 2,
                                   current_y - h * 1.5 / 2,
                                   current_x + w * 1.5 / 2,
                                   current_y + h * 1.5 / 2)


class Pattern3_State:  # 부채꼴 탄막
    def enter(self, event):
        self.attack_init = False
        self.attack4_spawn_time = 0.0
        self.attack4_duration_timer = 0.0
        self.attack4 = []

    def exit(self, event):
        self.attack4 = []

    def do(self, frame_time):
        is_spawning = self.attack4_duration_timer < self.attack4_duration
        if is_spawning:
            self.attack4_spawn_time += frame_time
            self.attack4_duration_timer += frame_time
            if self.attack4_spawn_time >= self.attack4_spawn_interval:
                self.attack4_spawn_time = 0.0
                spawn_x = self.x
                spawn_y = canvas_size.canvasheight // 2
                angle_deg = random.uniform(135, 225)
                angle_rad = math.radians(angle_deg)
                dir_x = math.cos(angle_rad)
                dir_y = math.sin(angle_rad)
                self.attack4.append([spawn_x, spawn_y, dir_x, dir_y, 0.0])

        for i in range(len(self.attack4) - 1, -1, -1):
            bullet = self.attack4[i]
            bullet[0] += bullet[2] * self.attack4_bullet_speed * frame_time
            bullet[1] += bullet[3] * self.attack4_bullet_speed * frame_time
            bullet[4] = (bullet[4] + self.attack1_speed * frame_time) % 28

            ax, ay = bullet[0], bullet[1]
            rx, ry = ramona.Ramona_POS_X, ramona.Ramona_POS_Y
            threshold = 40
            dx, dy = ax - rx, ay - ry
            is_collided = (
                                      dx * dx + dy * dy <= threshold * threshold) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible
            if is_collided:
                if ramona.CURRENT_HP > 0:
                    ramona.CURRENT_HP -= 1
                    ramona.Ramona_invincible = True
                    canvas_size.start_shake(0.5, 5.0)
                self.attack4.pop(i)
            elif bullet[0] < -50 or bullet[1] < -50 or bullet[1] > canvas_size.canvasheight + 50:
                self.attack4.pop(i)

        if not is_spawning and len(self.attack4) == 0:
            self.change_state(IdleState, None)  # (임시로 Idle로, 원하면 Pattern0_State로)

    def draw(self):
        if len(self.attack4) > 0:
            for bullet in self.attack4:
                frame_idx = int(bullet[4])
                ax, ay = resource.boss_kitty_attack_coordinate[frame_idx][2:4]
                Boss_Kitty.attack1_image[frame_idx].clip_draw(0, 0, ax, ay, bullet[0] - canvas_size.shake_x,
                                                              bullet[1] - canvas_size.shake_y, ax * 1.5, ay * 1.5)

                if canvas_size.collide_check:
                    draw_rectangle(bullet[0] - ax * 1.5 / 2,
                                   bullet[1] - ay * 1.5 / 2,
                                   bullet[0] + ax * 1.5 / 2,
                                   bullet[1] + ay * 1.5 / 2)


class DieState:
    def enter(self, event):
        self.die_animation = True
        self.die_frame = 0

    def exit(self, event):
        pass

    def do(self, frame_time):
        if self.y < -200:
            self.die = True
        else:
            self.y += self.speed * frame_time * -1 / 2
            self.die_frame = (self.die_frame + self.die_animation_speed * frame_time * 2) % 4
            canvas_size.start_shake(0.5, 5)

    def draw(self):
        left, bottom, width, height = boss_kitty_die_coordinate[0:4]
        self.die_image[int(self.die_frame)].draw(self.x - canvas_size.shake_x, self.y - canvas_size.shake_y,
                                                 width * SIZE * 1.5, height * SIZE * 1.5)
        if canvas_size.collide_check:
            draw_rectangle(self.x - width * SIZE * 1.5 / 2,
                           self.y - height * SIZE * 1.5 / 2,
                           self.x + width * SIZE * 1.5 / 2,
                           self.y + height * SIZE * 1.5 / 2)


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
        self.shape = self.pattern_set[randint(0, resource.pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.idle_frame = 0
        self.animation_speed = 4.0

        # 상태 전환 관련 변수
        self.attack_start = False  # (IdleState에서 True로 바뀜)
        self.attack_init = False  # (각 패턴 상태가 관리함)

        # 피격/죽음 관련
        self.hit = False
        self.hit_animation = False
        self.hit_time = 0.0
        self.die = False
        self.die_animation = False
        self.die_animation_speed = 2.0
        self.die_frame = 0

        # 각 패턴의 상태 변수들은 __init__에서 제거
        # (각 상태 클래스의 enter 함수에서 초기화됨)
        self.attack1_speed = 40.0  # 공통 변수는 유지
        self.attack1_player_speed = 1200.0
        self.attack1_timer = 0.2
        self.attack1_effect_speed = 8.0
        self.attack1_effect = []



        self.attack2_init_speed = 300
        self.attack2_init_timer = 2.0
        self.attack2_timer = 2.0
        self.attack2_speed = 40.0

        self.attack3_spawn_interval = 0.5
        self.attack3_vertical_speed = 150.0
        self.attack3_dance_amplitude = 50.0
        self.attack3_dance_frequency = 3.0
        w, h = resource.little_kitty_idle_coordinate[2:4]
        self.attack3_kitty_size = (w, h)
        self.attack3_num = 8
        self.attack3_init_timer = 2.0

        self.attack4_init_timer = 1.5
        self.attack4_duration = 8.0
        self.attack4_spawn_interval = 0.05
        self.attack4_bullet_speed = 200.0
        self.attack4_wave_amplitude = 250.0
        self.attack4_wave_frequency = 5.0

        # 상태 머신 초기화
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def change_state(self, new_state, event):
        if self.cur_state != new_state:
            self.cur_state.exit(self, event)
            self.cur_state = new_state
            self.cur_state.enter(self, event)

    def update(self, frame_time, events=None):
        self.idle_frame = (self.idle_frame + self.animation_speed * frame_time) % 2

        # 현재 상태가 DieState가 아니면, 위아래로 움직이는 로직 실행
        if self.cur_state != DieState:
            self.move(frame_time)

        # 현재 상태의 do() 로직 실행 (각 패턴 로직)
        self.cur_state.do(self, frame_time)

        # 공통 로직 (이펙트, 피격 판정)
        if len(self.attack1_effect) > 0:
            for i in range(len(self.attack1_effect) - 1, -1, -1):
                self.attack1_effect[i][4] = (self.attack1_effect[i][4] + self.attack1_speed * frame_time) % 28
                self.attack1_effect[i][2] -= self.attack1_effect_speed * frame_time
                self.attack1_effect[i][3] -= self.attack1_effect_speed * frame_time
                if self.attack1_effect[i][2] <= 0 or self.attack1_effect[i][3] <= 0:
                    self.attack1_effect.pop(i)

        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2

        if self.hit_animation:
            self.hit_kitty_animation()
        if self.hit:
            self.hit_timer(frame_time)

        # 죽음 판정 (체력이 0 이하이고, 아직 죽음 상태가 아니라면)
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

    # --- 나머지 Helper 함수들 ---
    def move(self, frame_time):
        self.y += self.speed * frame_time * self.dir
        if self.y >= canvas_size.canvasheight - self.height // 2:
            self.dir = -1
        elif self.y <= self.height // 2:
            self.dir = 1

    def ramonatoattack0(self, i):
        ax, ay = self.attack1[i][0], self.attack1[i][1]
        rx, ry = ramona.Ramona_POS_X, ramona.Ramona_POS_Y
        threshold = 40
        dx, dy = ax - rx, ay - ry
        b = (
                        dx * dx + dy * dy <= threshold * threshold) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible
        if b:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)
        return b

    def ramonatoattack1(self, i):
        b = resource.collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                             [canvas_size.canvaswidth // 2, i[0], resource.boss_kitty_uibim_coordinate[int(i[1])][2],
                              int(resource.boss_kitty_uibim_coordinate[int(i[1])][
                                      3] *0.7)]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible
        if b:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def hit_kitty_animation(self):
        self.shape = self.pattern_set[randint(0, resource.pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.hit_animation = False
        self.hit = True
        pass

    def hit_timer(self, frame_time):
        self.hit_time += frame_time
        if self.hit_time > 0.5:
            self.hit = False
            self.hit_time = 0.0
        pass

