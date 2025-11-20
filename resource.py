from pico2d import *

ramona_coordinate = [
    (0, 0, 30, 64,0,0),
    (33, 0, 30, 64,0,0),
    (66, 0, 29, 64,0,0),
    (99, 0, 30, 64,0,0),
    (131, 0, 31, 64,0,0),
    (165, 0, 31, 64,0,0),
]
ramona_walk_coordinate = [
    (0, 0, 28, 64,0,0),
    (31, 0, 30, 64,0,0),
    (64, 0, 33, 64,0,0),
    (100, 0, 31, 66,0,0),
    (134, 0, 29, 66,0,0),
    (166, 0, 33, 64,0,0),
]
ramona_run_coordinate =[
    (0, 0, 47, 59,0,0),
    (50, 0, 42, 65,0,0),
    (95, 5, 47, 59,0,0),
    (145, 3, 45, 59,0,0),
    (193, 0, 46, 59,0,0),
    (242, 0, 40, 65,0,0),
    (285, 5, 46, 59,0,0),
    (334, 0, 44, 61,0,0)
]
ramona_jump_coordinate =[
    (1, 0, 41, 51,0,0),
    (45, 12, 36, 65,0,0),
    (84, 14, 41, 61,0,0),
    (128, 18, 44, 58,0,0),
    (175, 20, 45, 53,0,0),
    (223, 18, 46, 56,0,0),
    (272, 14, 47, 62,0,0),
    (322, 7, 45, 69,0,0),
    (370, 0, 42, 52,0,0)
]
ramona_double_jump_coordinate =[
    (0, 0, 44, 44,0,0),
    (47, 5, 45, 34,0,0),
    (95, 0, 33, 46,0,0),
    (131, 5, 42, 39,0,0),
    (176, 5, 37, 47,0,0),
]
ramona_hit_coordinate=[
    (0, 0, 44, 65,0,0),
    (47, 0, 40, 63,0,0),
    (90, 0, 36, 63,0,0),
    (129, 0, 31, 65,0,0),
]
ramona_evade_coordinate =[
    (0, 0, 44, 64,0,0),
    (47, 0, 54, 43,0,0),
    (104, 0, 41, 43,0,0),
    (148, 0, 46, 35,0,0),
    (197, 0, 50, 41,0,0),
    (250, 0, 37, 50,0,0),
    (290, 0, 32, 56,0,0)
]
ramona_getup_coordinate =[
    (0, 0, 68, 32,0,0),
    (71, 0, 68, 32,0,0),
    (142, 2, 47, 40,0,0),
    (192, 2, 47, 42,0,0),
    (242, 3, 55, 68,0,0),
    (300, 28, 57, 43,0,0),
    (360, 8, 45, 69,0,0),
    (408, 3, 42, 52,0,0),
    (453, 3, 31, 65,0,0)
]
ramona_dead_coordinate =[
    (0, 0, 39, 62,0,0),
    (42, 9, 50, 56,0,0),
    (95, 25, 71, 43,0,0),
    (169, 38, 67, 36,0,0),
    (239, 35, 68, 45,0,0),
    (310, 30, 60, 58,0,0),
    (373, 18, 60, 62,0,0),
    (436, 0, 46, 38,0,0),
    (485, 5, 67, 30,0,0),
    (555, 5, 65, 31,0,0),
    (623, 0, 68, 28,0,0),
    (694, 0, 68, 29,0,0),
    (765, 0, 68, 29,0,0)
]
ramona_revive_coordinate =[
    (0, 0, 70, 153,0,0),
    (73, 0, 49, 142,0,0),
    (125, 0, 50, 142,0,0),
    (178, 0, 56, 93,0,0),
    (237, 0, 58, 105,0,0),
    (298, 0, 55, 115,0,0),
    (356, 0, 58, 121,0,0),
    (417, 0, 34, 126,0,0)
]
ramona_stageclear_coordinate =[
    (0, 0, 42, 52,0,0),
    (45, 0, 40, 55,0,0),
    (88, 6, 36, 68,0,0),
    (127, 8, 36, 68,0,0),
    (166, 7, 36, 68,0,0),
    (205, 6, 36, 66,0,0),
    (244, 0, 40, 65,0,0)
]
ramona_gameclear_coordinate =[
    (0, 0, 31, 67,0,0),
    (34, 0, 32, 66,0,0),
    (69, 0, 38, 60,0,0),
    (151, 0, 36, 61,0,0),
    (190, 0, 36, 61,0,0),
    (229, 0, 36, 61,0,0),
    (268, 0, 32, 62,0,0)
]
ramona_action1_coordinate =[
    (0, 0, 55, 63,0,0),
    (58, 0, 38, 82,-5,10),
    (97, 0, 56, 75,-7,9),
    (156, 0, 55, 79,-5,10),
    (214, 0, 77, 82,14,10),
    (294, 0, 69, 58,16,-2),
    (366, 0, 68, 61,16,-2),
    (437, 0, 52, 65,0,0)
]
ramona_action2_coordinate =[
    (0, 0, 52, 60,0,0),
    (55, 0, 75, 49,55,-12),
    (133, 0, 70, 50,55,-10),
    (206, 0, 60, 57,45,-4),
    (269, 0, 50, 62,35,-0)
]
ramona_action3_coordinate =[
    (0, 0, 45, 73, 0, 0),
    (48, 0, 45, 75, 0, 0),
    (96, 0, 46, 76, 0, 0),
    (145, 0, 46, 70, 0, 0),
    (194, 0, 40, 65, 0, 0)
]
ramona_action4_coordinate =[
    (0, 0, 60, 64, 0-30, 0),
    (63, 0, 60, 75, 26-30, 12),
    (126, 0, 38, 75, 30-30, 13),
    (167, 0, 99, 60, 50-30, 0),
    (269, 0, 74, 59, 75-30, -2),
    (346, 0, 73, 60, 75-30, -2),
    (422, 0, 62, 63, 60-30, 0),
    (487, 0, 52, 65, 50-30, 0)
]
ramona_action5_coordinate =[
    (0, 0, 30, 62, 0 ,0),
    (33, 0, 42, 65, 10, 0),
    (78, 0, 45, 66, 10, 0),
    (126, 0, 47, 66, 8, 0),
    (176, 0, 45, 66, 10, 0),
    (224, 0, 81, 63, 50, 0),
    (308, 0, 80, 67, 50, 8),
    (391, 0, 80, 59, 50, 0),
    (474, 0, 84, 59, 50, 0),
    (561, 0, 85, 59, 50, 0),
    (649, 0, 48, 60, 0, 0),
    (700, 0, 38, 62, 0, 0),
    (741, 0, 30, 65, 0, 0)
]
ramona_action6_coordinate =[
    (0, 0, 54, 61, 0, 0),
    (57, 0, 56, 59, 0, 0),
    (116, 0, 90, 51, 70, 0),
    (209, 0, 86, 53, 70, 0),
    (298, 0, 86, 53, 70, 0),
    (387, 0, 86, 53, 70, 0),
    (476, 0, 81, 57, 50, 0),
    (560, 0, 52, 65, 10, 8),
]
ramona_coordinate = {'idle': ramona_coordinate, 'walk': ramona_walk_coordinate, 'run': ramona_run_coordinate,
                     'jump': ramona_jump_coordinate, 'double_jump': ramona_double_jump_coordinate,
                     'hit': ramona_hit_coordinate, 'evade': ramona_evade_coordinate, 'getup': ramona_getup_coordinate,
                     'dead': ramona_dead_coordinate, 'revive': ramona_revive_coordinate, 'stageclear': ramona_stageclear_coordinate,
                     'gameclear': ramona_gameclear_coordinate, 'action1': ramona_action1_coordinate, 'action2': ramona_action2_coordinate,
                     'action3': ramona_action3_coordinate, 'action4': ramona_action4_coordinate, 'action5': ramona_action5_coordinate, 'action6': ramona_action6_coordinate}

