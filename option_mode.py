from pico2d import *
import canvas_size
import game_framework
import resource

option = None
black_background= None
circle0 = []
circle1 = []

def init():
    global option, circle0, circle1, black_background

    if black_background == None:
        option = load_image('배경\\option.png')
        circle0 = [load_image(f'배경\\circle{str(i + 1)}.png') for i in range(5)]
        circle1 = [load_image(f'배경\\circle{str(i + 6)}.png') for i in range(5)]
        black_background = load_image('배경\\black_background.png')


def update(frame_time,events):
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, canvas_size.canvasheight - 1 - event.y
            if 475 <= x <= 545 and 360 <= y <= 430:

                resource.bgm = 0
            elif 585 <= x <= 655 and 360 <= y <= 430:

                resource.bgm = 1
            elif 705 <= x <= 775 and 360 <= y <= 430:

                resource.bgm = 2
            elif 830 <= x <= 905 and 360 <= y <= 430:

                resource.bgm = 3
            elif 955 <= x <= 1025 and 360 <= y <= 430:

                resource.bgm = 4
            elif 475 <= x <= 545 and 190 <= y <= 260:

                resource.effect = 0
            elif 585 <= x <= 655 and 190 <= y <= 260:

                resource.effect = 1
            elif 705 <= x <= 775 and 190 <= y <= 260:

                resource.effect = 2
            elif 830 <= x <= 905 and 190 <= y <= 260:

                resource.effect = 3
            elif 955 <= x <= 1025 and 190 <= y <= 260:

                resource.effect = 4
            elif 1055 <= x <= 1185 and 515 <= y <= 640:

                game_framework.pop_mode()

def draw():
    black_background.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    option.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    circle0[resource.bgm].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    circle1[resource.effect].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    if canvas_size.collide_check:
        draw_rectangle(475, 360, 545, 430)  # 1
        draw_rectangle(585, 360, 655, 430)  # 2
        draw_rectangle(705, 360, 775, 430)  # 3
        draw_rectangle(830, 360, 905, 430)  # 4
        draw_rectangle(955, 360, 1025, 430)  # 5
        draw_rectangle(475, 190, 545, 260)  # 6
        draw_rectangle(585, 190, 655, 260)  # 7
        draw_rectangle(705, 190, 775, 260)  # 8
        draw_rectangle(830, 190, 905, 260)  # 9
        draw_rectangle(955, 190, 1025, 260)  # 10
        draw_rectangle(1055, 515, 1185, 640)  # 끄기