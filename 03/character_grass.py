from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

move = 10
Wid_x = 800
Wid_y = 600
x = 400
y = 80
loop = False
r = 300
seta = 0
degree = 10
init_xy = (0,0)
turn_UD, turn_RL = False, move
while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    if(init_xy == (400,80)):
        print('A')
        if(loop == False):
            loop = True
        else:
            loop = False
    if(loop == False):
        if Wid_x <= x + turn_RL:
            turn_RL = 0
            turn_UD = move
        elif x + turn_RL < 0:
            turn_RL = 0
            turn_UD = -move
        elif Wid_y <= y + turn_UD:
            turn_UD = 0
            turn_RL = -move
        elif y + turn_UD < 80:
            turn_UD = 0
            turn_RL = move
        x += turn_RL
        y += turn_UD
    else:
        seta += degree
        x = 400 + r * math.cos(seta / 360 * 2 * math.pi)
        y = 80 + r + r * math.sin(seta/ 360 * 2 * math.pi)
        print('x:%d y:%d'%(x,y))
    print('x:%d y:%d /turn_RL:%d turn_UD:%d'%(x,y,turn_RL,turn_UD))
    init_xy = (x,y)
    delay(0.01)
    
    



delay(1)

close_canvas()
