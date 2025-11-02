from pico2d import *

import canvas_size
from canvas_size import *
from resource import *

class Pattern:
    def __init__(self):
        self.width = 128
        self.height = 128
        self.x = None
        self.y = None
        self.image = None
        self.name = None

    def draw(self,sizex=0.2,sizey=0.2):
        self.image.clip_draw(0, 0, 128, 128,self.x-canvas_size.camera_x, self.y-canvas_size.camera_y, self.width*sizex, self.height*sizey)

