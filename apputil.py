import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt

def update_board(current_board):
    """
    Execute one step of Conway's Game of Life.
    
    Parameters
    ----------
    current_board : numpy.ndarray
        Binary array (0 = dead, 1 = alive).
    
    Returns
    -------
    updated_board : numpy.ndarray
        Next state of the board after applying Conway's rules.
    """
    # Pad the board with zeros to handle edges
    padded = np.pad(current_board, pad_width=1, mode='constant', constant_values=0)
    
    # Prepare an empty board for the next state
    updated_board = np.zeros_like(current_board)
    
    # Iterate through each cell
    for i in range(current_board.shape[0]):
        for j in range(current_board.shape[1]):
            # Count neighbors (sum of surrounding 8 cells)
            neighbors = np.sum(padded[i:i+3, j:j+3]) - padded[i+1, j+1]
            
            # Apply Conway's rules
            if padded[i+1, j+1] == 1:  # Cell is alive
                if neighbors == 2 or neighbors == 3:
                    updated_board[i, j] = 1
            else:  # Cell is dead
                if neighbors == 3:
                    updated_board[i, j] = 1
    
    return updated_board

def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)