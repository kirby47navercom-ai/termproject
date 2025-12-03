from pico2d import *
import canvas_size
import game_framework
import resource
import stage3_manager

black_background = None
choose = None
stage1 = None

def init():
    global choose, stage1, black_background
    black_background = load_image('배경\\black_background.png')
    choose = load_image('배경\\choose.png')
    stage1 = load_image('배경\\stage3.png')

def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 240 <= x <= 530 and 230 <= y <= 360:

                game_framework.pop_mode()
                game_framework.change_mode(stage3_manager)
            elif 750 <= x <= 1040 and 230 <= y <= 360:

                game_framework.pop_mode()

def draw():
    black_background.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    choose.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    stage1.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if canvas_size.collide_check:
        draw_rectangle(240, 230, 530, 360)

        draw_rectangle(750, 230, 1040, 360)

def finish():
    global black_background, choose, stage1
    del black_background,choose,stage1
    pass
def pause():
    pass
def resume():
    pass