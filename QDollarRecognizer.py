import math
import time
import xml.etree.ElementTree as ET
import os
import pickle

class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.int_x = 0
        self.int_y = 0

class PointCloud:
    def __init__(self, name, points):
        self.name = name
        self.points = resample(points, NUM_POINTS)
        self.points = scale(self.points)
        self.points = translate_to(self.points, ORIGIN)
        self.points = make_int_coords(self.points)
        self.lut = compute_lut(self.points)

class Result:
    def __init__(self, name, score, ms):
        self.name = name
        self.score = score
        self.time = ms

NUM_POINT_CLOUDS = 16
NUM_POINTS = 32
ORIGIN = Point(0, 0, 0)
MAX_INT_COORD = 1024
LUT_SIZE = 64
LUT_SCALE_FACTOR = MAX_INT_COORD / LUT_SIZE

def cloud_match(candidate, template, min_so_far):
    n = len(candidate.points)
    step = math.floor(n ** 0.5)

    lb1 = compute_lower_bound(candidate.points, template.points, step, template.lut)
    lb2 = compute_lower_bound(template.points, candidate.points, step, candidate.lut)

    for i, (val1, val2) in enumerate(zip(lb1, lb2)):
        j = i * step
        if val1 < min_so_far:
            min_so_far = min(min_so_far, cloud_distance(candidate.points, template.points, j, min_so_far))
        if val2 < min_so_far:
            min_so_far = min(min_so_far, cloud_distance(template.points, candidate.points, j, min_so_far))

    return min_so_far