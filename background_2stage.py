from pico2d import *
import canvas_size
import resource

start=False

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

        self.floor_pos = [(80, 24), (200, 24), (80, 170), (80, 340), (80, 510)]
        self.floor_width = [274, int(48 * 1.5)]
        self.floor_height = [63, int(32 * 1.2)]

        for i in range(3):
            resource.blocks.append((self.floor_pos[i+2][0], self.floor_pos[i+2][1], self.floor_width[1], self.floor_height[1]))

        self.background_num = 0
        self.background_change_time = 0
        self.background_change_timer = 4.0
        self.speed = 100
        self.background_magnification = [1.6, 1.8, 1.0]
        self.scroll_y = 0


    def update(self, frame_time, events=None):
        if self.background_change_time < self.background_change_timer:
            self.background_change_time += frame_time
        if start:
            self.scroll_y += self.speed * frame_time*20

            image_height = self.background_size[2][1] * self.background_magnification[2]

            if self.scroll_y >= image_height:
                self.scroll_y = 0

    def draw(self):
        pass
