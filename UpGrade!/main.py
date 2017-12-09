import game_framework
import title_state
import end_state
from a import A
from b import B
from c import C
from d import D
from f import F
from pico2d import *
from player import Player
from background import Ground

name = "main"

player = None
grades = None
ground = None

a_ct,b_ct,c_ct,d_ct,f_ct = 0,0,0,0,0

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
    destroy_world()
    close_canvas()

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

def update(frame_time):
    global a_ct,b_ct,c_ct,d_ct,f_ct
    a_ct += frame_time
    b_ct += frame_time
    c_ct += frame_time
    d_ct += frame_time
    f_ct += frame_time
    player.update(frame_time)

   # if player.hp < 0:

    if a_ct > 7:
        grades.append(A())
        a_ct = 0
    if b_ct > 5:
        grades.append(B())
        b_ct = 0
    if c_ct > 3:
        grades.append(C())
        c_ct = 0
    if d_ct > 3:
        grades.append(D())
        d_ct = 0
    if f_ct > 5:
        grades.append(F())
        f_ct = 0




    for grade in grades:
        grade.update(frame_time)
        if collide(player,grade):
            grades.remove(grade)
            player.hp-= grade.damage
            player.point+=grade.point

def draw(frame_time):
    clear_canvas()
    ground.draw()
    player.draw()
    player.draw_bb()
    player.draw_UI()

    for grade in grades:
        grade.draw()


    update_canvas()

