import game_framework

from pico2d import *
import main
name = "EndState"
image = None
BA_warning = None
font1 = None
font2 = None
point = 0
grade = ''

def enter():
    game_framework.reset_time()
    global image, font1, font2, point,grade,BA_warning
    image = load_image('end_state.png')
    BA_warning = load_image('BA_warning.png')
    font1 = load_font('her_lee.ttf', 30)
    font2 = load_font('her_lee.ttf', 45)
    point = main.player.point

    if point > 500:
        grade = 'A'
    elif point > 400:
        grade = 'B'
    elif point > 300:
        grade = 'C'
    elif point > 200:
        grade = 'D'
    else:
        grade = 'F'

def exit():
    global image, font1,font2
    del (image)
    del (font1)
    del (font2)


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
    image.draw(300, 400)
    font1.draw(200, 700, 'POINT: %d' %point, (0, 0, 0))

    if point < 0:
        BA_warning.draw(300,200)
    else:
        font2.draw(300, 200, '%c' %grade, (255, 0, 0))
    update_canvas()