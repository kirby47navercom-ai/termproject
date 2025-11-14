from pico2d import *
import mouse_image
import stage1_manager
import stage2_manager

def init():
    global mouse
    #stage1_manager.init()
    stage2_manager.init()
    mouse = mouse_image.Mouse()

def update(frame_time):
    global mouse
    events = get_events()
    #stage1_manager.update(frame_time, events)
    stage2_manager.update(frame_time, events)
    mouse.update(frame_time,events)

def draw():
    global mouse
    clear_canvas()
    #stage1_manager.draw()
    stage2_manager.draw()
    mouse.draw()
    update_canvas()
