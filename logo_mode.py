from pico2d import *
import canvas_size
import game_framework
import title_mode

image = None
logo_start_time = 0

def init():
    # 로고 이미지를 로드
    global image, logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def update(frame_time,events):
    pass

def draw():
    pass


def finish():
    pass


def pause():
    pass
def resume():
    pass