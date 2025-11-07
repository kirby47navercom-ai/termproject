import canvas_size
from resource import *


class Boss_HP:
    bar = None
    image = None

    def __init__(self):
        if Boss_HP.bar == None:
            Boss_HP.bar = load_image('bossui\\EnemyHealthBar.png')
        if Boss_HP.image == None:
            Boss_HP.image = load_image('bossui\\Enemy Health Frame.png')


    def update(self, frame_time, events=None):

        pass

    def draw(self,boss_now_hp=240, boss_max_hp=240):
        boss_hp_persentage = boss_now_hp / boss_max_hp

        self.image.clip_draw(0, 0, 512, 16, canvas_size.canvaswidth // 2, 20, boss_hp_coodinate[2] * 4.5,
                             boss_hp_coodinate[3])
        self.bar.clip_draw(
            0, 0, boss_hp_coodinate[2], boss_hp_coodinate[3],
            canvas_size.canvaswidth // 2 - (boss_hp_coodinate[2] * 4.3 * (1 - boss_hp_persentage)) / 2,
            20,
            boss_hp_coodinate[2] * 4.3 * boss_hp_persentage,
            boss_hp_coodinate[3]
        )