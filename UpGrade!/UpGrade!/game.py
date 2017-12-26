import random

from pico2d import *

class GAME:

    image = None

    def __init__(self):
        self.x, self.y = random.randint(10, 590), 800
        self.fall_speed = random.randint(70, 150)
        self.point = -10
        self.damage = 10
        if GAME.image == None:
            GAME.image = load_image('game.png')

    def update(self, frame_time):
        self.y -= frame_time * self.fall_speed

    def draw(self):
        self.image.draw(self.x, self.y)
    def stop(self):
        self.fall_speed = 0

    def get_bb(self):
        return  self.x - 15, self.y -15, self.x +15, self.y +15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())



