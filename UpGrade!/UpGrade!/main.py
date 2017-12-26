import game_framework
import title_state
import end_state
from a import A
from b import B
from c import C
from d import D
from f import F
from game import GAME
from pico2d import *
from player import Player
from background import Ground

name = "main"

player = None
grades = None
ground = None

a_ct,b_ct,c_ct,d_ct,f_ct,g_ct = 0,1,1,2,0,3

def create_world():
    global player,grades,ground
    player = Player()
    grades = []
    ground = Ground()

def destroy_world():
    global player,ground,grades
    del (player)
    del (ground)
    del (grades)

def enter():
    game_framework.reset_time()
    create_world()

def exit():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            else:
                player.handle_event(event)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return  False
    if bottom_a > top_b: return  False

    return True

def spawn_item(frame_time,a,b,c,d,f,g):
    global a_ct, b_ct, c_ct, d_ct, f_ct,g_ct
    a_ct += frame_time *1.25
    b_ct += frame_time*1.25
    c_ct += frame_time*1.25
    d_ct += frame_time*1.25
    f_ct += frame_time*1.25
    g_ct += frame_time*1.25
    if a_ct > a:
        grades.append(A())
        grades.append(GAME())
        a_ct = 0
    if b_ct > b:
        grades.append(B())
        grades.append(GAME())
        b_ct = 0
    if c_ct > c:
        grades.append(C())
        grades.append(GAME())
        c_ct = 0
    if d_ct > d:
        grades.append(D())
        grades.append(GAME())
        d_ct = 0
    if f_ct > f:
        grades.append(F())
        grades.append(GAME())
        f_ct = 0
    if g_ct > f:
        grades.append(GAME())
        g_ct = 0


def update(frame_time):

    player.update(frame_time)

    if player.hp < 0:
        end_state.point = player.point
        game_framework.change_state(end_state)


    if player.life_time < 20:
        spawn_item(frame_time,7,5,3,3,5,3)
    elif player.life_time > 20:
        spawn_item(frame_time, 7, 7, 2, 2, 3,2)
    elif player.life_time > 30:
        spawn_item(frame_time, 7, 7, 2, 2, 2,1)


    for grade in grades:
        grade.update(frame_time)
        if collide(player,grade):
            grades.remove(grade)
            player.pick(grade)


def draw(frame_time):
    clear_canvas()
    ground.draw()
    player.draw()
    player.draw_UI()

    for grade in grades:
        grade.draw()

    update_canvas()

