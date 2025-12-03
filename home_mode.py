from pico2d import *
import canvas_size
import ending_mode
import game_framework
import option_mode
import resource
import na25_mode
import stage1_ready_mode
import stage2_ready_mode
import stage3_ready_mode

home = None
stage1 = []
stage2 = []
stage3 = []
coin = None
sugar = None
water = None
lemon = None
coin_font = None

def init():
    # 로고 이미지를 로드
    global home, stage1, stage2, stage3, coin, sugar, water, lemon, coin_font

    if home == None:
        home = load_image('배경\\stage_memu.png')
        stage1 = [load_image('배경\\normal1.png'), load_image('배경\\perfect1.png')]
        stage2 = [load_image('배경\\normal2.png'), load_image('배경\\perfect2.png')]
        stage3 = [load_image('배경\\normal3.png'), load_image('배경\\perfect3.png')]
        coin = load_image('배경\\coin.png')
        sugar = load_image('배경\\clear1.png')
        water = load_image('배경\\clear2.png')
        lemon = load_image('배경\\clear3.png')
        coin_font = load_font('Font\\경기천년바탕_Bold.ttf', 80)


def update(frame_time,events):
    if not resource.ending and resource.stage1_clear != 0 and resource.stage2_clear != 0 and resource.stage3_clear != 0:
        resource.ending = True
        game_framework.push_mode(ending_mode)
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 15 <= x <= 305 and 130 <= y <= 545:

                game_framework.push_mode(stage1_ready_mode)
            elif 500 <= x <= 790 and 130 <= y <= 545:

                game_framework.push_mode(stage2_ready_mode)
            elif 965 <= x <= 1255 and 130 <= y <= 545:

                game_framework.push_mode(stage3_ready_mode)
            elif 1145 <= x <= 1255 and 585 <= y <= 690:

                game_framework.push_mode(option_mode)
            elif 495 <= x <= 855 and 605 <= y <= 670:

                game_framework.change_mode(na25_mode)

def draw():
    home.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    # print(resource.stage1_clear,resource.stage2_clear,resource.stage3_clear)

    if resource.stage1_clear == 1:
        stage1[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.stage1_clear == 2:
        stage1[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    if resource.stage1_clear >= 1:
        sugar.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.stage2_clear == 1:
        stage2[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.stage2_clear == 2:
        stage2[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    if resource.stage2_clear >= 1:
        water.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.stage3_clear == 1:
        stage3[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.stage3_clear == 2:
        stage3[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    if resource.stage3_clear >= 1:
        lemon.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    coin.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    coin_font.draw(80, canvas_size.canvasheight - 40, 'X ' + str(resource.coin), (0, 0, 0))
    if canvas_size.collide_check:
        draw_rectangle(15, 130, 305, 545)
        draw_rectangle(500, 130, 790, 545)
        draw_rectangle(965, 130, 1255, 545)
        draw_rectangle(1145, 585, 1255, 690)
        draw_rectangle(495, 605, 855, 670)

def finish():

    pass


def pause():
    pass