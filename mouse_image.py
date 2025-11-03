from pico2d import *
import draw_gesture
width, height = 128, 128

class Mouse:
    def __init__(self):
        self.normal = load_image('Mouse\\1.png')
        self.paint = load_image('Mouse\\2.png')
        self.x = 0
        self.y = 0

    def update(self, frame_time,events):
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.x, self.y = event.x, get_canvas_height() - 1 - event.y

    def draw(self):
        if draw_gesture.f_pressed == False:
            self.paint.clip_draw(0, 0, 128, 128, self.x + 30, self.y - 30,
                                 width * 0.5, height * 0.5)
        else:
            self.normal.clip_draw(0, 0, 128, 128, self.x + 30, self.y - 30,
                                  width * 0.5, height * 0.5)