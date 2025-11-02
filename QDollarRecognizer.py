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

