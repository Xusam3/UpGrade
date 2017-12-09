import game_framework

from pico2d import *
import main

name = "EndState"
image = None

def enter():
    open_canvas(600,800)
    global image
    image = load_image('end_state.png')

def exit():
    global image
    del (image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main)

def update(frame_time):
    pass

def draw(frame_time):
    clear_canvas()
    image.draw(300,400)
    update_canvas()