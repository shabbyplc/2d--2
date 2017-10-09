import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

npc = None
space = None
font = None
team = None

def SetState(i):
    for npc in team:
        npc.state=0
    team[i].state =1



class Space:
    def __init__(self):
        self.image = load_image('space2.jpg')

    def draw(self):
        self.image.draw(0,0)



class Npc:
    def __init__(self):
        self.x, self.y = random.randint(10, 70), random.randint(10, 70)
        self.frame = random.randint(0, 7)
        self.image = load_image('npc.png')
        self.state = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 0.1

    def draw(self):
        self.image.clip_draw(self.frame * 10, 0, 10, 10, self.x, self.y)



def enter():
    global team, space
    space = Space()
    team = [Npc() for i in range(10)]
    pass


def exit():
    global team, space
    del(team)
    del(space)
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
       # elif event.type == SDL_MOUSEMOTION:
           

    pass


def update():
    for npc in team:
        npc.update()

    pass


def draw():
    clear_canvas()
    space.draw()
    for npc in team:
        npc.update()
        npc.draw()

    update_canvas()
    pass





