from pico2d import *
import canvas_size
import game_framework
import resource
import stage2_manager

black_background = None
choose = None
stage1 = None

def init():
    global choose, stage1, black_background
    black_background = load_image('배경\\black_background.png')
    choose = load_image('배경\\choose.png')
    stage1 = load_image('배경\\stage2.png')


def update(frame_time,events):