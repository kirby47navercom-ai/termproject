from pico2d import *
import canvas_size
import game_framework
import resource

ending_image = None
black_background=None
current_image = 0
alpha = 0
FADE_SPEED = 10  # 알파값 증가 속도

def init():
    global ending_image, current_image, alpha,black_background
    if ending_image is None:
        ending_image = resource.end_image
        black_background = load_image('배경\\black_background.png')
    current_image = 0
    alpha = 0
    resource.background_sound[1].stop()
    resource.background_sound[9].set_volume(
        (resource.background_sound_offset[9] * resource.effect) // 2)
    resource.background_sound[9].play(-1)

def update(frame_time, events):
    global current_image, alpha

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if alpha < 255:
                alpha = 255  # 현재 이미지 바로 다 보이게

            else:
                if current_image < 6:
                    current_image += 1
                    alpha = 0

                else:

                    game_framework.pop_mode()

    if alpha < 255:
        alpha += FADE_SPEED*frame_time*60
        if alpha > 255:
            alpha = 255

def draw():
    global ending_image, current_image, alpha,black_background

    black_background.draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)

    for i in range(current_image):
        ending_image[i].opacify(1.0)
        ending_image[i].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)
    ending_image[current_image].opacify(alpha / 255.0)
    ending_image[current_image].draw(canvas_size.canvaswidth // 2, canvas_size.canvasheight // 2)



def finish():
    pass

def pause():
    pass

def resume():
    pass




