from pico2d import *
import canvas_size
import game_framework
import home_mode
import ramona
import resource

black_background = None
clear = None
food = []
perfect = None

def init(): # 로고 이미지를 로드
    global black_background,clear,food,perfect



    if black_background == None:
        black_background = load_image('배경\\black_background.png')
        clear = load_image('배경\\clear.png')
        food = [load_image('배경\\sugar.png'),load_image('배경\\water.png'),
                load_image('배경\\lemon.png')]
        perfect = load_image('배경\\perfect_no.png')


    if resource.boss1:
        if ramona.MAX_HP != ramona.CURRENT_HP:
            if resource.stage1_clear != 2:
                resource.stage1_clear = 1
            if resource.stage1_coin == 0:
                resource.coin += 1
                resource.stage1_coin=1
        else:
            resource.stage1_clear = 2
            if resource.stage1_coin == 0:
                resource.coin += 2
                resource.stage1_coin = 2
            elif resource.stage1_coin == 1:
                resource.coin += 1
                resource.stage1_coin = 2