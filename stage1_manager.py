from pico2d import *
import ramona
import background_1stage
import draw_gesture
import ramona_ui
import stage1_monster
import canvas_size
import game_framework
import game_world
import stage_clear_mode
import resource
import stage_fail_mode

ramona_instance = None
monster_instance = None

def init():
    global ramona_instance, monster_instance
    game_world.clear()

    canvas_size.start_shake(0, 0)

    stage_background = background_1stage.Background()
    ramona.GROUND_LEVEL = 100
    ramona.WIDTH_LEVEL = canvas_size.canvaswidth - 25

    ramona_instance = ramona.Ramona()
    monster_instance = stage1_monster.Stage1_Monster()

    ramona_ui_instance = ramona_ui.Ramona_UI()
    draw_gest_instance = draw_gesture.GestureRecognizer()

    game_world.add_object(stage_background, 0)
    game_world.add_object(monster_instance, 1)
    game_world.add_object(ramona_instance, 2)
    game_world.add_object(ramona_ui_instance, 3)
    game_world.add_object(draw_gest_instance, 3)

    canvas_size.camera_x = 0
    canvas_size.camera_y = 0
    ramona_instance.x = canvas_size.canvaswidth // 2
    ramona_instance.y = ramona.GROUND_LEVEL
    ramona.Ramona_POS_X = ramona_instance.x
    ramona.Ramona_POS_Y = ramona_instance.y

    ramona.Ramona_retry = False
    ramona.Ramona_dead = False


def update(frame_time,events):
    if not ramona.Ramona_dead:
        game_world.update(frame_time, events)
    elif ramona.Ramona_retry:
        resource.boss1 = True
        ramona.Ramona_dead = False
        ramona.CURRENT_HP = ramona.MAX_HP
        game_framework.push_mode(stage_fail_mode)

    if ramona.Ramona_dead:
        if ramona_instance:
            ramona_instance.update(frame_time, events)

    if resource.boss1 and not ramona.Ramona_retry:
        game_framework.push_mode(stage_clear_mode)

    if canvas_size.shake_timer > 0:
        canvas_size.update_shake(frame_time)





def draw():
    game_world.render()

def finish():
    game_world.clear()

def pause(): pass

def resume(): pass
