import random
from pico2d import*

def SetState(i):
    for boy in team:
        boy.state=0
    team[i].state = 1

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame =random.randint(0,7)
        self.image =load_image('run_animation.png')
        self.state =0;

    def update(self):
        self.frame=(self.frame+1)%8
        self.x +=2

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type ==SDL_MOUSEMOTION:
             for boy in team:
                if boy.state == 1:
                    boy.x,boy.y = event.x, 600-event.y
        elif event.type ==SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and SDLK_1:
            SetState(0)
        elif event.type == SDL_KEYDOWN and SDLK_2:
            SetState(1)
        elif event.type == SDL_KEYDOWN and SDLK_2:
            SetState(2)

open_canvas()
team = [Boy() for i in range(11)]


boy = Boy()
grass = Grass()

running = True;



while (running):
    handle_events()
    clear_canvas()
    for boy in team:
        boy.update()


    grass.draw()
    for boy in team:
        boy.draw()

    update_canvas()

    delay (0.05)

close_canvas()

