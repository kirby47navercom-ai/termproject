from pico2d import *
from canvas_size import *

check_image_width = 825
check_image_height = 216
SIZE=20

class GestureBackground:
    check_image=None
    canvas_image=None
    def __init__(self):
        if GestureBackground.check_image == None:
            GestureBackground.check_image = load_image('Canvas\\2.png')
        if GestureBackground.canvas_image == None:
            GestureBackground.canvas_image = load_image('Canvas\\1.png')
        self.check_image_x = canvaswidth // 2
        self.check_image_y = canvasheight - (check_image_height * 0.2)
        self.canvas_image_x = canvaswidth // 2
        self.canvas_image_y = canvasheight + canvasheight // 2
        self.f_pressed = True
        self.go = False
        pass

    def update(self, frame_time, events):

        pass


    def handle_event(self, events):
        pass


    def draw(self):

        pass