from pico2d import *
import canvas_size
import game_framework
import resource

ending_image = None
black_background=None
current_image = 0
alpha = 0
FADE_SPEED = 10  # 알파값 증가 속도

def init():
    global ending_image, current_image, alpha,black_background
    if ending_image is None:
        ending_image = resource.end_image
        black_background = load_image('배경\\black_background.png')
    current_image = 0
    alpha = 0

