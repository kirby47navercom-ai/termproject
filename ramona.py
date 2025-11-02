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
        pass

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
        pass