import tkinter as tk
import time

root = tk.Tk()

def ingame(game_manager):
    global running
    running = True

    game_manager.init()

    global frame_time
    frame_time = 0.0
    current_time = time.time()
    while running:
        game_manager.update(frame_time)
        game_manager.render()
        frame_time = time.time() - current_time
        current_time += frame_time
        pass

    pass