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