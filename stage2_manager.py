from pico2d import *
import ramona
import background_2stage
import draw_gesture
import ramona_ui
import stage2_monster
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

    stage_background = background_2stage.Background()
    ramona.GROUND_LEVEL = 70
    ramona.WIDTH_LEVEL = 320

    ramona_instance = ramona.Ramona()
    monster_instance = stage2_monster.Stage2_Monster()

    ramona_ui_instance = ramona_ui.Ramona_UI()
    draw_gest_instance = draw_gesture.GestureRecognizer()

    game_world.add_object(stage_background, 0)
    game_world.add_object(monster_instance, 1)
    game_world.add_object(ramona_instance, 2)
    game_world.add_object(ramona_ui_instance, 3)
    game_world.add_object(draw_gest_instance, 3)

    background_2stage.start = False

    canvas_size.camera_x = 0
    canvas_size.camera_y = 0
    ramona_instance.x = 50
    ramona_instance.y = ramona.GROUND_LEVEL
    ramona.Ramona_POS_X = ramona_instance.x
    ramona.Ramona_POS_Y = ramona_instance.y

    ramona.Ramona_retry = False
    ramona.Ramona_dead = False


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
    stage_background.draw()
    stage2_monster_.draw()
    player.draw()
    ramona_ui_.draw()
    draw_gest.draw()