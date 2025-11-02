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

def cloud_distance(pts1, pts2, start, min_so_far):
    n = len(pts1)
    unmatched = list(range(n))

    i = start
    weight = n
    sum_dist = 0.0

    while True:
        u = -1
        b = float('inf')
        for j_idx, j in enumerate(unmatched):
            d = sqr_euclidean_distance(pts1[i], pts2[j])
            if d < b:
                b = d
                u = j_idx

        unmatched.pop(u)
        sum_dist += weight * b

        if sum_dist >= min_so_far:
            return sum_dist

        weight -= 1
        i = (i + 1) % n
        if i == start:
            break

    return sum_dist


def compute_lower_bound(pts1, pts2, step, lut):
    n = len(pts1)
    lb = [0.0] * (math.floor(n / step) + 1)
    sat = [0.0] * n

    for i in range(n):
        x = round(pts1[i].int_x / LUT_SCALE_FACTOR)
        y = round(pts1[i].int_y / LUT_SCALE_FACTOR)
        index = lut[x][y]
        d = sqr_euclidean_distance(pts1[i], pts2[index])
        sat[i] = d if i == 0 else sat[i - 1] + d
        lb[0] += (n - i) * d

    for i in range(step, n, step):
        j = i // step
        lb[j] = lb[0] + i * sat[n - 1] - n * sat[i - 1]

    return lb

def resample(points, n):
    I = path_length(points) / (n - 1)
    D = 0.0
    new_points = [points[0]]

    i = 1
    while i < len(points):
        if points[i].id == points[i - 1].id:
            d = euclidean_distance(points[i - 1], points[i])
            if (D + d) >= I:
                qx = points[i - 1].x + ((I - D) / d) * (points[i].x - points[i - 1].x)
                qy = points[i - 1].y + ((I - D) / d) * (points[i].y - points[i - 1].y)
                q = Point(qx, qy, points[i].id)
                new_points.append(q)
                points.insert(i, q)
                D = 0.0
            else:
                D += d
        i += 1

    if len(new_points) == n - 1:
        last_point = points[-1]
        new_points.append(Point(last_point.x, last_point.y, last_point.id))

    return new_points

def scale(points):
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')

    for p in points:
        min_x = min(min_x, p.x)
        min_y = min(min_y, p.y)
        max_x = max(max_x, p.x)
        max_y = max(max_y, p.y)

    size = max(max_x - min_x, max_y - min_y)
    new_points = []
    for p in points:
        qx = (p.x - min_x) / size
        qy = (p.y - min_y) / size
        new_points.append(Point(qx, qy, p.id))

    return new_points

def translate_to(points, pt):
    c = centroid(points)
    new_points = []
    for p in points:
        qx = p.x + pt.x - c.x
        qy = p.y + pt.y - c.y
        new_points.append(Point(qx, qy, p.id))

    return new_points

def centroid(points):
    x_sum, y_sum = 0.0, 0.0
    for p in points:
        x_sum += p.x
        y_sum += p.y

    return Point(x_sum / len(points), y_sum / len(points), 0)

def path_length(points):
    d = 0.0
    for i in range(1, len(points)):
        if points[i].id == points[i - 1].id:
            d += euclidean_distance(points[i - 1], points[i])
    return d

def make_int_coords(points):
    for p in points:
        p.int_x = round((p.x + 1.0) / 2.0 * (MAX_INT_COORD - 1))
        p.int_y = round((p.y + 1.0) / 2.0 * (MAX_INT_COORD - 1))
    return points

def compute_lut(points):
    lut = [[0 for _ in range(LUT_SIZE)] for _ in range(LUT_SIZE)]

    for x in range(LUT_SIZE):
        for y in range(LUT_SIZE):
            u = -1
            b = float('inf')
            for i, p in enumerate(points):
                row = round(p.int_x / LUT_SCALE_FACTOR)
                col = round(p.int_y / LUT_SCALE_FACTOR)
                d = ((row - x) ** 2) + ((col - y) ** 2)
                if d < b:
                    b = d
                    u = i
            lut[x][y] = u

    return lut

def sqr_euclidean_distance(pt1, pt2):
    dx = pt2.x - pt1.x
    dy = pt2.y - pt1.y
    return dx * dx + dy * dy

def euclidean_distance(pt1, pt2):
    return math.sqrt(sqr_euclidean_distance(pt1, pt2))


class QDollarRecognizer:
    def __init__(self):
        self.point_clouds = []
        self.point_clouds.append(PointCloud("없어용", [
            Point(382, 310, 1), Point(377, 308, 1), Point(373, 307, 1), Point(366, 307, 1), Point(360, 310, 1),
            Point(356, 313, 1), Point(353, 316, 1), Point(349, 321, 1), Point(347, 326, 1), Point(344, 331, 1),
            Point(342, 337, 1), Point(341, 343, 1), Point(341, 350, 1), Point(341, 358, 1), Point(342, 362, 1),
            Point(344, 366, 1), Point(347, 370, 1), Point(351, 374, 1), Point(356, 379, 1), Point(361, 382, 1),
            Point(368, 385, 1), Point(374, 387, 1), Point(381, 387, 1), Point(390, 387, 1), Point(397, 385, 1),
            Point(404, 382, 1), Point(408, 378, 1), Point(412, 373, 1), Point(416, 367, 1), Point(418, 361, 1),
            Point(419, 353, 1), Point(418, 346, 1), Point(417, 341, 1), Point(416, 336, 1), Point(413, 331, 1),
            Point(410, 326, 1), Point(404, 320, 1), Point(400, 317, 1), Point(393, 313, 1), Point(392, 312, 1),
            Point(418, 309, 2), Point(337, 390, 2)
        ]))

    def save_gesture_cache(self, cache_path):
        with open(cache_path, 'wb') as f:
            pickle.dump(self.point_clouds, f)

    def load_gesture_cache(self, cache_path):
        with open(cache_path, 'rb') as f:
            self.point_clouds = pickle.load(f)

    def recognize(self, points):
        t0 = time.time()
        candidate = PointCloud("", points)

        u = -1
        b = float('inf')

        for i, template in enumerate(self.point_clouds):
            d = cloud_match(candidate, template, b)
            if d < b:
                b = d
                u = i

        t1 = time.time()

        if u == -1:
            return Result("No match.", 0.0, (t1 - t0) * 1000)
        else:
            score = 1.0 / b if b > 1.0 else 1.0
            return Result(self.point_clouds[u].name, score, (t1 - t0) * 1000)

    def add_gesture(self, name, points):