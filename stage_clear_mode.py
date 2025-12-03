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
    elif resource.boss2:
        if ramona.MAX_HP != ramona.CURRENT_HP:
            if resource.stage2_clear != 2:
                resource.stage2_clear = 1
            if resource.stage2_coin == 0:
                resource.coin += 1
                resource.stage2_coin = 1
        else:
            resource.stage2_clear = 2
            if resource.stage2_coin == 0:
                resource.coin += 2
                resource.stage2_coin = 2
            elif resource.stage2_coin == 1:
                resource.coin += 1
                resource.stage2_coin = 2
    elif resource.boss3:
        if ramona.MAX_HP != ramona.CURRENT_HP:
            if resource.stage3_clear != 2:
                resource.stage3_clear = 1
            if resource.stage3_coin == 0:
                resource.coin += 1
                resource.stage3_coin = 1
        else:
            resource.stage3_clear = 2
            if resource.stage3_coin == 0:
                resource.coin += 2
                resource.stage3_coin = 2
            elif resource.stage3_coin == 1:
                resource.coin += 1
                resource.stage3_coin = 2

def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 478 <= x <= 584 and 67 <= y <= 175:
                if resource.boss1:
                    resource.boss1 = False
                elif resource.boss2:
                    resource.boss2 = False
                elif resource.boss3:
                    resource.boss3 = False

                game_framework.pop_mode()
                game_framework.change_mode(home_mode)
        elif 678 <= x <= 784 and 67 <= y <= 175:
            import stage1_manager
            import stage2_manager
            import stage3_manager
            if resource.boss1:
                resource.boss1 = False
                game_framework.pop_mode()

                game_framework.change_mode(stage1_manager)
            elif resource.boss2:
                resource.boss2 = False
                game_framework.pop_mode()

                game_framework.change_mode(stage2_manager)
            elif resource.boss3:
                resource.boss3 = False
                game_framework.pop_mode()

                game_framework.change_mode(stage3_manager)

def draw():
    if black_background:
        black_background.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)


    if clear:
        clear.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if resource.boss1:
        food[0].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.boss2:
        food[1].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    elif resource.boss3:
        food[2].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if ramona.MAX_HP != ramona.CURRENT_HP:
        perfect.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if canvas_size.collide_check:
        draw_rectangle(478, 67, 584, 175)

        draw_rectangle(678, 67, 784, 175)