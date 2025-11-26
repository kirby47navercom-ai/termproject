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
        self.pattern2_target_x = 0
        self.pattern2_landing_x = 0

        self.jump_frame = 0.0

        self.fireballs = []
        self.fireball_speed = 100.0
        self.fireball_jump_power = 1000.0
        self.fireball_gravity = 2500.0

        # 패턴 3
        self.pattern3_state = 0
        self.pattern3_fireball = []
        self.pattern3_fireball_index = 0
        self.pattern3_fireball_speed = 600.0
        self.spread_frame = 0
        self.current_idx = 0

        self.hit = False
        self.hit_animation = False
        self.hit_time = 0.0

        # 패턴 4
        self.pattern4_state = 0
        self.pattern4_enter = False
        self.pattern4_player_x = 0.0
        self.pattern4_move_timer = 0.0
        self.pattern4_move_duration = 0.5
        self.pattern4_speed = 1000.0
        self.scratch_frame = 0.0
        self.pattern4_attack = False
        self.pattern4_attack_frame = 0.0

        # 패턴 5
        self.pattern5_state = 0
        self.pattern5_enter = False
        self.pattern5_player_x = 0.0
        self.scratch_frame2 = 0.0
        self.pattern5_attack_frame = 0.0
        self.pattern5_attack_prepare_timer = 0.0
        self.pattern5_attack_prepare_duration = 1.0
        self.pattern5_attack = False
        self.pattern5_attack_timer = 0.0
        self.pattern5_attack_duration = 0.5

        # 패턴 6
        self.change_phase_1_frame = 0.0
        self.change_phase_1_frame_timer = 0.0
        self.change_phase_1_frame_duration = 3.0

        # 패턴 7
        self.fox_idle_frame = 0
        self.fox_idle_timer = 0.0
        self.fox_idle_time = 1.0

        # 패턴 8
        self.pattern8_state = 0
        self.pattern8_timer = 0.0
        self.pattern8_target_x = 0
        self.pattern8_landing_x = 0

        # 패턴 9
        self.pattern9_state = 0
        self.pattern9_attack_num = 0
        self.scratch_frame3 = 0.0
        self.pattern9_attack = []  # 플레이어 위치 x, 300 ,프레임, 준비시간, 지속시간
        self.pattern9_attack_prepare_duration = 0.5
        self.pattern9_attack_duration = 0.2

        # 패턴 10
        self.pattern10_state = 0
        self.bite_frame = 0.0
        self.pattern10_attack = []  # x,y,프레임,준비시간,첫번째
        self.pattern10_attack_prepare_duration = 0.5

        # 패턴 11
        self.pattern11_state = 0
        self.change_phase_2_frame = 0.0
        self.change_phase_2_frame_timer = 0.0
        self.change_phase_2_frame_duration = 3.0

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

        if self.pattern_num != 14:
            self.update_fireballs(frame_time)
            self.update_pattern3_fireball(frame_time)
            self.update_pattern9_scratch(frame_time)
            self.update_pattern10_bite(frame_time)


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
                self.pattern2_state = 1

                self.pattern2_target_x = ramona.Ramona_POS_X

                distance_x = self.pattern2_target_x - self.x
                self.v_x = distance_x / self.jump_duration

                self.y_velocity = (self.gravity * (self.jump_duration / 2.0))

                self.jump_frame = 0

        elif self.pattern2_state == 1:
            self.x += self.v_x * frame_time
            self.y_velocity -= self.gravity * frame_time
            self.y += self.y_velocity * frame_time

            if self.y_velocity < 0:
                self.pattern2_state = 2
                self.jump_frame = 0

        elif self.pattern2_state == 2:
            self.x += self.v_x * frame_time
            self.y_velocity -= self.gravity * frame_time
            self.y += self.y_velocity * frame_time

            self.jump_frame = (self.jump_frame + self.animation_speed * frame_time) % 4

            if self.y <= self.boss_ground_level:
                self.y = self.boss_ground_level  #
                self.y_velocity = 0
                self.v_x = 0

                self.pattern2_landing_x = self.x
                self.launch_fireballs()

                self.pattern2_state = 3
                self.pattern2_timer = 0.0
                self.jump_frame = 0
                canvas_size.start_shake(0.5, 2.5)

        elif self.pattern2_state == 3:
            self.jump_frame = (self.jump_frame + self.animation_speed * frame_time) % 5

            if int(self.jump_frame) == 4:
                self.pattern_num = 1
                self.pattern2_state = 0
                self.pattern2_timer = 0.0
                self.pattern2_target_x = 0
                self.pattern2_landing_x = 0
                self.jump_frame = 0.0

    def launch_fireballs(self):
        if self.pattern_num == 2:
            start_x = self.pattern2_landing_x
        if self.pattern_num == 8:
            start_x = self.pattern8_landing_x
        start_y = self.boss_ground_level


        angles_deg = [-60, -30, 0, 30, 60]

        for i, angle_deg in enumerate(angles_deg):
            angle_rad = math.radians(angle_deg)


            dir_x = math.sin(angle_rad) * self.fireball_speed * 5


            dir_y = self.fireball_jump_power

            self.fireballs.append([start_x, start_y, dir_x, dir_y, 0, 0.0, True])

    def update_fireballs(self, frame_time):
        for i in range(len(self.fireballs) - 1, -1, -1):
            ball = self.fireballs[i]

            ball[0] += ball[2] * frame_time
            ball[1] += ball[3] * frame_time

            ball[3] -= self.fireball_gravity * frame_time

            if ball[1] < 0:
                self.fireballs.pop(i)
                continue

            self.ramonatofireballs(ball)
            ball[5] = (ball[5] + self.animation_speed * 0.5 * frame_time) % 4

    def ramonatofireballs(self, ball):
        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [ball[0], ball[1], 32, 32]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def pattern3(self, frame_time):
        if self.pattern3_state == 0:
            self.spread_frame = (self.spread_frame + self.animation_speed * frame_time)
            if self.spread_frame >= 3:
                self.pattern3_state = 1
                self.spread_frame = 0
                self.pattern3_fireball_index += 6  ##이거 이용하기
                self.current_idx = 0
        elif self.pattern3_state == 1:
            self.spread_frame = (self.spread_frame + self.animation_speed * frame_time)
            if self.spread_frame >= 2:
                self.pattern3_state = 2
                self.spread_frame = 0
                self.pattern3_fireball.append([self.x + 50, self.y + 100, 0, 0, 0, False, False])

        elif self.pattern3_state == 2:
            self.spread_frame = (self.spread_frame + self.animation_speed * frame_time) % 4
            if self.pattern3_fireball[-1][6]:
                self.pattern3_state = 3
                self.spread_frame = 0

        elif self.pattern3_state == 3:
            self.spread_frame = (self.spread_frame + self.animation_speed * frame_time)
            if self.spread_frame >= 3:
                self.pattern3_state = 0
                self.spread_frame = 0
                self.pattern_num = 1

    def update_pattern3_fireball(self, frame_time):
        ball_idx = [[-50, 100], [-100, 0], [-50, -100], [50, -100], [100, 0]]
        for i in range(len(self.pattern3_fireball) - 1, -1, -1):
            if not self.pattern3_fireball[i][5]:
                self.pattern3_fireball[i][4] = self.pattern3_fireball[i][4] + self.animation_speed * frame_time
                if self.pattern3_fireball[i][4] >= 3:
                    self.pattern3_fireball[i][5] = True
                    self.pattern3_fireball[i][4] = 0
                    if self.current_idx < 5:  # 이거 왜 안댐??
                        self.pattern3_fireball.append(
                            [self.x + ball_idx[self.current_idx][0], self.y + ball_idx[self.current_idx][1], 0, 0, 0,
                             False, False])
                        self.current_idx += 1

            elif self.pattern3_fireball[i][6]:
                self.pattern3_fireball[i][:4] = canvas_size.distance_funtion2(self.pattern3_fireball[i][0],
                                                                              self.pattern3_fireball[i][1],
                                                                              self.pattern3_fireball[i][2],
                                                                              self.pattern3_fireball[i][3],
                                                                              frame_time, self.pattern3_fireball_speed,
                                                                              self.pattern3_fireball[i][2],
                                                                              self.pattern3_fireball[i][3])
                if self.pattern3_fireball[i][1] < -50 or self.pattern3_fireball[i][1] > 2000:
                    self.pattern3_fireball.pop(i)
                    self.pattern3_fireball_index = -1
                    continue
                self.ramonatofireballs(self.pattern3_fireball[i])
                self.pattern3_fireball[i][4] = (self.pattern3_fireball[i][
                                                    4] + self.animation_speed * 0.5 * frame_time) % 4


            else:
                self.ramonatofireballs(self.pattern3_fireball[i])
                self.pattern3_fireball[i][4] = (self.pattern3_fireball[i][4] + self.animation_speed * frame_time) % 4
                if self.current_idx >= 5 and self.pattern3_fireball[len(self.pattern3_fireball) - 1][5]:
                    self.pattern3_fireball[i][6] = True
                    self.pattern3_fireball[i][2] = ramona.Ramona_POS_X
                    self.pattern3_fireball[i][3] = ramona.Ramona_POS_Y

    def pattern4(self, frame_time):
        if self.pattern4_state == 0:
            if not self.pattern4_enter:
                self.pattern4_player_x = ramona.Ramona_POS_X
                self.pattern4_enter = True

            self.pattern4_move_timer += frame_time
            if math.fabs(self.x - ramona.Ramona_POS_X) > 0.5:
                self.x, non = canvas_size.distance_funtion(self.x, 0, self.pattern4_player_x, 0, frame_time,
                                                           self.pattern4_speed)
            self.scratch_frame = min((self.scratch_frame + self.animation_speed * frame_time), 2)
            if self.pattern4_move_timer >= self.pattern4_move_duration:
                self.pattern4_state = 1
                self.pattern4_move_timer = 0.0
                self.scratch_frame = 0
                self.pattern4_enter = False
        elif self.pattern4_state == 1:
            self.scratch_frame = min((self.scratch_frame + self.animation_speed * frame_time), 2)
            if int(self.scratch_frame) == 2 and not self.pattern4_attack:
                self.pattern4_attack = True

            if self.pattern4_attack:
                self.pattern4_attack_frame = (self.pattern4_attack_frame + self.animation_speed * frame_time * 2)
                self.ramonatoscratch()
                if self.pattern4_attack_frame >= 11:
                    self.pattern4_attack = False
                    self.pattern4_attack_frame = 0.0
                    self.pattern4_state = 2
                    self.scratch_frame = 0.0

        elif self.pattern4_state == 2:
            self.scratch_frame = (self.scratch_frame + self.animation_speed * frame_time)
            if self.scratch_frame >= 3:
                self.pattern4_state = 0
                self.scratch_frame = 0.0
                self.pattern_num = 1


    def ramonatoscratch(self):
        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [self.x, self.y, 128 * 2,
                    128 * 2]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def pattern5(self, frame_time):
        if self.pattern5_state == 0:
            if not self.pattern5_enter:
                self.pattern5_player_x = ramona.Ramona_POS_X
                self.pattern5_enter = True
                self.pattern5_attack = True
            self.scratch_frame2 = min((self.scratch_frame2 + self.animation_speed * frame_time),2)
            self.pattern5_attack_prepare_timer += frame_time
            if self.pattern5_attack_prepare_timer >= self.pattern5_attack_prepare_duration:
                resource.stage3_effect_sound[15].set_volume(
                    (resource.stage3_effect_sound_offset[15] * resource.effect) // 2)
                resource.stage3_effect_sound[15].play(1)
                self.pattern5_state = 1
                self.pattern5_attack_prepare_timer = 0.0
                self.scratch_frame2=0
                self.pattern5_enter = False
        elif self.pattern5_state == 1:
            self.scratch_frame2 = self.scratch_frame2 + self.animation_speed * frame_time
            self.pattern5_attack_frame = min((self.pattern5_attack_frame + self.animation_speed * frame_time * 2), 3)
            self.ramonatoscratch2()
            self.pattern5_attack_timer += frame_time
            if self.pattern5_attack_timer >= self.pattern5_attack_duration:
                self.pattern5_attack_frame = 0.0
                self.pattern5_attack_timer = 0.0
                self.pattern5_state = 2
                self.scratch_frame2 = 0
                self.pattern5_attack = False
        elif self.pattern5_state == 2:
            self.scratch_frame2 = (self.scratch_frame2 + self.animation_speed * frame_time)
            if self.scratch_frame2 >= 3:
                self.pattern5_state = 0
                self.scratch_frame2 = 0.0
                self.pattern_num = 1

    def ramonatoscratch2(self):
        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [self.pattern5_player_x, 300, 54 * 2,
                    220 * 2]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def pattern6(self, frame_time):
        if self.change_phase_1_frame_timer < self.change_phase_1_frame_duration:
            self.change_phase_1_frame = min((self.change_phase_1_frame + self.animation_speed * frame_time), 2)
            self.change_phase_1_frame_timer += frame_time

        elif self.change_phase_1_frame_timer >= self.change_phase_1_frame_duration:
            self.change_phase_1_frame = self.change_phase_1_frame + self.animation_speed * frame_time
            if self.change_phase_1_frame >= 17:
                self.pattern_num = 7
                self.change_phase_1_frame = 0.0
                self.change_graphycs = True
                self.change_phase_1_frame_timer = 0.0

    def pattern7(self, frame_time):
        self.fox_idle_frame = (self.fox_idle_frame + self.animation_speed * frame_time) % 8
        self.fox_idle_timer += frame_time
        if self.fox_idle_timer >= self.fox_idle_time:
            self.dir = '' if ramona.Ramona_POS_X > self.x else 'h'
            self.pattern_num=randint(8, 10)
            self.fox_idle_timer = 0.0

        if self.hp<=300:
            self.pattern_num=11

    def pattern8(self, frame_time):
        if self.pattern8_state == 0:
            self.jump_frame = (self.jump_frame + self.animation_speed * frame_time) % 2

            if self.jump_frame >= 1.9:
                self.pattern8_state = 1

                self.pattern8_target_x = ramona.Ramona_POS_X

                distance_x = self.pattern8_target_x - self.x
                self.v_x = distance_x / self.jump_duration

                self.y_velocity = (self.gravity * (self.jump_duration / 2.0))

                self.jump_frame = 0

        elif self.pattern8_state == 1:

            self.x += self.v_x * frame_time
            self.y_velocity -= self.gravity * frame_time
            self.y += self.y_velocity * frame_time

            if self.y_velocity < 0:
                self.pattern8_state = 2
                self.jump_frame = 0

        elif self.pattern8_state == 2:
            self.x += self.v_x * frame_time
            self.y_velocity -= self.gravity * frame_time
            self.y += self.y_velocity * frame_time

            self.jump_frame = (self.jump_frame + self.animation_speed * frame_time) % 5

            if self.y <= self.boss_ground_level:
                self.y = self.boss_ground_level  #
                self.y_velocity = 0
                self.v_x = 0

                self.pattern8_landing_x = self.x
                self.launch_fireballs()

                self.pattern8_state = 3
                self.pattern8_timer = 0.0
                self.jump_frame = 0
                canvas_size.start_shake(0.5, 2.5)

        elif self.pattern8_state == 3:
            self.jump_frame = (self.jump_frame + self.animation_speed * frame_time) % 6

            if int(self.jump_frame) == 5:
                self.pattern_num = 7
                self.pattern8_state = 0
                self.pattern8_timer = 0.0
                self.pattern8_target_x = 0
                self.pattern8_landing_x = 0
                self.jump_frame = 0.0

    def pattern9(self, frame_time):
        if self.pattern9_state == 0:
            self.scratch_frame3 = min((self.scratch_frame3 + self.animation_speed * frame_time), 2)
            if self.scratch_frame3 >= 2:
                self.pattern9_state = 1
                self.scratch_frame3 = 0
                self.pattern9_attack.append([ramona.Ramona_POS_X, 300, 0.0, 0.0, 0.0])
                self.pattern9_attack_num += 1

        elif self.pattern9_state == 1:
            self.scratch_frame3 = min((self.scratch_frame3 + self.animation_speed * frame_time), 1)
            if self.pattern9_attack_num == 1 and self.pattern9_attack[-1][2] > 0.0:
                self.pattern9_attack.append([ramona.Ramona_POS_X, 300, 0.0, 0.0, 0.0])
                self.pattern9_attack_num += 1
            elif self.pattern9_attack_num == 2 and self.pattern9_attack[-1][2] > 0.0:
                self.pattern9_attack.append([ramona.Ramona_POS_X, 300, 0.0, 0.0, 0.0])
                self.pattern9_attack_num += 1
                self.pattern9_state = 2
                self.scratch_frame3 = 0
        elif self.pattern9_state == 2:
            self.scratch_frame3 = min((self.scratch_frame3 + self.animation_speed * frame_time), 1)
            if self.pattern9_attack_num == 3 and self.pattern9_attack[-1][2] > 0.0:
                self.pattern9_attack.append([ramona.Ramona_POS_X, 300, 0.0, 0.0, 0.0])
                self.pattern9_attack_num += 1
            elif self.pattern9_attack_num == 4 and self.pattern9_attack[-1][2] >= 3:
                self.pattern9_state = 3
                self.scratch_frame3 = 0

        elif self.pattern9_state == 3:
            self.scratch_frame3 = (self.scratch_frame3 + self.animation_speed * frame_time)
            if self.scratch_frame3 >= 3:
                self.pattern9_state = 0
                self.scratch_frame3 = 0.0
                self.pattern_num = 7
                self.pattern9_attack_num = 0

    def update_pattern9_scratch(self, frame_time):
        for i in range(len(self.pattern9_attack) - 1, -1, -1):
            self.pattern9_attack[i][3] += frame_time
            if self.pattern9_attack[i][3] >= self.pattern9_attack_prepare_duration:
                self.pattern9_attack[i][2] = min((self.pattern9_attack[i][2] + self.animation_speed * frame_time * 2),
                                                 3)
                if self.pattern9_attack[i][2] >= 3:
                    self.pattern9_attack[i][4] += frame_time
                    self.ramonatoscratch3(self.pattern9_attack[i])
                    if self.pattern9_attack[i][4] >= self.pattern9_attack_duration:
                        self.pattern9_attack.pop(i)
                        continue

    def ramonatoscratch3(self,attack):
        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [attack[0], attack[1], 54 * 2,
                    220 * 2]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def pattern10(self, frame_time):
        if self.pattern10_state == 0:
            self.bite_frame = self.bite_frame + self.animation_speed * frame_time
            if self.bite_frame >= 0:
                self.pattern10_state = 1
                self.bite_frame = 0
        elif self.pattern10_state == 1:
            self.bite_frame = self.bite_frame + self.animation_speed * frame_time
            if self.bite_frame >= 3:
                self.pattern10_state = 2
                self.bite_frame = 0
                self.pattern10_attack.extend([
                    [self.x + (1 if self.dir == '' else -1) * (i + 1) * 320, self.y, 0.0, 0.0,
                     True if i == 0 else False]
                    for i in range(0, 3)
                ])
        elif self.pattern10_state == 2:
            self.bite_frame = (self.bite_frame + self.animation_speed * frame_time)
            if self.bite_frame >= 3:
                self.pattern10_state = 0
                self.bite_frame = 0.0
                self.pattern_num = 7

    def update_pattern10_bite(self, frame_time):
        for i in range(len(self.pattern10_attack) - 1, -1, -1):
            if self.pattern10_attack[i][4] or self.pattern10_attack[i - 1][3] > 0.2:
                self.pattern10_attack[i][3] += frame_time
            if self.pattern10_attack[i][3] >= self.pattern10_attack_prepare_duration:
                self.pattern10_attack[i][2] = self.pattern10_attack[i][2] + self.animation_speed * frame_time
                if self.pattern10_attack[i][2] < 3:
                    self.ramonatobite(self.pattern10_attack[i])
                if self.pattern10_attack[i][2] >= 6:
                    self.pattern10_attack.pop(i)
                    continue

    def ramonatobite(self, attack):
        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [attack[0], attack[1], 160,
                    160]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)

    def pattern11(self, frame_time):
        if self.pattern11_state == 0:
            self.change_phase_2_frame = self.change_phase_2_frame + self.animation_speed * frame_time
            if self.change_phase_2_frame >= 8:
                self.pattern11_state = 1
                self.change_phase_2_frame = 0.0
                canvas_size.start_shake(3.0, 5.0)
        elif self.pattern11_state == 1:


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

        elif self.appear_animation and self.pattern_num == 2:
            # 0: 준비 (3프레임), 1: 상승 (1프레임), 2: 착지/발사 (4프레임), 3: 정리 (5프레임)
            if self.pattern2_state == 0:
                frame_list = resource.boss_siho_jump_prepare_image
            elif self.pattern2_state == 1:
                frame_list = resource.boss_siho_jump_up_image  # 단일 프레임
            elif self.pattern2_state == 2:
                frame_list = resource.boss_siho_jump_cast_image
            elif self.pattern2_state == 3:
                frame_list = resource.boss_siho_jump_over_image
            else:
                return

            current_frame = frame_list[min(int(self.jump_frame), len(frame_list) - 1)]

            current_frame.clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                              self.x - canvas_size.camera_x,
                                              self.y - canvas_size.camera_y,
                                              64 * SIZE, 64 * SIZE)

        elif self.appear_animation and self.pattern_num == 3:
            if self.pattern3_state == 0:
                frame_list = resource.boss_siho_fire_prepare_image
            elif self.pattern3_state == 1:
                frame_list = resource.boss_siho_fire_cast_a_image  # 단일 프레임
            elif self.pattern3_state == 2:
                frame_list = resource.boss_siho_fire_cast_b_image
            elif self.pattern3_state == 3:
                frame_list = resource.boss_siho_fire_over_image
            else:
                return

            current_frame = frame_list[min(int(self.spread_frame), len(frame_list) - 1)]

            current_frame.clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                              self.x - canvas_size.camera_x,
                                              self.y - canvas_size.camera_y,
                                              64 * SIZE, 64 * SIZE)

        elif self.appear_animation and self.pattern_num == 4:
            if self.pattern4_state == 0:
                frame_list = resource.boss_siho_scratch_rush_prepare_image
            elif self.pattern4_state == 1:
                frame_list = resource.boss_siho_scratch_rush_cast_image
            elif self.pattern4_state == 2:
                frame_list = resource.boss_siho_scratch_rush_over_image
            else:
                return

            current_frame = frame_list[min(int(self.scratch_frame), len(frame_list) - 1)]

            current_frame.clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                              self.x - canvas_size.camera_x,
                                              self.y - canvas_size.camera_y,
                                              64 * SIZE, 64 * SIZE)
            if self.pattern4_attack:
                resource.boss_siho_rush_scratch_image[int(self.pattern4_attack_frame)].clip_composite_draw(0, 0, 128,128, 0,
                                                                                                           self.dir,
                                                                                                           self.x - canvas_size.camera_x,
                                                                                                           self.y - canvas_size.camera_y,
                                                                                                           128 * 2,
                                                                                                           128 * 2)
                if canvas_size.collide_check:
                    draw_rectangle(self.x - canvas_size.camera_x - 128,
                                   self.y - canvas_size.camera_y - 128,
                                   self.x - canvas_size.camera_x + 128,
                                   self.y - canvas_size.camera_y + 128)

        elif self.appear_animation and self.pattern_num == 5:
            if self.pattern5_state == 0:
                frame_list = resource.boss_siho_scratch_prepare_image
            elif self.pattern5_state == 1:
                frame_list = resource.boss_siho_scratch_cast_image
            elif self.pattern5_state == 2:
                frame_list = resource.boss_siho_scratch_over_image
            else:
                return
            current_frame = frame_list[min(int(self.scratch_frame2), len(frame_list) - 1)]
            current_frame.clip_composite_draw(0, 0, 64, 64, 0, self.dir,
                                              self.x - canvas_size.camera_x,
                                              self.y - canvas_size.camera_y,
                                              64 * SIZE, 64 * SIZE)
            if self.pattern5_attack:
                resource.boss_siho_scratch_image[int(self.pattern5_attack_frame)].clip_composite_draw(0, 0, 128, 256,
                                                                                                      math.radians(-30),
                                                                                                      '',
                                                                                                      self.pattern5_player_x - canvas_size.camera_x,
                                                                                                      300 - canvas_size.camera_y,
                                                                                                      128 * 2, 256 * 2)
                if canvas_size.collide_check:
                    draw_rectangle(self.pattern5_player_x - canvas_size.camera_x - 54,
                                   300 - canvas_size.camera_y - 220,
                                   self.pattern5_player_x - canvas_size.camera_x + 54,
                                   300 - canvas_size.camera_y + 220)

        elif self.appear_animation and self.pattern_num == 6:
            resource.boss_fox_change_image[int(self.change_phase_1_frame)].clip_composite_draw(0, 0, 128, 64, 0,
                                                                                               self.dir,
                                                                                               self.x - canvas_size.camera_x,
                                                                                               self.y - canvas_size.camera_y,
                                                                                               128 * SIZE, 64 * SIZE)

        elif self.appear_animation and self.pattern_num == 7:
            resource.boss_fox_idle_image[int(self.fox_idle_frame)].clip_composite_draw(0, 0, 96, 64, 0, self.dir,
                                                                                       self.x - canvas_size.camera_x,
                                                                                       self.y - canvas_size.camera_y,
                                                                                       96 * SIZE, 64 * SIZE)

        elif self.appear_animation and self.pattern_num == 8:
            if self.pattern8_state == 0:
                frame_list = resource.boss_fox_jump_prepare_image
            elif self.pattern8_state == 1:
                frame_list = resource.boss_fox_jump_up_image  # 단일 프레임
            elif self.pattern8_state == 2:
                frame_list = resource.boss_fox_jump_cast_image
            elif self.pattern8_state == 3:
                frame_list = resource.boss_fox_jump_over_image
            else:
                return

            current_frame = frame_list[min(int(self.jump_frame), len(frame_list) - 1)]

            if self.pattern8_state == 0:
                current_frame.clip_composite_draw(0, 0, 96, 64, 0, self.dir,
                                                  self.x - canvas_size.camera_x,
                                                  self.y - canvas_size.camera_y,
                                                  96 * SIZE, 64 * SIZE)
            else:
                current_frame.clip_composite_draw(0, 0, 96, 96, 0, self.dir,
                                                  self.x - canvas_size.camera_x,
                                                  self.y - canvas_size.camera_y,
                                                  96 * SIZE, 96 * SIZE)

        elif self.appear_animation and self.pattern_num == 9:
            if self.pattern9_state == 0:
                frame_list = resource.boss_fox_scratch_prepare_image
            elif self.pattern9_state == 1:
                frame_list = resource.boss_fox_scratch_cast_a_image
            elif self.pattern9_state == 2:
                frame_list = resource.boss_fox_scratch_cast_b_image
            elif self.pattern9_state == 3:
                frame_list = resource.boss_fox_scratch_over_image

            else:
                return

            current_frame = frame_list[min(int(self.scratch_frame3), len(frame_list) - 1)]

            current_frame.clip_composite_draw(0, 0, 96, 64, 0, self.dir,
                                              self.x - canvas_size.camera_x,
                                              self.y - canvas_size.camera_y,
                                              96 * SIZE, 64 * SIZE)

        elif self.appear_animation and self.pattern_num == 10:
            if self.pattern10_state == 0:
                frame_list = resource.boss_fox_bite_prepare_image
            elif self.pattern10_state == 1:
                frame_list = resource.boss_fox_bite_cast_image
            elif self.pattern10_state == 2:
                frame_list = resource.boss_fox_bite_over_image
            else:
                return
            current_frame = frame_list[min(int(self.bite_frame), len(frame_list) - 1)]

            current_frame.clip_composite_draw(0, 0, 96 if self.pattern10_state != 1 else 128, 64,
                                              0, self.dir,
                                              self.x - canvas_size.camera_x,
                                              self.y - canvas_size.camera_y,
                                              (96 if self.pattern10_state != 1 else 128) * SIZE, 64 * SIZE)



        if self.hp >= 0 and self.pattern_num != 14:
            for ball_a in self.fireballs:
                if ball_a[6]:
                    frame_idx = int(ball_a[5])
                    fire_image = resource.boss_siho_fire_a_image[frame_idx]

                    fire_image.draw(ball_a[0] - canvas_size.camera_x,
                                    ball_a[1] - canvas_size.camera_y,
                                    32 * 2, 32 * 2)

                    if canvas_size.collide_check:
                        draw_rectangle(ball_a[0] - 16 - canvas_size.camera_x,
                                       ball_a[1] - 16 - canvas_size.camera_y,
                                       ball_a[0] + 16 - canvas_size.camera_x,
                                       ball_a[1] + 16 - canvas_size.camera_y)

            for ball_b in self.pattern3_fireball:
                frame_idx = int(ball_b[4])
                if ball_b[5]:
                    fire_image = resource.boss_siho_fire_b_image[frame_idx]
                else:
                    fire_image = resource.boss_siho_fire_b_appear_image[frame_idx]

                fire_image.draw(ball_b[0] - canvas_size.camera_x,
                                ball_b[1] - canvas_size.camera_y,
                                32 * 2, 32 * 2)

                if canvas_size.collide_check:
                    draw_rectangle(ball_b[0] - 16 - canvas_size.camera_x,
                                   ball_b[1] - 16 - canvas_size.camera_y,
                                   ball_b[0] + 16 - canvas_size.camera_x,
                                   ball_b[1] + 16 - canvas_size.camera_y)

            for attack in self.pattern9_attack:
                resource.boss_siho_scratch_image[int(attack[2])].clip_composite_draw(0, 0, 128, 256, math.radians(-30),
                                                                                     '',
                                                                                     attack[0] - canvas_size.camera_x,
                                                                                     attack[1] - canvas_size.camera_y,
                                                                                     128 * 2, 256 * 2)
                if canvas_size.collide_check:
                    draw_rectangle(attack[0] - canvas_size.camera_x - 54,
                                   attack[1] - canvas_size.camera_y - 220,
                                   attack[0] - canvas_size.camera_x + 54,
                                   attack[1] - canvas_size.camera_y + 220)

            for bite in self.pattern10_attack:
                resource.boss_siho_bite_image[int(bite[2])].clip_composite_draw(0, 0, 160, 160, 0, '',
                                                                                bite[0] - canvas_size.camera_x,
                                                                                bite[1] - canvas_size.camera_y,
                                                                                160 * 2, 160 * 2)
                if canvas_size.collide_check:
                    draw_rectangle(bite[0] - canvas_size.camera_x - 80,
                                   bite[1] - canvas_size.camera_y - 80,
                                   bite[0] - canvas_size.camera_x + 80,
                                   bite[1] - canvas_size.camera_y + 80)

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
