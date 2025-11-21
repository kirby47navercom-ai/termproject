from pico2d import *
import ramona
import draw_gesture
import ramona_ui
import canvas_size
import game_framework
import background_3stage
import stage3_monster

def init():
    global player, stage_background, draw_gest, ramona_ui_, stage3_monster_
    stage_background = background_3stage.Background()
    player = ramona.Ramona()
    stage3_monster_ = stage3_monster.Stage3_Monster()
    ramona_ui_ = ramona_ui.Ramona_UI()
    draw_gest = draw_gesture.GestureRecognizer()


def update(frame_time,events):
    pass





def draw():
    pass