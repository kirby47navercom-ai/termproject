from pico2d import *
import canvas_size

stage1width = 1980
stage1height = 1080

start=False

class Background:
    background = None
    def __init__(self):
        if Background.background == None:
            Background.background = [load_image('1stage\\1.png'), load_image('1stage\\2.png'),
                                     load_image('1stage\\3.png'),
                                     load_image('1stage\\4.png'), load_image('1stage\\5.png'),
                                     load_image('1stage\\6.png'),
                                     load_image('1stage\\7.png'), load_image('1stage\\8.png'), ]
        self.x = [0, 0, 0, 0]
        self.speed = 300

    def update(self, frame_time, events=None):
        for i in range(self.x.__len__()):
            self.x[i] += self.speed * frame_time * (i + 1) * 0.2
            if self.x[i] >= stage1width * 0.7:
                self.x[i] = 0

    def draw(self):
        for i in range(self.background.__len__()):
            if i == 2 or i == 3 or i == 4:
                self.background[i].clip_draw(0, 0, stage1width, stage1height,
                                             canvas_size.canvaswidth // 2 + self.x[i - 2] - (
                                                         stage1width * 0.7) - canvas_size.camera_x,
                                             canvas_size.canvasheight // 2 - canvas_size.camera_y, stage1width * 0.7,
                                             stage1height * 0.7)
                self.background[i].clip_draw(0, 0, stage1width, stage1height,
                                             canvas_size.canvaswidth // 2 + self.x[i - 2] - canvas_size.camera_x,
                                             canvas_size.canvasheight // 2 - canvas_size.camera_y, stage1width * 0.7,
                                             stage1height * 0.7)
            else:
                self.background[i].clip_draw(0, 0, stage1width, stage1height,
                                             canvas_size.canvaswidth // 2 - canvas_size.camera_x,
                                             canvas_size.canvasheight // 2 - canvas_size.camera_y, stage1width * 0.7,
                                             stage1height * 0.7)