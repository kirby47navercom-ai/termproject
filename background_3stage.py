from pico2d import *
import canvas_size
import resource
import ramona

start = False
width = 1980

class Background:
    fox_platform = None
    fox_background1 = None
    fox_background2 = None
    fox_background3 = None
    def __init__(self):
        resource.blocks.clear()
        if Background.fox_platform == None:
            Background.fox_platform = load_image('3stage\\Fox Platform.png')
        self.fox_platform_size = (752, 128)

        if Background.fox_background1 == None:
            Background.fox_background1 = load_image('3stage\\Fox BackGround 1.png')

        self.bg_parallax_ratio_x1 = 0.5  # 배경은 x축으로 50% 느리게
        self.bg_parallax_ratio_y1 = 0.2  # 배경은 y축으로 20% 느리게

        if Background.fox_background2 == None:
            Background.fox_background2 = load_image('3stage\\Fox BackGround 2.png')

        self.bg_parallax_ratio_x2 = 0.3
        self.bg_parallax_ratio_y2 = 0.1

        if Background.fox_background3 == None:
            Background.fox_background3 = load_image('3stage\\Fox BackGround 3.png')

        self.bg_parallax_ratio_x3 = 0.15
        self.bg_parallax_ratio_y3 = 0.05

        resource.blocks.append(
            (width // 2, 0, self.fox_platform_size[0] * 1.5 + 80,
             self.fox_platform_size[1] * 3.8))

        self.scroll_x = 0
        self.scroll_y = 0

        self.map_width = width
        self.map_height = 864

    def update(self, frame_time, events=None):
        target_camera_x = ramona.Ramona_POS_X - canvas_size.canvaswidth // 2
        target_camera_y = ramona.Ramona_POS_Y - canvas_size.canvasheight // 2

        canvas_size.scroll_x = clamp(0, target_camera_x, self.map_width - canvas_size.canvaswidth)
        canvas_size.scroll_y = clamp(0, target_camera_y, self.map_height - canvas_size.canvasheight)


def draw(self):
    bg_draw_x = width // 2 - (canvas_size.camera_x * self.bg_parallax_ratio_x3)
    bg_draw_y = 450 - (canvas_size.camera_y * self.bg_parallax_ratio_y3)
    self.fox_background3.clip_draw(0, 0, 800, 480,
                                   bg_draw_x,
                                   bg_draw_y,
                                   800 * 3,
                                   480 * 3)

    bg_draw_x = width // 2 - (canvas_size.camera_x * self.bg_parallax_ratio_x2)
    bg_draw_y = 450 - (canvas_size.camera_y * self.bg_parallax_ratio_y2)
    self.fox_background2.clip_draw(0, 0, 800, 480,
                                   bg_draw_x,
                                   bg_draw_y,
                                   800 * 3,
                                   480 * 3)

    bg_draw_x = width // 2 - (canvas_size.camera_x * self.bg_parallax_ratio_x1)
    bg_draw_y = 450 - (canvas_size.camera_y * self.bg_parallax_ratio_y1)
    self.fox_background1.clip_draw(0, 0, 800, 480,
                                   bg_draw_x,
                                   bg_draw_y,
                                   800 * 2,
                                   480 * 2)

