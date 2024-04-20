import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_board(N):
    board = np.random.choice([0, 1], size=(N, N), p=[0.5, 0.5])
    return board

# Function to update the board based on the rules of the Game of Life
def update_board(board):
    new_board = np.zeros(board.shape)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # Count neighbors
            total_neighbors = np.sum(board[max(0, i-1):min(board.shape[0], i+2), max(0, j-1):min(board.shape[1], j+2)]) - board[i, j]

            if board[i, j] == 1:
                if total_neighbors < 2 or total_neighbors > 3:
                    new_board[i, j] = 0
                else:
                    new_board[i, j] = 1
            else:
                if total_neighbors == 3:
                    new_board[i, j] = 1
    return new_board

def update_plot(frameNum, img, board):
    new_board = update_board(board)
    img.set_data(new_board)
    board[:] = new_board[:]
    return img,

fig, ax = plt.subplots()
N = 150
board = initialize_board(N)
img = ax.imshow(board, interpolation='nearest')

ani = animation.FuncAnimation(fig, update_plot, frames=100, fargs=(img, board), interval=100)

import time
time.sleep(2)
plt.show()
