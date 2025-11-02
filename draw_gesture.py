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
    dx, dy = x2 - x1, y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        draw_point(x1, y1)
        return
    x_inc, y_inc = dx / steps, dy / steps
    x, y = x1, y1
    for i in range(int(steps) + 1):
        draw_point(int(x), int(y))
        x += x_inc
        y += y_inc

def draw_text_on_screen(x, y, text,font):
    font.draw(x, y, text, BLACK)

class GestureRecognizer:
    check_image = None
    canvas_image = None
    def __init__(self):
        CACHE_PATH = 'gesture_cache.pkl'
        self.recognizer = QDollarRecognizer()

    def update(self, frame_time, events):
        pass

    def handle_event(self, events):
        pass

    def draw(self):
        pass