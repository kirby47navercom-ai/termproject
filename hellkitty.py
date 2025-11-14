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

class IdleState:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass

class Pattern0_State:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self, frame_time):
        pass

    def draw(self):
        pass

class Pattern1_State:
    pass

class Pattern2_State:
    pass

class Pattern3_State:
    pass

class DieState:
    pass



class Boss_Kitty:
    image = None
    attack1_image = None
    attack2_image = None
    little_image = None
    die_image = None
    def __init__(self):
        self.pattern_set = get_pattern_set()
        if Boss_Kitty.image == None:
            Boss_Kitty.image = [load_image('2stage\\boss1.png'), load_image('2stage\\boss2.png')]
        if Boss_Kitty.die_image == None:
            Boss_Kitty.die_image = resource.boss_kitty_die_image
        if Boss_Kitty.attack1_image == None:
            Boss_Kitty.attack1_image = resource.boss_kitty_attack_image
        if Boss_Kitty.attack2_image == None:
            Boss_Kitty.attack2_image = resource.boss_kitty_uibim_image
        if Boss_Kitty.little_image == None:
            Boss_Kitty.little_image = load_image('2stage\\157.png')

        self.x, self.y = canvas_size.canvaswidth - 300, canvas_size.canvasheight // 2
        self.boss_hp = 240
        self.hp = self.boss_hp
        self.hp_bar = Boss_HP()
        self.width, self.height = 386 * SIZE, 299 * SIZE
        self.frame = 0
        self.dir = 1
        self.timer = 0.0
        self.speed = 300
        self.shape = self.pattern_set[randint(0, pattern_number)]
        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.2
        self.idle_frame = 0
        self.animation_speed = 4.0

        # 상태 전환 관련 변수
        self.attack_start = False
        self.attack_init = False


        self.hit = False
        self.hit_animation = False
        self.hit_time = 0.0
        self.die = False
        self.die_animation = False
        self.die_animation_speed = 2.0
        self.die_frame = 0

    def change_state(self, new_state, event):
        pass

    def update(self, frame_time, events=None):
        pass

    def draw(self):
        pass