from pico2d import *
import canvas_size
import resource

class Background:
    background = None
    floor1 = None
    floor2 = None
    def __init__(self):
        resource.blocks.clear()
        if Background.background == None:
            Background.background =  [load_image('2stage\\1.png'), load_image('2stage\\2.png'),
                               load_image('2stage\\3.png')]

        self.background_size = [(872, 479), (726, 574), (1280 * 1.5, 2048 * 1.5)]

        if Background.floor1 == None:
            Background.floor1 = load_image('2stage\\floor_1.png')

        if Background.floor2 == None:
            Background.floor2 = load_image('2stage\\floor_2.png')

    def update(self, frame_time, events=None):
        pass

    def draw(self):
        pass
