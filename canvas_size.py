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

def distance_funtion(x1, y1, x2, y2,frame_time,speed):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    x3 = x1 + (x2 - x1) * speed * frame_time / distance
    y3 = y1 + (y2 - y1) * speed * frame_time / distance
    return x3, y3

def distance_funtion2(x1, y1, x2, y2,frame_time,speed,x4,y4):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    x3 = x1 + (x2 - x1) * speed * frame_time / distance
    y3 = y1 + (y2 - y1) * speed * frame_time / distance
    x4 = x4 + (x2 - x1) * speed * frame_time / distance
    y4 = y4 + (y2 - y1) * speed * frame_time / distance
    return x3, y3,x4, y4

def cout(a):
    print(a)