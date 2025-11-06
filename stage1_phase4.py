from ghost_normal import *
import draw_gesture
import random

ghost_phase_far=50
ghost_phase_pos=[-1,1,-1,1,-1,1,-1,1,-1,1]

class Stage1_Phase4:
    def __init__(self):
        self.phase=[Ghost() for _ in range(ghost_phase_pos.__len__())]
        for i in range(self.phase.__len__()):
            self.phase[i].x=0 if ghost_phase_pos[i] == -1 else canvaswidth+ghost_phase_pos[i]*ghost_phase_far
            self.phase[i].y=random.randint(0,canvasheight)
            self.phase[i].speed=150



        pass
    def update(self, frame_time, events=None):
        self.phase[self.phase.__len__()-1].update(frame_time,events)

        self.shape_check()
        self.monster_die()


    def shape_check(self):
        if self.phase[self.phase.__len__()-1].shape.name==draw_gesture.result:
            self.phase[self.phase.__len__()-1].hp-=ramona.Ramona_attack
            self.phase[self.phase.__len__()-1].hit_animation=True
            self.phase[self.phase.__len__()-1].hit_frame = 0
            ramona.Ramona_smash = True

        draw_gesture.result=None

        pass
    def monster_die(self):
        if self.phase[self.phase.__len__()-1].die:
            self.phase.pop(self.phase.__len__()-1)

    def draw(self):
        self.phase[self.phase.__len__()-1].draw()
