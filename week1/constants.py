import random

board = []
player = 'P'
empty = '.'
obstacle = 'X'
for i in range(3):
    row = []
    for j in range(10):
        row.append(empty)
    board.append(row)
no_of_obstacles = random.randint(5, 10)
obstacle_list = []
player_r = 0
player_c = 0