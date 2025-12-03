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
    # 시간 체크를 해주고
    if get_time() - logo_start_time > 2.0:
        game_framework.change_mode(title_mode)

def draw():
    image.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)


def finish():
    pass


def pause():
    pass
def resume():
    pass