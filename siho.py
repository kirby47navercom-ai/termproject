from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
import ramona
import resource
import math

SIZE = 1.8


class Boss_Siho:
    def __init__(self):
        self.pattern_set = get_pattern_set()
        self.x, self.y = 1000, 300
        self.boss_hp = 800
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()

    def update(self, frame_time, events=None):
        pass
    def draw(self):
        pass