The main.py file should be opnened from the system terminal, as opening from VSCode causes errors in screen clearing.

# constants.py
Has some basic constant values which are imported in utils.py and main.py
# utils.py
This contains the functions which are used in the main program.
## clear_screen()
I have used this to clear the terminal so that the game board gets displayed freshly after each move, and not one after the other
## place_obstacles()
I had tried to implement a random obstacle selection method using random module, so that every time the user opens the game, the obstacles are positioned differently. Also the number of obstacles can also vary from 5 to 10.   
And to make the movement of the player possible I had tried to remove obstacles placed diagonally to each other as it might block the user from moving through the entire board.
## move_player()
This is what changes the position of the player
# main.py
This contains the main game flow.  
Every time the enter key is pressed, the terminal is cleared and the new board is displayed.
First the player starts at (0,0). The player enters a W/A/S/D and the position of the player moves accordingly leaving a dot at its previous position.  
Going outside the box is detected by going out of range of the row and column indices. If the new player position is present in the obstacle_list, then the game gets over.    
  
There are still much more edge cases for placing the obstacles like three obstacles are placed along the same column the user gets stuck on one side of the board. But since there can be more such cases, I have not included them. If any such situation occurs, the game can b erestarted until a proper board is given.
