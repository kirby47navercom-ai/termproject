from pico2d import *
import canvas_size

stage1width = 1980
stage1height = 1080

start=False

class Background:
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
        pass

    def draw(self):
        pass