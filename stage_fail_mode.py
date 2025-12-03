from pico2d import *
import canvas_size
import game_framework
import home_mode
import resource


black_background = None
fail = None
fail_no = None
food = []


def init():
    # 로고 이미지를 로드
    global black_background,fail,food,fail_no



    if black_background == None:
        black_background = load_image('배경\\black_background.png')
        fail = load_image('배경\\fail.png')
        food = [load_image('배경\\sugar.png'),load_image('배경\\water.png'),
                load_image('배경\\lemon.png')]
        fail_no = load_image('배경\\fail_no.png')

