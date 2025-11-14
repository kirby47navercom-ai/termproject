from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
from canvas_size import *
import canvas_size
import ramona


SIZE = 1.2

class CutsceneState:
    def enter(self, event):
        self.cutscene_timer = 0.0
        self.speed = 50
        self.pattern_num = -1

    def exit(self, event):
        self.cutscene = True
        self.speed = 100

    def do(self, frame_time):
        self.cutscene_timer += frame_time
        if self.cutscene_timer >= self.cutscene_time:
            self.change_state(ReadyState, None)
        else:
            self.y -= self.speed * frame_time
            canvas_size.start_shake(0.1, 3)

    def draw(self):
        a = boss_ghost_idle_coordinate[int(self.idle_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)


        if canvas_size.collide_check:
            draw_rectangle(self.x - width * SIZE / 2,
                           self.y - height * SIZE / 2,
                           self.x + width * SIZE / 2,
                           self.y + height * SIZE / 2)


class ReadyState:
    def enter(self, event):
        self.pattern_ready_timer = 0.0
        self.pattern_num = -1

    def exit(self, event):
        pass

    def do(self, frame_time):
        self.pattern_ready_timer += frame_time
        if self.pattern_ready_timer >= self.pattern_ready_time:
            self.change_state(Pattern0State, None)

    def draw(self):
        a = boss_ghost_idle_coordinate[int(self.idle_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)

        if canvas_size.collide_check:
            draw_rectangle(self.x - width * SIZE / 2,
                           self.y - height * SIZE / 2,
                           self.x + width * SIZE / 2,
                           self.y + height * SIZE / 2)


class Pattern0State:
    def enter(self, event):
        self.pattern_ready = False
        self.pattern0_ready_timer = 0.0
        self.pattern_state = 0
        self.pattern_num = 0

    def exit(self, event):
        self.pattern_state = 0

    def do(self, frame_time):
        if not self.pattern_ready:
            x, y = self.width, self.height
            self.x, self.y = distance_funtion(self.x, self.y, x, y, frame_time, self.pattern_ready_speed)
            if abs(self.x - x) <= 5 and abs(self.y - y) <= 5:
                self.pattern_ready = True
        elif self.pattern0_ready_timer < self.pattern0_ready_time:
            self.pattern0_ready_timer += frame_time
        else:
            self.pattern_state = 2
            self.x += self.speed * 6 * frame_time * self.pattern_speed
            if self.x >= canvas_size.canvaswidth + 50:
                self.rereset(Pattern2State)

    def draw(self):
        if self.pattern_state == 2:
            a = boss_ghost_pattern1_coordinate[1]
        else:
            a = boss_ghost_idle_coordinate[int(self.idle_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)


        if canvas_size.collide_check:
            draw_rectangle(self.x - width * SIZE / 2,
                           self.y - height * SIZE / 2,
                           self.x + width * SIZE / 2,
                           self.y + height * SIZE / 2)




class Pattern1State:
    def enter(self, event):
        self.pattern_ready = False
        self.pattern0_ready_timer = 0.0
        self.pattern_state = 0
        self.pattern_num = 1
        self.pattern1_x, self.pattern1_y = randint(int(self.width),
                                                   int(canvas_size.canvaswidth - self.width)), canvas_size.canvasheight // 2 + canvas_size.canvasheight // 4
        self.pattern1_frame = 0

    def exit(self, event):
        self.pattern_state = 0

    def do(self, frame_time):
        if not self.pattern_ready:
            self.x, self.y = distance_funtion(self.x, self.y, self.pattern1_x, self.pattern1_y, frame_time,
                                              self.pattern_ready_speed)
            if abs(self.x - self.pattern1_x) <= 5 and abs(self.y - self.pattern1_y) <= 5:
                self.pattern_ready = True
        elif self.pattern0_ready_timer < self.pattern0_ready_time:
            self.pattern0_ready_timer += frame_time
            self.pattern1_x, self.pattern1_y = ramona.Ramona_POS_X, ramona.Ramona_POS_Y
        else:
            self.pattern_state = 3
            self.x, self.y = distance_funtion(self.x, self.y, self.pattern1_x, self.pattern1_y, frame_time,
                                              self.speed * 6 * self.pattern_speed)
            self.pattern1_frame = (self.pattern1_frame + self.die_animation_speed * frame_time) % 5
            if abs(self.x - self.pattern1_x) <= 5 and abs(self.y - self.pattern1_y) <= 5:
                self.rereset(Pattern2State)

    def draw(self):
        if self.pattern_state == 3:
            a = boss_ghost_pattern2_coordinate[int(self.pattern1_frame)]
        else:
            a = boss_ghost_idle_coordinate[int(self.idle_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)

        if canvas_size.collide_check:
            draw_rectangle(self.x - width * SIZE / 2,
                           self.y - height * SIZE / 2,
                           self.x + width * SIZE / 2,
                           self.y + height * SIZE / 2)



class Pattern2State:
    def enter(self, event):
        self.attack_timer = 0.0
        self.pattern_num = 2

    def exit(self, event):
        pass

    def do(self, frame_time):
        self.x, self.y = distance_funtion(self.x, self.y, ramona.Ramona_POS_X, ramona.Ramona_POS_Y, frame_time,
                                          self.speed)
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

        self.attack_timer += frame_time
        if self.attack_timer >= self.attack_time or self.hit_num <= 0:
            self.attack_timer = 0
            if self.prev_pattern == 0:
                self.prev_pattern = 1
                self.rereset(Pattern1State)
            else:
                self.prev_pattern = 0
                self.rereset(Pattern0State)

    def draw(self):
        a = boss_ghost_idle_coordinate[int(self.idle_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)

        if canvas_size.collide_check:
            draw_rectangle(self.x - width * SIZE / 2,
                           self.y - height * SIZE / 2,
                           self.x + width * SIZE / 2,
                           self.y + height * SIZE / 2)

        self.shape.draw()

class HitState:
    def enter(self, event):
        self.hit_frame = 0

    def exit(self, event):
        self.hit_animation = False
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

    def do(self, frame_time):
        self.hit_frame = (self.hit_frame + self.hit_animation_speed * frame_time) % 4
        if int(self.hit_frame) == 3:
            self.change_state(self.previous_state, None)

    def draw(self):
        a = boss_ghost_hit_coordinate[int(self.hit_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)



class DieState:
    def enter(self, event):
        self.die_frame = 0
        self.shape.name = 'No'
        self.pattern_num = -1

    def exit(self, event):
        pass

    def do(self, frame_time):
        if not self.die:
            self.die_frame = (self.die_frame + self.die_animation_speed * frame_time) % 8
            canvas_size.start_shake(0.5, 5)
            if int(self.die_frame) == 7:
                self.die = True

    def draw(self):
        a = boss_ghost_die_coordinate[int(self.die_frame)]
        left, bottom, width, height, jx, jy = a
        self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                       self.y + jy - canvas_size.shake_y, width * SIZE, height * SIZE)


class Boss_Ghost:
    image = None

    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Boss_Ghost.image == None:
            Boss_Ghost.image = load_image('1stage\\level1-png-sprite.png')
        self.x, self.y = canvas_size.canvaswidth // 2, canvas_size.canvasheight + 100
        self.boss_hp = 240
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
        self.width, self.height = 70 * SIZE, 104 * SIZE
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 50
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7
        self.idle_frame = 0
        self.die = False
        self.die_animation = False
        self.die_animation_speed = 2.0
        self.die_frame = 0
        self.hit = False
        self.hit_animation = False
        self.hit_animation_speed = 8.0

        self.pattern_speed = 1
        self.half_hp = False

        self.cutscene = False
        self.cutscene_time = 7
        self.pattern_ready_time = 1.0
        self.pattern_ready_speed = 1000
        self.pattern0_ready_time = 0.5
        self.hit_num = 3
        self.attack_time = 8.0
        self.prev_pattern = 0

        self.pattern_num = -1
        self.pattern_ready_timer = 0.0
        self.pattern_ready = False
        self.pattern_state = 0
        self.pattern1_x = 0
        self.pattern1_y = 0
        self.pattern1_frame = 0

        self.cur_state = CutsceneState
        self.previous_state = CutsceneState
        self.cur_state.enter(self, None)

    def change_state(self, new_state, event):
        if self.cur_state != new_state:
            self.previous_state = self.cur_state
            self.cur_state.exit(self, event)
            self.cur_state = new_state
            self.cur_state.enter(self, event)

    def update(self, frame_time, events=None):
        self.idle_frame = (self.idle_frame + self.hit_animation_speed * frame_time) % 4

        if self.hit_animation and self.cur_state not in [HitState, DieState]:
            self.change_state(HitState, None)

        if self.hp <= 0 and self.cur_state != DieState:
            self.die_animation = True
            self.change_state(DieState, None)

        self.cur_state.do(self, frame_time)

        self.ramonatoghost()

        if self.hp <= 120 and not self.half_hp:
            self.pattern_speed = 2
            self.half_hp = True

    def draw(self):
        if not self.die:
            self.cur_state.draw(self)

            if self.cur_state not in [DieState]:
                self.hp_bar.draw(self.hp, self.boss_hp)

            if not self.die_animation and self.cutscene and self.pattern_ready_timer >= self.pattern_ready_time and self.hit_num > 0 and self.cur_state == Pattern2State:
                self.shape.draw()

    def rereset(self, next_state_class):
        self.pattern_ready = False
        self.pattern0_ready_timer = 0.0
        self.pattern_state = 0
        self.x = randint(int(self.width), int(canvas_size.canvaswidth - self.width))
        self.y = canvas_size.canvasheight + self.height

        if next_state_class == Pattern2State:
            remainder = self.hp % 60
            if remainder > 40 or remainder == 0:
                self.hit_num = 3
            elif remainder > 20:
                self.hit_num = 2
            else:
                self.hit_num = 1

        self.change_state(next_state_class, None)

    def ramonatoghost(self):
        if self.cur_state == DieState: return

        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [self.x, self.y, self.width,
                    self.height]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                canvas_size.start_shake(0.5, 5.0)