import background_2stage
from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
import ramona
import resource
import math

SIZE = 1


class Boss_Kitty:
    image = None
    attack1_image = None
    attack2_image = None
    little_image = None
    die_image = None
    def __init__(self):
        pass

    def change_state(self, new_state, event):
        pass

    def update(self, frame_time, events=None):
        pass

    def draw(self):
        pass