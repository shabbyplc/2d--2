import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None
team = None

def SetState(i):
    for boy in team:
        boy.state=0
    team[i].state =1



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.dir = 1
        if Boy.image == None:
            Boy.image = load_image('run_animation.png')
        self.state = 0;

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += (self.dir * 5)
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1
            self.x =0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global team, grass
    grass = Grass()
    team = [Boy() for i in range(1000)]
    pass


def exit():
    global team, grass
    del(team)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.chage_state(title_state)

    pass


def update():
    for boy in team:
        boy.update()

    pass


def draw():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
        boy.draw()

    update_canvas()
    pass