image_idle = None
image_walk = None
image_run = None
image_jump = None
image_double_jump = None
image_hit = None
image_evade = None
image_getup = None
image_dead = None
image_revived = None
image_stageclear = None
image_gameclear = None
image_action1 = None
image_action2 = None
image_action3 = None
image_action4 = None
image_action5 = None
image_action6 = None

ramona_image = {}# 비어있는 dict 준비

image_pattern = []
pattern_string_dict = {}
pattern_index_dict = {}

#패턴 리소스 128*128
pattern_name=['가로선','세로선','여우귀','브이','번개','N','별','Z','다이아몬드','네모','세모','검정1','검정2','검정3','검정4','검정5']
pattern_number=15

#보스 체력
boss_hp_coodinate = [0,0,288,16,0,0]

#스테이지 1리소스
ghost_idle_coordinate = [1981,820-265-76,59,76,0,0]
ghost_hit_coordinate = [[1175,820-539-89,101,89,0,0],[1289,820-539-90,100,90,0,0], [1406,820-554-80,100,80,0,0],[1535,820-554-80,62,80,0,0]]
ghost_die_coordinate = [[1143,820-637-81,69,81,0,0],[1242,820-637-81,71,81,0,0],[1349,820-637-81,53,81,0,0]]

boss_ghost_idle_coordinate = [[3313,820-709-104,70,104,0,0],[3385,820-709-104,67,104,0,0],[3457,820-709-106,66,106,0,0],[3529,820-709-104,66,104,0,0]]
boss_ghost_hit_coordinate = [[2115,820-443-105,124,105,0,0],[2252,820-450-102,104,102,0,0], [2402,820-450-97,92,97,0,0]]
boss_ghost_pattern1_coordinate = [[1020,820-670-127,83,127,0,0],[953,820-576-129,62,129,0,0]]
boss_ghost_pattern2_coordinate = [[282,820-689-99,74,99,0,0],[363,820-689-97,74,97,0,0],[444,820-689-97,73,97,0,0],[525,820-689-97,76,97,0,0],[606,820-699-97,77,97,0,0]]
boss_ghost_die_coordinate = [[436,820-566-106,81,106,0,0],[530,820-571-102,82,102,0,0],[629,820-578-108,86,108,0,0],[729,820-581-111,86,111,0,0],[829,820-591-105,86,105,0,0],[1143,820-637-81,69,81,0,0],[1242,820-637-81,71,81,0,0],[1349,820-637-81,53,81,0,0]]

