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