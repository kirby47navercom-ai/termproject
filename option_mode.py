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