#스테이지 2리소스
boss_kitty_idle_coordinate = [[0,0,362,288,0,0],[0,0,386,299,0,0]]
boss_kitty_die_coordinate = [0,0,288,232,0,0]
boss_kitty_attack_coordinate = [[0,0,27,27,0,0],[0,0,26,26,0,0],[0,0,25,25,0,0],[0,0,25,26,0,0],[0,0,25,27,0,0],[0,0,24,27,0,0],
                                [0,0,27,26,0,0],[0,0,26,24,0,0],[0,0,27,26,0,0],[0,0,27,27,0,0],[0,0,26,26,0,0],[0,0,25,25,0,0],
                                [0,0,25,26,0,0],[0,0,25,27,0,0],[0,0,25,27,0,0],[0,0,25,27,0,0],[0,0,26,26,0,0],[0,0,26,26,0,0],
                                [0,0,25,25,0,0],[0,0,26,26,0,0],[0,0,26,26,0,0],[0,0,27,26,0,0],[0,0,26,26,0,0],[0,0,26,26,0,0],
                                [0,0,25,26,0,0],[0,0,26,26,0,0],[0,0,26,26,0,0],[0,0,26,26,0,0]]
boss_kitty_uibim_coordinate = [[0,0,1280,32,0,0],[0,0,1280,48,0,0],[0,0,1280,288,0,0],[0,0,1280,300,0,0],[0,0,1280,288,0,0],[0,0,1280,48,0,0],[0,0,1280,32,0,0]]
little_kitty_idle_coordinate = [0,0,32,32,0,0]
boss_kitty_attack_image= []
boss_kitty_die_image= []
boss_kitty_uibim_image= []

#스테이지 3리소스
#배경
fox_background_coordinate = [0,0,960,128,0,0]
fox_vine_background_image = []
fox_water_background_image = []
fox_flame_background_image = []

fox_vine_needle_coordinate = [0,0,128,176,0,0]
fox_vine_needle_appear_image = []
fox_vine_needle_disappear_image = []

fox_water_wave_coordinate = [0,0,224,160,0,0]
fox_water_wave_image = []

fox_flame_ball_coordinate = [0,0,64,80,0,0]
fox_flame_ball_image = []

#시호 인간
boss_siho_coordinate = [0,0,64,64,0,0]

boss_siho_appear_image = []

boss_siho_idle_image = []

boss_siho_jump_prepare_image = []
boss_siho_jump_up_image = []
boss_siho_jump_cast_image = []
boss_siho_jump_over_image = []

boss_siho_scratch_prepare_image = []
boss_siho_scratch_cast_image = []
boss_siho_scratch_over_image = []

boss_siho_scratch_rush_prepare_image = []
boss_siho_scratch_rush_cast_image = []
boss_siho_scratch_rush_over_image = []

boss_siho_fire_prepare_image = []
boss_siho_fire_cast_a_image = []
boss_siho_fire_cast_b_image = []
boss_siho_fire_over_image = []

#시호 여우
boss_fox_change_coordinate = [0,0,128,64,0,0]
boss_fox_change_image = []

boss_fox_idle_coordinate = [0,0,96,64,0,0]
boss_fox_idle_image = []

boss_fox_bite_prepare_coordinate = [0,0,96,64,0,0]
boss_fox_bite_prepare_image = []
boss_fox_bite_cast_coordinate = [0,0,128,64,0,0]
boss_fox_bite_cast_image = []
boss_fox_bite_over_coordinate = [0,0,96,64,0,0]
boss_fox_bite_over_image = []

boss_fox_jump_prepare_coordinate = [0,0,96,64,0,0]
boss_fox_jump_prepare_image = []
boss_fox_jump_up_coordinate = [0,0,96,96,0,0]
boss_fox_jump_up_image = []
boss_fox_jump_cast_coordinate = [0,0,96,96,0,0]
boss_fox_jump_cast_image = []
boss_fox_jump_over_coordinate = [0,0,96,64,0,0]
boss_fox_jump_over_image = []

