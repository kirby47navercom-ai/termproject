from pico2d import *
import canvas_size
import resource
import ramona

start = False
width = 1980

class Background:
    fox_platform = None
    fox_background1 = None
    fox_background2 = None
    fox_background3 = None
    def __init__(self):
        resource.blocks.clear()
        if Background.fox_platform == None:
            Background.fox_platform = load_image('3stage\\Fox Platform.png')
        self.fox_platform_size = (752, 128)

    def update(self, frame_time, events=None):
        pass
    def draw(self):
        pass