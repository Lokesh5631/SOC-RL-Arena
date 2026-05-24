from constants import *
from utils import *
import time

place_obstacles()
# print(no_of_obstacles)
# print(obstacle_list)
place_player()
display_board()

while True:
    clear_screen()
    display_board()
    print("\nUse W/A/S/D to move")
    key = input().upper()
    old_r, old_c = player_r, player_c
    player_r, player_c = move_player(key, player_r, player_c)
    if player_r not in range(3) or player_c not in range(10):
        print("Invalid move")
        player_r, player_c = old_r, old_c
        time.sleep(2)
        continue
    elif (player_r, player_c) in obstacle_list:
        board[old_r][old_c] = empty
        clear_screen()
        display_board()
        print("Game Over")
        time.sleep(2)
        break
    else:
        board[old_r][old_c] = empty
        board[player_r][player_c] = player

