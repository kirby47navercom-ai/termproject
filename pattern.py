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

class Width(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[0]
        self.name = '가로선'
class Height(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[1]
        self.name = '세로선'
class FoxEar(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[2]
        self.name = '여우귀'
class Victory(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[3]
        self.name = '브이'
class Thunder(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[4]
        self.name = '번개'
class Night(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[5]
        self.name = 'N'
class Star(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[6]
        self.name = '별'
class Zzz(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[7]
        self.name = 'Z'
class diamond(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[8]
        self.name = '다이아몬드'
class square(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[9]
        self.name = '네모'
class triangle(Pattern):
    def __init__(self):
        super().__init__()
        self.image = image_pattern[10]
        self.name = '세모'