boss_fox_scratch_prepare_coordinate = [0,0,96,64,0,0]
boss_fox_scratch_prepare_image = []
boss_fox_scratch_cast_coordinate = [0,0,96,64,0,0]
boss_fox_scratch_cast_a_image = []
boss_fox_scratch_cast_b_image = []
boss_fox_scratch_over_coordinate = [0,0,96,64,0,0]
boss_fox_scratch_over_image = []

boss_fox_spread_prepare_coordinate = [0,0,96,64,0,0]
boss_fox_spread_prepare_image = []
boss_fox_spread_cast_coordinate = [0,0,96,64,0,0]
boss_fox_spread_cast_image = []
boss_fox_spread_over_coordinate = [0,0,96,64,0,0]
boss_fox_spread_over_image = []

boss_fox_burning_coordinate =  [0,0,96,64,0,0]
boss_fox_burning_a_image = []
boss_fox_burning_b_image = []
boss_fox_burning_c_image = []


#블록
blocks=[]

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a[0] - a[2]/2, a[1] - a[3]/2, a[0] + a[2]/2, a[1] + a[3]/2
    left_b, bottom_b, right_b, top_b = b[0] - b[2]/2, b[1] - b[3]/2, b[0] + b[2]/2, b[1] + b[3]/2

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide2(a, b):
    left_a, bottom_a, right_a, top_a = a[0] - a[2] / 2, a[1] - a[3] / 2, a[0] + a[2] / 2, a[1] + a[3] / 2
    left_b, bottom_b, right_b, top_b = b[0], b[1], b[2], b[3]

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


# 함수로 묶기
def load_resources():
    # 캐릭터
    global image_idle, image_walk, image_run, image_jump, image_double_jump
    global image_hit, image_evade, image_getup, image_dead, image_revived
    global image_stageclear, image_gameclear
    global image_action1, image_action2, image_action3, image_action4, image_action5, image_action6
    global ramona_image, ghost_image
    global image_pattern, pattern_string_dict, pattern_index_dict
    image_idle = load_image('Ramona\\Ramona_idle.png')
    image_walk = load_image('Ramona\\Ramona_walk.png')
    image_run = load_image('Ramona\\Ramona_run.png')
    image_jump = load_image('Ramona\\Ramona_jump.png')
    image_double_jump = load_image('Ramona\\Ramona_double_jump.png')
    image_hit = load_image('Ramona\\Ramona_hit.png')
    image_evade = load_image('Ramona\\Ramona_evade.png')
    image_getup = load_image('Ramona\\Ramona_getup.png')
    image_dead = load_image('Ramona\\Ramona_dead.png')
    image_revived = load_image('Ramona\\Ramona_revived.png')
    image_stageclear = load_image('Ramona\\Ramona_stageclear.png')
    image_gameclear = load_image('Ramona\\Ramona_gameclear.png')
    image_action1 = load_image('Ramona\\Ramona_action1.png')
    image_action2 = load_image('Ramona\\Ramona_action2.png')
    image_action3 = load_image('Ramona\\Ramona_action3.png')
    image_action4 = load_image('Ramona\\Ramona_action4.png')
    image_action5 = load_image('Ramona\\Ramona_action5.png')
    image_action6 = load_image('Ramona\\Ramona_action6.png')

    for i in range(16):
        image_pattern.append(load_image(f'Pattern\\{str(i + 1)}.png'))
        pattern_index_dict[i + 1] = image_pattern[i]
        pattern_string_dict[pattern_name[i]] = i + 1


    for i in range(28):
        boss_kitty_attack_image.append(load_image(f'2stage\\attack_{str(i+1)}.png'))
    for i in range(4):
        boss_kitty_uibim_image.append(load_image(f'2stage\\lightAttack{str(i+1)}.png'))
    for i in range(2,-1,-1):
        boss_kitty_uibim_image.append(load_image(f'2stage\\lightAttack{str(i+1)}.png'))
    for i in range(4):
        boss_kitty_die_image.append(load_image(f'2stage\\blast{str(i+1)}.png'))






    ramona_image = {
        'idle': image_idle, 'walk': image_walk, 'run': image_run, 'jump': image_jump,
        'double_jump': image_double_jump, 'hit': image_hit, 'evade': image_evade,
        'getup': image_getup, 'dead': image_dead, 'revive': image_revived,
        'stageclear': image_stageclear, 'gameclear': image_gameclear, 'action1': image_action1,
        'action2': image_action2, 'action3': image_action3, 'action4': image_action4,
        'action5': image_action5, 'action6': image_action6
    }
























































