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

    ramona.GROUND_LEVEL = 70
    ramona.WIDTH_LEVEL = 320

    player.x = 50
    player.y = ramona.GROUND_LEVEL
    ramona.Ramona_POS_X = player.x
    ramona.Ramona_POS_Y = player.y

    background_2stage.start = False


def update(frame_time,events):
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_

def draw():
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_