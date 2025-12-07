
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

        if not self.die_animation and not self.hit_animation:
            self.move(frame_time)
        elif self.hit_animation and not self.die_animation:
            self.hit_ghost_animation(frame_time)
        elif self.die_animation:
            self.die_ghost_animation(frame_time)

        self.ramonatoghost()
        self.die_ghost()

    def move(self, frame_time):
        distance = math.sqrt((self.x - ramona.Ramona_POS_X) ** 2 + (self.y - ramona.Ramona_POS_Y) ** 2)
        self.x = self.x + (ramona.Ramona_POS_X - self.x) * self.speed * frame_time / distance
        self.y = self.y + (ramona.Ramona_POS_Y - self.y) * self.speed * frame_time / distance

        self.shape.x = self.x
        self.shape.y = self.y + self.height * 0.7

    def ramonatoghost(self):
        if collide([ramona.Ramona_POS_X, ramona.Ramona_POS_Y, ramona.Ramona_SIZE_X, ramona.Ramona_SIZE_Y],
                   [self.x, self.y, self.width,
                    self.height]) and not ramona.Ramona_invincible and not ramona.Ramona_roll_invincible and not self.die_animation:
            if ramona.CURRENT_HP > 0:
                ramona.CURRENT_HP -= 1
                ramona.Ramona_invincible = True
                ramona.invincible_timer = 0.0
                self.die_animation = True
                canvas_size.start_shake(0.5, 5.0)

    def hit_ghost_animation(self, frame_time):
        self.hit_frame = (self.hit_frame + self.hit_animation_speed * frame_time) % 4
        if int(self.hit_frame) == 3:
            if self.hp > 0:
                resource.stage1_effect_sound[0].set_volume(
                    (resource.stage1_effect_sound_offset[0] * resource.effect) // 2)
                resource.stage1_effect_sound[0].play(1)
            self.hit_animation = False
            self.shape = self.pattern_set[randint(0, pattern_number - 5)]
            self.shape.x = self.x
            self.shape.y = self.y + self.height * 0.7
        pass

    def die_ghost(self):
        if self.hp <= 0 and not self.die_animation:
            self.die_animation = True
            self.shape.name = 'No'

    def die_ghost_animation(self, frame_time):
        self.die_frame = (self.die_frame + self.die_animation_speed * frame_time) % 4
        if int(self.die_frame) == 3:
            self.die = True




    def draw(self):
        if not self.die:

            if self.die_animation:
                left, bottom, width, height, jx, jy = ghost_die_coordinate[int(self.die_frame)]
            elif self.hit_animation:
                left, bottom, width, height, jx, jy = ghost_hit_coordinate[int(self.hit_frame)]
            else:
                left, bottom, width, height, jx, jy = ghost_idle_coordinate

            if ramona.Ramona_POS_X < self.x:
                self.image.clip_composite_draw(left, bottom, width, height, 0, '', self.x + jx - canvas_size.shake_x,
                                               self.y + jy - canvas_size.shake_y, width, height)
            else:
                self.image.clip_composite_draw(left, bottom, width, height, 0, 'h', self.x + jx - canvas_size.shake_x,
                                               self.y + jy - canvas_size.shake_y, width, height)

            if canvas_size.collide_check:
                draw_rectangle(self.x - width / 2,
                               self.y - height / 2,
                               self.x + width / 2,
                               self.y + height / 2)

            if not self.die_animation:
                self.shape.draw()

