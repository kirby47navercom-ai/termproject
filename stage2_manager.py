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

    canvas_size.camera_x = 0
    canvas_size.camera_y = 0

    ramona.Ramona_retry = False


def update(frame_time,events):
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_
    if not ramona.Ramona_dead:
        stage_background.update(frame_time, events)
        stage2_monster_.update(frame_time, events)
        ramona_ui_.update(frame_time, events)
        draw_gest.update(frame_time, events)
    elif ramona.Ramona_retry:
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_r:
                ramona.Ramona_dead = False
                ramona.CURRENT_HP = ramona.MAX_HP
                ramona.Ramona_POS_X = 50
                ramona.Ramona_POS_Y = ramona.GROUND_LEVEL
                init()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_F1:
                canvas_size.collide_check= not canvas_size.collide_check
        elif event.key == SDLK_ESCAPE:
            game_framework.quit()

        player.update(frame_time, events)

        if canvas_size.shake_timer > 0:
            canvas_size.update_shake(frame_time)


def draw():
    global player,stage_background,draw_gest,ramona_ui_,stage2_monster_