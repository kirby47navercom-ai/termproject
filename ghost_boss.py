from boss_hp import Boss_HP
from pattern import *
from resource import *
from random import randint
import canvas_size
import ramona


SIZE = 1.2

class DieState:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass

class Boss_Ghost:
    image = None

    def __init__(self):
        pass


    def update(self, frame_time, events=None):
        pass

    def draw(self):
        pass