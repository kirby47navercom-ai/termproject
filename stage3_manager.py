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

    canvas_size.start_shake(0, 0)

    ramona.GROUND_LEVEL = 25
    ramona.WIDTH_LEVEL = background_3stage.width - 25

    player.x = canvas_size.canvaswidth // 2
    player.y = 260
    ramona.Ramona_POS_X = player.x
    ramona.Ramona_POS_Y = player.y

    canvas_size.camera_x = 0
    canvas_size.camera_y = 0
    ramona.Ramona_retry = False
    ramona.Ramona_dead = False


def update(frame_time,events):
    pass





def draw():
    pass