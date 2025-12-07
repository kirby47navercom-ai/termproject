import draw_gesture
import background_2stage
import hellkitty
import ramona
import resource


class Stage2_Monster:
    def __init__(self):
        self.boss = hellkitty.Boss_Kitty()
        self.game_start = False
        resource.background_sound[5].set_volume(
            (resource.background_sound_offset[5] * resource.bgm) // 2)
        resource.background_sound[5].play(-1)

    def update(self, frame_time, events=None):
        if '하트' == draw_gesture.result:
            background_2stage.start = True
            draw_gesture.result = None
            self.boss.attack_start = True
        elif background_2stage.start:
            self.boss.update(frame_time, events)
            self.shape_check()
            self.monster_die()

    def shape_check(self):
        if self.boss.shape.name == draw_gesture.result and self.boss.hp>0:
            self.boss.hp -= ramona.Ramona_attack
            ramona.Ramona_smash = True
            self.boss.hit_animation=True
            if self.boss.hp <= 0:
                self.boss.hp = 0
                self.boss.die_animation=True

        draw_gesture.result = None

    def monster_die(self):
        if self.boss.die:
            pass

    def draw(self):
        if background_2stage.start:
            self.boss.draw()