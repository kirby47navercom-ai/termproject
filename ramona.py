from pico2d import *
import time
import resource
import canvas_size
import draw_gesture
import random

# 물리
GRAVITY = 2000.0
GROUND_LEVEL = 100
WIDTH_LEVEL = canvas_size.canvaswidth-25
# 속도 (pixel/sec)
WALK_SPEED = 200.0
RUN_SPEED = 350.0
EVADE_SPEED = 500.0
JUMP_POWER = 600.0
DEATH_KNOCKBACK_SPEED = 150.0
# 시간
EVADE_DURATION = 0.3
DOUBLE_TAP_INTERVAL = 0.2
EVADE_COOLDOWN = 1.5
#플레이어 체력
MAX_HP = 3
CURRENT_HP = 3
#플레이어의 크기
Ramona_SIZE_X=30
Ramona_SIZE_Y=64
#플레이어의 위치
Ramona_POS_X=100
Ramona_POS_Y=GROUND_LEVEL
#플레이어 무적
Ramona_invincible_timer=0.0
Ramona_roll_invincible=False
Ramona_invincible=False
hit_toggle=False
#플레이어의 공격력
Ramona_attack=20
#플레이어의 공격
Ramona_smash=False
Ramona_smash_toggle=False
#플레이어 점프할때 속도
Ramona_jump_speed=0
#플레이어 죽었다는 표시
Ramona_dead=False

A_DOWN, D_DOWN, A_UP, D_UP = range(4)
SHIFT_DOWN, SHIFT_UP, SPACE_DOWN, SPACE_UP = range(4, 8)
A_D_TAP, D_D_TAP = range(8, 10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
    (SDL_KEYUP, SDLK_a): A_UP,
    (SDL_KEYUP, SDLK_d): D_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP, # SPACE_UP 추가
}
class DeadState:
    def enter(self, event):
        global Ramona_dead
        self.frame = 0
        Ramona_dead = True
        self.knockback_timer = 2.0

    def exit(self, event):
        pass

    def do(self, frame_time):
        if self.knockback_timer > 0:
            dir= 1 if self.flip else -1
            self.x += dir * DEATH_KNOCKBACK_SPEED * frame_time
            self.knockback_timer -= frame_time

        total_frames = len(self.coordinate['dead'])
        self.frame = self.frame + self.animation_speed * frame_time / 3
        if self.frame >= total_frames:
            self.frame = total_frames - 1

        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time

    def draw(self):
        self.draw_sprite('dead')

    def handle_event(self, event):
        pass


