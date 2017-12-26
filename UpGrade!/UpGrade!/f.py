import random

from pico2d import *

class F:

    image = None

    def __init__(self):
        self.x, self.y = random.randint(10, 590), 800
        self.fall_speed = random.randint(90, 180)
        self.cooltime = 3
        self.point = -5
        self.damage = 3
        if F.image == None:
            F.image = load_image('f.png')

    def update(self, frame_time):
        self.y -= frame_time * self.fall_speed

    def draw(self):
        self.image.draw(self.x, self.y)
    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return  self.x - 10, self.y -10, self.x +10, self.y +10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



