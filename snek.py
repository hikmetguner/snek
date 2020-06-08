l1 = ' _______    _          _______    _        '
l2 = '(  ____ \  ( (    /|  (  ____ \  | \    /\ '
l3 = '| (    \/  |  \  ( |  | (    \/  |  \  / / '
l4 = '| (_____   |   \ | |  | (__      |  (_/ /  '
l5 = '(_____  )  | (\ \) |  |  __)     |   _ (   '
l6 = '      ) |  | | \   |  | (        |  ( \ \  '
l7 = '/\____) |  | )  \  |  | (____/\  |  /  \ \ '
l8 = '\_______)  |/    )_)  (_______/  |_/    \/ '

g1='   _________    __  _________   ____ _    ____________  '
g2='  / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \ '
g3=' / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ / '
g4='/ /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/  '
g5='\____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|   '

import os,keyboard,copy,random
from time import sleep

def game_over(score):
    for _ in range(3):
        for i in range(3,59):
            game_ov[(i,4)] = ' '
            game_ov[(i,5)] = ' '
            game_ov[(i,6)] = ' '
            game_ov[(i,7)] = ' '
            game_ov[(i,8)] = ' '
        printer(game_ov)
        sleep(0.2)
        for i in range(3,59):
            game_ov[(i,4)] = g1[i-3]
            game_ov[(i,5)] = g2[i-3]
            game_ov[(i,6)] = g3[i-3]
            game_ov[(i,7)] = g4[i-3]
            game_ov[(i,8)] = g5[i-3]
        printer(game_ov)
        sleep(0.2)
    sleep(0.1)
    printer(game_ov)
    for i in range(3,59):
        game_ov[(i,4)] = g1[i-3]
        game_ov[(i,5)] = g2[i-3]
        game_ov[(i,6)] = g3[i-3]
        game_ov[(i,7)] = g4[i-3]
        game_ov[(i,8)] = g5[i-3]
    for i,j in zip(range(24,32),'Score = '):
        game_ov[i,14] = j
    for i,j in zip(range(len(str(score))),str(score)):
        game_ov[32+i,14] = j
    for i,j in zip(range(24,29),'Retry'):
        game_ov[i,18] = j
    for i,j in zip(range(24,29),'Quit'):
        game_ov[i,22] = j
    arrow_coor = (23,18)
    while True:
        game_ov[arrow_coor] = '>'
        if keyboard.is_pressed('down arrow'):
            game_ov[arrow_coor] = ' '
            arrow_coor = (23,22)
        elif keyboard.is_pressed('up arrow'):
            game_ov[arrow_coor] = ' '
            arrow_coor = (23,18)
        elif keyboard.is_pressed('enter') and arrow_coor == (23,22):
            os.system('mode con: cols=1 lines=1')
            quit()
        elif keyboard.is_pressed('enter') and arrow_coor == (23,18):
            os.system('cls')
            main(True)
        printer(game_ov)
    exit()
def key_get(obj):
    return [key for key in game_dict.keys() if game_dict[key] == obj][0]
def move(coor,direction):
    global score
    global path
    if coor == head or path == []:
        c,l = coor
        x,y = movement_dict[direction]
        if game_dict[(c+x,l+y)] == '#' or game_dict[(c+x,l+y)] == 'O':
            game_over(score)
        else:
            temp.append((c+x,l+y))
            path.append((c,l))
    else:
        c,l = coor
        a = path[char_arr.index(coor)-1]
        temp.append(a)
        path.append((c,l))
def food(coor):
    global char_arr,score
    if coor == head or path == []:
        c,l = coor
        x,y = movement_dict[direction]
        if game_dict[(c+x,l+y)] == 'X':
            game_dict[(c+x,l+y)] == 'O'
            char_arr = [(c+x,l+y)] + char_arr
            score += 500
def food_spawn():
    coor = (random.randint(1,59),random.randint(1,29))
    if game_dict[coor] != 'O' and game_dict[coor] != '#':
        game_dict[coor] = 'X'