class Ramona:
    image=None

    def __init__(self):
        self.x, self.y = canvas_size.canvaswidth // 2, GROUND_LEVEL
        self.y_velocity = 0
        self.frame = 0.0
        self.dir = 0
        self.flip = False
        self.animation_speed = 8.0
        if Ramona.image == None:
            Ramona.image = resource.ramona_image
        self.coordinate = resource.ramona_coordinate
        self.attack_motion = None
        self.last_key_time = {'a': 0, 'd': 0}
        self.jump_count = 0
        self.evade_cooldown_timer = 0.0
        self.knockback_timer = 2.0
        # 키 눌림 상태 추적
        self.a_pressed = False
        self.d_pressed = False

        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.shift_pressed = False

    def change_state(self, new_state, event):
        if self.cur_state != new_state:
            self.cur_state.exit(self, event)
            self.cur_state = new_state
            self.cur_state.enter(self, event)
            self.frame = 0.0


    def update(self, frame_time, events):
        global Ramona_POS_X, Ramona_POS_Y, Ramona_invincible_timer, Ramona_invincible, hit_toggle, CURRENT_HP, Ramona_smash, Ramona_smash_toggle
        global WIDTH_LEVEL, GROUND_LEVEL

        if Ramona_smash and self.cur_state not in [AttackState, HitState, EvadeState] and not Ramona_smash_toggle:
            self.change_state(AttackState, None)
            Ramona_smash = False
            Ramona_smash_toggle = True
        elif not draw_gesture.f_pressed and not Ramona_smash and not Ramona_smash_toggle:

            self.a_pressed = False
            self.d_pressed = False
            self.shift_pressed = False
            self.dir = 0

            if self.cur_state != IdleState:
                self.change_state(IdleState, None)

            self.cur_state.do(self, frame_time)
        else:

            self.handle_event(frame_time,events)
            self.cur_state.do(self, frame_time)


            if self.evade_cooldown_timer > 0:
                self.evade_cooldown_timer -= frame_time


            if self.cur_state in [IdleState, WalkState, RunState]:
                if self.a_pressed == self.d_pressed:
                    self.dir = 0
                    if self.cur_state in [WalkState, RunState]:
                        self.change_state(IdleState, None)
                elif self.a_pressed:
                    self.dir = -1
                    if self.cur_state == IdleState:
                        self.change_state(WalkState, None)
                elif self.d_pressed:
                    self.dir = 1
                    if self.cur_state == IdleState:
                        self.change_state(WalkState, None)

        self.y_velocity -= GRAVITY * frame_time
        self.y += self.y_velocity * frame_time

        on_ground = False
        for bx, by, bw, bh in resource.blocks:
            block_left, block_right = bx - bw / 2, bx + bw / 2
            block_bottom, block_top = by - bh / 2, by + bh / 2

            if resource.collide([self.x, self.y, Ramona_SIZE_X, Ramona_SIZE_Y],
                                [bx, by, bw, bh]):  # a. 아래로 떨어지며 발판을 밟았을 때
                dx = self.x - bx
                dy = self.y - by
                overlap_x = (Ramona_SIZE_X / 2 + bw / 2) - abs(dx)
                overlap_y = (Ramona_SIZE_Y / 2 + bh / 2) - abs(dy)

                if overlap_y < overlap_x:
                    # 수직 충돌
                    if self.y_velocity <= 0 and dy > 0:  # 아래로 떨어지며 위를 밟았을 때
                        self.y = block_top + Ramona_SIZE_Y / 2
                        self.y_velocity = 0
                        self.jump_count = 0
                        on_ground = True
                        continue
                    elif self.y_velocity > 0 and dy < 0:  # 위로 점프하며 아래를 박았을 때
                        self.y = block_bottom - Ramona_SIZE_Y / 2
                        self.y_velocity = 0
                else:
                    # 수평 충돌
                    if dx < 0:
                        self.x = block_left - Ramona_SIZE_X / 2
                    else:
                        self.x = block_right + Ramona_SIZE_X / 2
        # 3. 어떤 발판 위에도 있지 않다면, 최종 바닥(GROUND_LEVEL) 확인
        if not on_ground and self.y <= GROUND_LEVEL:
            self.y = GROUND_LEVEL
            self.y_velocity = 0
            self.jump_count = 0
            on_ground = True

        if on_ground:  # 땅이나 발판 위에 있다면
            if self.cur_state == JumpState:  # 막 착지했다면
                if self.a_pressed or self.d_pressed:
                    self.change_state(WalkState, None)
                else:
                    self.change_state(IdleState, None)
        else:  # 공중에 있다면
            if self.cur_state in [IdleState, WalkState, RunState]:  # 발판에서 떨어졌다면
                self.change_state(JumpState, None)

        self.x = clamp(25, self.x, WIDTH_LEVEL)
        self.y = clamp(GROUND_LEVEL, self.y, 720 - 50)

        if self.dir == -1:
            self.flip = True
        elif self.dir == 1:
            self.flip = False
        global hit_toggle

        if Ramona_invincible:

            Ramona_invincible_timer += frame_time

            if not hit_toggle:
                hit_toggle = True
                if CURRENT_HP > 0:
                    self.change_state(HitState, None)
                else:
                    self.change_state(DeadState, None)
                    pass
            if Ramona_invincible_timer >= 2.0:
                Ramona_invincible = False
                Ramona_invincible_timer = 0.0
                hit_toggle = False

        Ramona_POS_X = self.x
        Ramona_POS_Y = self.y


    def handle_event(self, frame_time, events):
        for event in events:
            if (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]


                if key_event == A_DOWN:
                    self.a_pressed = True
                elif key_event == A_UP:
                    self.a_pressed = False
                elif key_event == D_DOWN:
                    self.d_pressed = True
                elif key_event == D_UP:
                    self.d_pressed = False
                elif key_event == SHIFT_DOWN:
                    self.shift_pressed = True
                elif key_event == SHIFT_UP:
                    self.shift_pressed = False


                if key_event == A_DOWN and self.evade_cooldown_timer <= 0:
                    if time.time() - self.last_key_time['a'] < DOUBLE_TAP_INTERVAL:
                        self.cur_state.handle_event(self, A_D_TAP)
                    else:
                        self.cur_state.handle_event(self, A_DOWN)
                    self.last_key_time['a'] = time.time()
                elif key_event == D_DOWN and self.evade_cooldown_timer <= 0:
                    if time.time() - self.last_key_time['d'] < DOUBLE_TAP_INTERVAL:
                        self.cur_state.handle_event(self, D_D_TAP)
                    else:
                        self.cur_state.handle_event(self, D_DOWN)
                    self.last_key_time['d'] = time.time()
                else:
                    self.cur_state.handle_event(self, key_event)

    def draw_sprite(self, state_name, frame_idx=None):
        if frame_idx is None:
            frame_idx = int(self.frame)

        if state_name not in self.coordinate or frame_idx >= len(self.coordinate[state_name]):
            return

        left, bottom, width, height, jx, jy = self.coordinate[state_name][frame_idx]

        if not self.flip:
            self.image[state_name].clip_draw(left, bottom, width, height, self.x+jx-canvas_size.camera_x, self.y+jy-canvas_size.camera_y, width, height)
        else:
            self.image[state_name].clip_composite_draw(left, bottom, width, height, 0, 'h', self.x-jx-canvas_size.camera_x, self.y+jy-canvas_size.camera_y, width,
                                                       height)


    def draw(self):
        global Ramona_invincible

        if Ramona_invincible:
            if (get_time() % 0.2) > 0.1:
                self.cur_state.draw(self)
        else:
            self.cur_state.draw(self)