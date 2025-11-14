from pico2d import *
import ramona
import background_2stage
import draw_gesture
import ramona_ui
import stage2_monster
import canvas_size
import game_framework

def init():
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_
    stage_background = background_2stage.Background()
    player = ramona.Ramona()
    stage2_monster_ = stage2_monster.Stage2_Monster()
    ramona_ui_ = ramona_ui.Ramona_UI()
    draw_gest = draw_gesture.GestureRecognizer()


def update(frame_time,events):
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_

def draw():
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_