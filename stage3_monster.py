import draw_gesture
import stage3_topography
import siho
import ramona
from random import randint
import resource

class Stage3_Monster:
    def __init__(self):
        self.phase_num=0
        self.phase=[]
        self.boss=siho.Boss_Siho()
        self.floor = stage3_topography.Stage3_Terrain()
        resource.background_sound[8].set_volume(
            (resource.background_sound_offset[8] * resource.bgm) // 2)
        resource.background_sound[8].play(-1)





    def update(self, frame_time, events=None):
        self.boss.update(frame_time, events)

        if self.boss.appear_animation and self.boss.pattern_num!=14:
            self.floor.update(frame_time, events)
            self.shape_check()

            if self.boss.change_graphycs:
                self.floor.current_pattern+=1
                self.boss.change_graphycs=False
        self.monster_die()

    def shape_check(self):
        if self.boss.shape.name == draw_gesture.result and self.boss.hp>0:
            self.boss.hp -= ramona.Ramona_attack
            ramona.Ramona_smash = True
            self.boss.hit_animation=True

        draw_gesture.result = None

        pass

    def monster_die(self):
        if self.boss.die:
            resource.boss3 = True




    def draw(self):
        if self.boss.appear_animation:
            self.floor.draw()
        self.boss.draw()




