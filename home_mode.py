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