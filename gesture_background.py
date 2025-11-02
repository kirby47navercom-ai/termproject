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
        self.handle_event(events)

        if self.f_pressed == False:
            if self.canvas_image_y > canvasheight // 2:
                self.check_image_y -= SIZE
                self.canvas_image_y -= SIZE
            else:
                self.go = True
        else:
            if self.canvas_image_y < canvasheight + canvasheight // 2:
                self.check_image_y += SIZE
                self.canvas_image_y += SIZE
                self.go = False
        pass


    def handle_event(self, events):
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_f:
                    self.f_pressed=False

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_f:
                    self.f_pressed=True
        pass


    def draw(self):
        self.check_image.clip_draw(0, 0, check_image_width, check_image_height, self.check_image_x, self.check_image_y,
                                   check_image_width * 0.4, check_image_height * 0.4)
        self.canvas_image.draw(self.canvas_image_x, self.canvas_image_y)
        pass