def move_input():
    global direction
    if keyboard.is_pressed('up arrow') and direction != 'down':
        direction = 'up'
    elif keyboard.is_pressed('down arrow')and direction != 'up':
        direction = 'down'
    elif keyboard.is_pressed('left arrow') and direction != 'right':
        direction = 'left'
    elif keyboard.is_pressed('right arrow') and direction != 'left':
        direction = 'right'
    return direction
def normalizer(lst):
    temp = []
    for i in lst:
        for j in i:
            temp.append(j)
    return temp
def printer(dicc):
    for i in dicc.keys():
        if i != list(dicc.keys())[-1]:
            print(dicc[i],end='')
        else:
            print(dicc[i],end='\r')
if __name__ == '__main__':
    os.system('title Snek')
    def main(skip=False):
        global game_dict,head,temp,path,char_arr,game_ov,direction,movement_dict,score,cols,lines
        movement_dict = {
        'up':(0,-1),
        'down':(0,1),
        'left':(-1,0),
        'right':(1,0),
        }
        cols,lines = 60,30
        direction = 'up'
        score = 0
        os.system('mode con: cols=60 lines=30')
        game_table = [[(col,line) for col in range(cols)] for line in range(lines)]
        game_blank = [' ' for i in range(cols*lines)]
        game_dict = dict(zip(normalizer(game_table),game_blank))
        for i in range(cols):
            game_dict[(i,0)] = '#'
            game_dict[(0,i//2)] = '#'
            game_dict[(59,i//2)] = '#'
            game_dict[(i,29)] = '#'
        main_menu = copy.deepcopy(game_dict)
        game_ov = copy.deepcopy(game_dict)
        for i in range(9,51):
            main_menu[(i,4)] = l1[i-9]
            main_menu[(i,5)] = l2[i-9]
            main_menu[(i,6)] = l3[i-9]
            main_menu[(i,7)] = l4[i-9]
            main_menu[(i,8)] = l5[i-9]
            main_menu[(i,9)] = l6[i-9]
            main_menu[(i,10)] = l7[i-9]
            main_menu[(i,11)] = l8[i-9]
        if skip:
            pass
        else:
            for i in range(3):
                printer(game_dict)
                sleep(0.2)
                printer(main_menu)
                sleep(0.2)
            main_menu[(24,18)] = 'P'
            main_menu[(25,18)] = 'l'
            main_menu[(26,18)] = 'a'
            main_menu[(27,18)] = 'y'
            main_menu[(24,22)] = 'Q'
            main_menu[(25,22)] = 'u'
            main_menu[(26,22)] = 'i'
            main_menu[(27,22)] = 't'

            arrow_coor = (23,18)

            while True:
                main_menu[arrow_coor] = '>'
                if keyboard.is_pressed('down arrow'):
                    main_menu[arrow_coor] = ' '
                    arrow_coor = (23,22)
                elif keyboard.is_pressed('up arrow'):
                    main_menu[arrow_coor] = ' '
                    arrow_coor = (23,18)
                elif keyboard.is_pressed('enter') and arrow_coor == (23,22):
                    quit()
                    os.close()
                elif keyboard.is_pressed('enter') and arrow_coor == (23,18):
                    break
                printer(main_menu)
        game_dict[(30,15)] = 'O'
        game_dict[(30,16)] = 'O'
        game_dict[(30,17)] = 'O'
        game_dict[(30,18)] = 'O'
        game_dict[(30,19)] = 'O'
        char_arr = [(30,15),(30,16),(30,17),(30,18),(30,19)]
        turn = 0
        while True:
            direction = move_input()
            head = char_arr[0]
            if turn % 60 == 0:
                food_spawn()
            if turn % 3 == 0:
                path = list()
                temp = list()
                path_t = list()
                food(head)
                for i in char_arr:
                    move(i,direction)
                for i,j in zip(temp,path):
                    game_dict[i] = 'O'
                    game_dict[j] = ' '
                char_arr = temp
            printer(game_dict)
            turn += 1
            sleep(0.01)
    main()
