import random

from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(300,400)

    def draw_bb(self):
        draw_rectangle(5,755,205,785)

