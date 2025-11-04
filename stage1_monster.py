import stage1_phase1
import stage1_phase2
import stage1_phase3
import stage1_phase4
import stage1_phase5





class Stage1_Monster:
    def __init__(self):
        self.phase_num = 0
        self.phase = []
        self.phase.append(stage1_phase1.Stage1_Phase1())
        self.phase.append(stage1_phase2.Stage1_Phase2())
        self.phase.append(stage1_phase3.Stage1_Phase3())
        self.phase.append(stage1_phase4.Stage1_Phase4())
        self.phase.append(stage1_phase5.Stage1_Phase5())


    def update(self, frame_time, events=None):
        self.phase[self.phase_num].update(frame_time, events)

        if self.phase_num == 4:
            pass
        elif self.phase[self.phase_num].phase.__len__() == 0:
            self.phase_num += 1
            self.update(frame_time, events)

    def draw(self):
        self.phase[self.phase_num].draw()