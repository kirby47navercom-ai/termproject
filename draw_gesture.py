from pico2d import *
import os
from QDollarRecognizer import QDollarRecognizer, Point
import canvas_size
import ramona

check_image_width = 825
check_image_height = 216
SIZE=20

BLACK = (0, 0, 0)

f_pressed = True

result = None

def draw_point(x, y):
    draw_rectangle(x, y, x + 1, y + 1)

def draw_line(x1, y1, x2, y2):
