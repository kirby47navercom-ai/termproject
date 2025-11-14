import draw_gesture
import background_2stage
import hellkitty
import ramona


class Stage2_Monster:
    def __init__(self):
        self.boss = hellkitty.Boss_Kitty()

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


    def draw(self):
        pass