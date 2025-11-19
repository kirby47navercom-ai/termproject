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
    font = None
    def __init__(self):
        CACHE_PATH = 'gesture_cache.pkl'
        self.recognizer = QDollarRecognizer()
        if os.path.exists(CACHE_PATH):
            self.recognizer.load_gesture_cache(CACHE_PATH)
        else:
            self.recognizer.load_gesture_from_xml('NewGestures')
            self.recognizer.save_gesture_cache(CACHE_PATH)

        self.font = load_font('Font\\경기천년제목_Bold.ttf', 30)
        self.drawing = False
        self.points = []
        self.stroke_id = 0
        self.result = None
        self.shape = None

        if GestureRecognizer.canvas_image is None:
            GestureRecognizer.canvas_image = load_image('Canvas\\1.png')
        if GestureRecognizer.check_image is None:
            GestureRecognizer.check_image = load_image('Canvas\\2.png')
        self.check_image_x = canvas_size.canvaswidth // 2
        self.check_image_y = canvas_size.canvasheight - (check_image_height * 0.2)
        self.canvas_image_x = canvas_size.canvaswidth // 2
        self.canvas_image_y = canvas_size.canvasheight + canvas_size.canvasheight // 2
        self.go = False

    def update(self, frame_time, events):
        global f_pressed, result
        self.handle_event(events)

        if not f_pressed:
            if self.canvas_image_y > canvas_size.canvasheight // 2:
                self.check_image_y -= SIZE
                self.canvas_image_y -= SIZE
            else:
                self.go = True
        else:
            if self.canvas_image_y < canvas_size.canvasheight + canvas_size.canvasheight // 2:
                self.check_image_y += SIZE
                self.canvas_image_y += SIZE
                self.go = False

        if ramona.Ramona_invincible:
            f_pressed = True
        pass


    def handle_event(self, events):
        global f_pressed, result
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_f:
                    f_pressed = False

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_f:
                    f_pressed = True
                    self.points = []
                    self.result = None
                    self.drawing = False
                    result = None

            if self.go == True:
                if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
                    self.points, self.result, self.drawing = [], None, True
                    self.stroke_id += 1
                    result = None
                elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
                    self.drawing = False
                    if len(self.points) > 10:
                        self.result = self.recognizer.recognize(self.points)
                        if self.result and self.result.score >= 0.2:

                            result = self.result.name
                        else:

                            result = None
                        self.points = []
                elif event.type == SDL_MOUSEMOTION and self.drawing:
                    self.points.append(Point(event.x, event.y, self.stroke_id))

    def draw(self):
        self.check_image.clip_draw(0, 0, check_image_width, check_image_height,
                                   self.check_image_x - canvas_size.camera_x, self.check_image_y - canvas_size.camera_y,
                                   check_image_width * 0.4, check_image_height * 0.4)
        self.canvas_image.draw(self.canvas_image_x - canvas_size.camera_x, self.canvas_image_y - canvas_size.camera_y, )

        if self.go:
            if len(self.points) > 1:
                for i in range(1, len(self.points)):
                    if self.points[i].id == self.points[i - 1].id:
                        draw_line(self.points[i - 1].x - canvas_size.camera_x,
                                  canvas_size.canvasheight - self.points[i - 1].y - canvas_size.camera_y,
                                  self.points[i].x - canvas_size.camera_x,
                                  canvas_size.canvasheight - self.points[i].y - canvas_size.camera_y)

            draw_text_on_screen(10 - canvas_size.camera_x, canvas_size.canvasheight - 90 - canvas_size.camera_y,
                                "그림을 그리고 마우스를 떼세요.", self.font)
            if self.result:
                if self.result.score < 0.25:
                    draw_text_on_screen(10 - canvas_size.camera_x,
                                        canvas_size.canvasheight - 120 - canvas_size.camera_y,
                                        f"인식 결과: 인식 실패 (Score: {self.result.score:.2f})", self.font)
                else:
                    draw_text_on_screen(10 - canvas_size.camera_x,
                                        canvas_size.canvasheight - 120 - canvas_size.camera_y,
                                        f"인식 결과: {self.result.name} (Score: {self.result.score:.2f})", self.font)

