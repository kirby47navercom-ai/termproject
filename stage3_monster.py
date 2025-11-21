import draw_gesture
import stage3_topography
import ramona
import resource

class Stage3_Monster:
    def __init__(self):
        self.floor = stage3_topography.Stage3_Terrain()

    def update(self, frame_time, events=None):
        self.floor.update(frame_time, events)

    def draw(self):
        self.floor.draw()

