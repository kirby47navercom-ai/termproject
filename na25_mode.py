from pico2d import *
import canvas_size
import game_framework
import resource
import home_mode
import ramona

background= None
nanahira = []
inventory=None
coin = None
coin_font = None
weapon1 = []
weapon2 = []
weapon3 = []
weapon4 = []
talk = []

def init():
    # 로고 이미지를 로드
    global coin, coin_font, background, nanahira, inventory, weapon1, weapon2, weapon3, weapon4, talk

    if background == None:
        background = load_image('배경\\na25_background.png')
        nanahira = [load_image('배경\\na1.png'), load_image('배경\\na2.png')]
        inventory = load_image('배경\\inventory.png')
        weapon1 = load_image('배경\\weapon1_on.png')
        weapon2 = [load_image('배경\\weapon2_on.png'), load_image('배경\\weapon2_buy.png')]
        weapon3 = [load_image('배경\\weapon3_on.png'), load_image('배경\\weapon3_buy.png')]
        weapon4 = [load_image('배경\\weapon4_on.png'), load_image('배경\\weapon4_buy.png')]
        talk = [load_image('배경\\talk1.png'), load_image('배경\\talk2.png'),
                load_image('배경\\talk3.png'), load_image('배경\\talk4.png')]
        coin = load_image('배경\\coin.png')
        coin_font = load_font('Font\\경기천년바탕_Bold.ttf', 80)

def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 495 <= x <= 855 and 605 <= y <= 670:

                game_framework.change_mode(home_mode)
            elif 833 <= x <= 873 and 540 <= y <= 580:
                if resource.talk != 1:

                    resource.nanahira = 1
                    resource.talk = 1
            elif 1060 <= x <= 1100 and 540 <= y <= 580:
                if resource.talk != 2:

                    resource.nanahira = 1
                    resource.talk = 2
            elif 835 <= x <= 875 and 245 <= y <= 285:
                if resource.talk != 3:

                    resource.nanahira = 1
                    resource.talk = 3
            elif 1060 <= x <= 1100 and 245 <= y <= 285:
                if resource.talk != 4:

                    resource.nanahira = 1
                    resource.talk = 4
