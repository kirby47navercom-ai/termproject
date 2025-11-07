import draw_gesture
import ghost_boss
import ramona


class Stage1_Phase5:
    def __init__(self):
        self.boss = ghost_boss.Boss_Ghost()
        self.monster = []
        self.pattern_num = 0

    def update(self, frame_time, events=None):
        self.boss.update(frame_time, events)
        if self.boss.cutscene:
            self.shape_check()
            self.monster_die()
        else:
            pass

    def shape_check(self):
        if self.boss.shape.name == draw_gesture.result and self.boss.hit_num > 0 and self.boss.pattern_num == 2 and self.boss.hp > 0:
            self.boss.hp -= ramona.Ramona_attack
            self.boss.hit_animation = True
            self.boss.hit_frame = 0
            self.boss.hit_num -= 1
            ramona.Ramona_smash = True

        draw_gesture.result = None

    def monster_die(self):
        if self.boss.die:
            pass

    def draw(self):
        self.boss.draw()