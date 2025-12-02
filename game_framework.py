import tkinter as tk
import time

import canvas_size
import mouse_image
from pico2d import *
from canvas_size import *
import resource
import ramona
root = tk.Tk()


def change_mode(mode):
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()

    # execute resume function of the previous mode
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False




def ingame(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()
    mouse = mouse_image.Mouse()
    global frame_time
    frame_time = 0.0
    current_time = time.time()
    while running:
        events = get_events()
        mouse.update(frame_time,events)

        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_F1:
                    canvas_size.collide_check = not canvas_size.collide_check
                elif event.key == SDLK_F2:
                    resource.coin = 9999
                elif event.key == SDLK_F3:
                    ramona.Ramona_attack=1000
                elif event.key == SDLK_F4:
                    resource.stage1_clear = 2
                    resource.stage2_clear = 2
                    resource.stage3_clear = 2
                elif event.key == SDLK_ESCAPE:
                    quit()


        stack[-1].update(frame_time,events)
        clear_canvas()
        for mode in stack:
            mode.draw()
        mouse.draw()
        update_canvas()
        frame_time = time.time() - current_time
        current_time += frame_time


    pass
