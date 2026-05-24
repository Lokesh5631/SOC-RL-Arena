from constants import *

def clear_screen():
    import os
    import platform
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        

def display_board():
    for row in board:
        print(' '.join(row))

def place_player():
    board[0][0] = player

def place_obstacles():
    import random
    while len(obstacle_list) < no_of_obstacles:
        r = random.randint(0,2)
        c = random.randint(0,9)
        prohibited = [(0,0)]
        if obstacle_list != []:
            for (orow, ocol) in obstacle_list:
                prohibited.extend([(orow-1,ocol-1), (orow-1,ocol+1), (orow+1,ocol+1), (orow+1,ocol-1)])
        if (r,c) in prohibited or (r,c) in obstacle_list:
            continue
        else:
            board[r][c] = obstacle
            obstacle_list.append((r,c))

def move_player(key, player_r, player_c):
    if key == "W":
        player_r -= 1
    elif key == "A":
        player_c -= 1
    elif key == "S":
        player_r +=1
    elif key == "D":
        player_c +=1
    return player_r, player_c


    

