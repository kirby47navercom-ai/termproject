from pico2d import *
from canvas_size import *
import ramona

class Ramona_UI:
    def __init__(self):
        self.ramona_hp_image = load_image('playerui\\heart1.png')
        self.ramona_broken_hp_image = load_image('playerui\\heart2.png')
        pass

    def update(self, frame_time, events=None):

        pass

    def draw(self):
        for i in range(ramona.MAX_HP):
            if i < ramona.MAX_HP - ramona.CURRENT_HP:
                self.ramona_broken_hp_image.clip_draw(0, 0, 17, 17, (50 + (ramona.MAX_HP - 1) * 70) - i * 70,
                                                      canvasheight - 50,
                                                      50, 50)
            else:
                self.ramona_hp_image.clip_draw(0, 0, 17, 17, (50 + (ramona.MAX_HP - 1) * 70) - i * 70,
                                               canvasheight - 50,
                                               50, 50)
        pass