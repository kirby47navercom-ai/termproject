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

    resource.background_sound[2].set_volume(
        (resource.background_sound_offset[2] * resource.bgm) // 2)
    resource.background_sound[2].play(-1)

def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 495 <= x <= 855 and 605 <= y <= 670:
                resource.ui_effect_sound[4].set_volume(
                    (resource.ui_effect_sound_offset[4] * resource.effect) // 2)
                resource.ui_effect_sound[4].play(1)
                game_framework.change_mode(home_mode)
            elif 833 <= x <= 873 and 540 <= y <= 580:
                if resource.talk !=1:
                    resource.ui_effect_sound[6].set_volume(
                        (resource.ui_effect_sound_offset[6] * resource.effect) // 2)
                    resource.ui_effect_sound[6].play(1)
                    resource.nanahira = 1
                    resource.talk = 1
            elif 1060 <= x <= 1100 and 540 <= y <= 580:
                if resource.talk != 2:
                    resource.ui_effect_sound[6].set_volume(
                        (resource.ui_effect_sound_offset[6] * resource.effect) // 2)
                    resource.ui_effect_sound[6].play(1)
                    resource.nanahira = 1
                    resource.talk = 2
            elif 835 <= x <= 875 and 245 <= y <= 285:
                if resource.talk != 3:
                    resource.ui_effect_sound[6].set_volume(
                        (resource.ui_effect_sound_offset[6] * resource.effect) // 2)
                    resource.ui_effect_sound[6].play(1)
                    resource.nanahira = 1
                    resource.talk = 3
            elif 1060 <= x <= 1100 and 245 <= y <= 285:
                if resource.talk != 4:
                    resource.ui_effect_sound[6].set_volume(
                        (resource.ui_effect_sound_offset[6] * resource.effect) // 2)
                    resource.ui_effect_sound[6].play(1)
                    resource.nanahira = 1
                    resource.talk = 4
            elif 860 <= x <= 1010 and 318 <= y <= 390:
                if resource.weapon1==0:
                    resource.weapon1 = 1
                    resource.weapon2 = 0 if resource.weapon2!=2 else 2
                    resource.weapon3 = 0 if resource.weapon3!=2 else 2
                    resource.weapon4 = 0 if resource.weapon4!=2 else 2

                    ramona.MAX_HP=3
                    ramona.CURRENT_HP = 3

                    ramona.Ramona_attack = 20

                    resource.pattern_number=15

                    resource.ui_effect_sound[8].set_volume(
                        (resource.ui_effect_sound_offset[8] * resource.effect) // 2)
                    resource.ui_effect_sound[8].play(1)

            elif 1090 <= x <= 1240 and 318 <= y <= 390:
                if resource.weapon2==0:
                    resource.weapon2 = 1
                    resource.weapon1 = 0
                    resource.weapon3 = 0 if resource.weapon3!=2 else 2
                    resource.weapon4 = 0 if resource.weapon4!=2 else 2

                    ramona.MAX_HP = 4
                    ramona.CURRENT_HP = 4

                    ramona.Ramona_attack = 20

                    resource.pattern_number = 15

                    resource.ui_effect_sound[8].set_volume(
                        (resource.ui_effect_sound_offset[8] * resource.effect) // 2)
                    resource.ui_effect_sound[8].play(1)

                elif resource.weapon2==2 and resource.coin>=1:
                    resource.ui_effect_sound[7].set_volume(
                        (resource.ui_effect_sound_offset[7] * resource.effect) // 2)
                    resource.ui_effect_sound[7].play(1)
                    resource.coin-=1
                    resource.weapon2=0

            elif 860 <= x <= 1010 and 28 <= y <= 100:
                if resource.weapon3==0:
                    resource.weapon3 = 1
                    resource.weapon1 = 0
                    resource.weapon2 = 0 if resource.weapon2!=2 else 2
                    resource.weapon4 = 0 if resource.weapon4!=2 else 2

                    ramona.MAX_HP = 3
                    ramona.CURRENT_HP = 3

                    ramona.Ramona_attack = 30

                    resource.pattern_number = 15

                    resource.ui_effect_sound[8].set_volume(
                        (resource.ui_effect_sound_offset[8] * resource.effect) // 2)
                    resource.ui_effect_sound[8].play(1)

                elif resource.weapon3==2 and resource.coin>=2:
                    resource.ui_effect_sound[7].set_volume(
                        (resource.ui_effect_sound_offset[7] * resource.effect) // 2)
                    resource.ui_effect_sound[7].play(1)
                    resource.coin-=2
                    resource.weapon3=0
            elif 1090 <= x <= 1240 and 28 <= y <= 100:
                if resource.weapon4==0:
                    resource.weapon4 = 1
                    resource.weapon1 = 0
                    resource.weapon2 = 0 if resource.weapon2!=2 else 2
                    resource.weapon3 = 0 if resource.weapon3!=2 else 2

                    ramona.MAX_HP = 3
                    ramona.CURRENT_HP = 3

                    ramona.Ramona_attack = 20

                    resource.pattern_number = 10

                elif resource.weapon4==2 and resource.coin>=3:
                    resource.ui_effect_sound[7].set_volume(
                        (resource.ui_effect_sound_offset[7] * resource.effect) // 2)
                    resource.ui_effect_sound[7].play(1)
                    resource.coin-=3
                    resource.weapon4=0
            else:
                resource.nanahira = 0
                resource.talk = 0

def draw():
    background.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.nanahira == 1:
        nanahira[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    else:
        nanahira[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    inventory.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.weapon1 == 1:
        weapon1.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.weapon2 == 2:
        weapon2[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.weapon2 == 1:
        weapon2[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.weapon3 == 2:
        weapon3[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.weapon3 == 1:
        weapon3[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.weapon4 == 2:
        weapon4[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.weapon4 == 1:
        weapon4[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.talk == 1:
        talk[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.talk == 2:
        talk[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.talk == 3:
        talk[2].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.talk == 4:
        talk[3].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    coin.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    coin_font.draw(80, canvas_size.canvasheight - 40, 'X ' + str(resource.coin), (0, 0, 0))
    if canvas_size.collide_check:
        draw_rectangle(495, 605, 855, 670)  # 집

        draw_rectangle(833, 540, 873, 580)  # 망치 1 ?

        draw_rectangle(1060, 540, 1100, 580)  # 망치 2 ?

        draw_rectangle(835, 245, 875, 285)  # 망치 3 ?

        draw_rectangle(1060, 245, 1100, 285)  # 망치 4 ?

        draw_rectangle(860, 318, 1010, 390)  # 망치 1 고르기

        draw_rectangle(1090, 318, 1240, 390)  # 망치 2 고르기

        draw_rectangle(860, 28, 1010, 100)  # 망치 3 고르기

        draw_rectangle(1090, 28, 1240, 100)  # 망치 4 고르기

def finish():

    pass

def pause():
    pass
def resume():
    pass