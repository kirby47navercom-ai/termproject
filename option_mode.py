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
    pass
