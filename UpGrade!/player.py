import random

from pico2d import *

class Player:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 30.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    font = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 4, 9, 2, 7

    def __init__(self):
        self.x, self.y = 295, 77
        self.frame = random.randint(0, 9)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.point = 0
        self.hp = 100
        self.state = self.RIGHT_STAND
        if Player.image == None:
            Player.image = load_image('player_sprite.png')
        if Player.font == None:
            Player.font = load_font('her_lee.ttf',16)

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        self.hp -= 1*frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 11
        self.x += (self.dir * distance)

        self.x = clamp(0, self.x, 600)

    def draw(self):
        self.image.clip_draw(self.frame * 50, self.state * 50, 50, 50, self.x, self.y)


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw_UI(self):
        self.font.draw(78, 770, 'HP: %d' % self.hp, (255, 0, 0))
        self.font.draw(25, 740, 'TIME: %d' % self.life_time, (0, 0, 0))
        self.font.draw(280, 770, 'POINT: %d' % self.point, (0, 0, 255))
        draw_rectangle(5,755,(self.hp*2)+5,785)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir = 0





