from pico2d import *
from pattern import *
from resource import *
from random import randint
import canvas_size
import ramona
import math

class Ghost:
    image=None
    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Ghost.image == None:
            Ghost.image = load_image('1stage\\level1-png-sprite.png')
        self.x, self.y = -100, 0
        self.hp = 20
        self.width, self.height = 59, 76
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 50

        self.shape = self.pattern_set[randint(0, pattern_number - 5)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

        self.die = False
        self.die_animation = False
        self.die_animation_speed = 8.0
        self.die_frame = 0
        self.hit = False
        self.hit_animation = False
        self.hit_animation_speed = 8.0
        self.hit_frame = 0
    def update(self, frame_time, events=None):
        pass



    def draw(self):
        if not self.die:

            if self.die_animation:
                left, bottom, width, height, jx, jy = ghost_die_coordinate[int(self.die_frame)]
            elif self.hit_animation:
                left, bottom, width, height, jx, jy = ghost_hit_coordinate[int(self.hit_frame)]
            else:
                left, bottom, width, height, jx, jy = ghost_idle_coordinate

            if ramona.Ramona_POS_X < self.x:
                self.image.clip_composite_draw(left, bottom, width, height, 0, '', self.x + jx - canvas_size.camera_x,
                                               self.y + jy - canvas_size.camera_y, width, height)
            else:
                self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.camera_x,
                                               self.y + jy - canvas_size.camera_y, width, height)

            if not self.die_animation:
                self.shape.draw()

