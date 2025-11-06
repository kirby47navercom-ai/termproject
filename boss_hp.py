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
            0, 0, boss_hp_coodinate[2], boss_hp_coodinate[3],  # 원본 클리핑 영역 (변경 없음)
            canvas_size.canvaswidth // 2 - (boss_hp_coodinate[2] * 4.3 * (1 - boss_hp_persentage)) / 2,  # X좌표 보정
            20,  # Y좌표
            boss_hp_coodinate[2] * 4.3 * boss_hp_persentage,  # 화면 너비
            boss_hp_coodinate[3]  # 화면 높이 (배율 적용)
        )