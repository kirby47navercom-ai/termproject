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

        pass

    pass