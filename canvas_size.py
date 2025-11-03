import random
import math
canvaswidth = 1280
canvasheight = 720

shake_x, shake_y = 0, 0
camera_x, camera_y = 0, 0
shake_timer = 0.0  # 흔들림이 지속될 시간
shake_magnitude = 10.0 # 흔들림의 강도

def start_shake(duration, magnitude):
    global shake_timer, shake_magnitude
    shake_timer = duration
    shake_magnitude = magnitude

def update_shake(frame_time):
    global shake_x, shake_y, shake_timer, shake_magnitude
    if shake_timer > 0:
        shake_timer -= frame_time
        # 카메라 위치를 -강도 ~ +강도 범위 내에서 무작위로 변경
        shake_x = random.uniform(-shake_magnitude, shake_magnitude)
        shake_y = random.uniform(-shake_magnitude, shake_magnitude)
        if shake_timer <= 0:
            shake_x, shake_y = 0, 0  # 흔들림이 끝나면 카메라 위치 초기화

def cout(a):
    print(a)