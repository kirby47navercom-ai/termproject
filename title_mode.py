from pico2d import *
import canvas_size
import game_framework
import option_mode
import  home_mode
import resource

image = None

def init():
    # 로고 이미지를 로드
    global image

    image = load_image('배경//main.png')


def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, get_canvas_height() - 1 - event.y
            if 410 <= x <= 618 and 30 <= y <= 100:
                game_framework.change_mode(home_mode)


            elif 660 <= x <= 868 and 30 <= y <= 100:
                game_framework.push_mode(option_mode)


def draw():
    # 로고 이미지를 그려준다
    image.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    if canvas_size.collide_check:
        i = 120
        j = 100
        draw_rectangle(410, 30, 618, 100)  # 시작
        draw_rectangle(660, 30, 868, 100)  # 설정

def finish():
    global image
    del image

def pause():
    pass

def resume():
    pass