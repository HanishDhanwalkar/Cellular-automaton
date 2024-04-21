import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class DrawingApp:
    def __init__(self, N):
        self.board = np.zeros(shape=(N, N))
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Click on the canvas to draw')
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def on_click(self, event):
        if event.button == 1:  # Left-click to draw
            x, y = event.xdata, event.ydata
            if x is not None and y is not None:
                print(f"Clicked at: ({x:.2f}, {y:.2f})")
                x = abs(int(x))
                _y = abs(int(y))
                self.board[_y,x] = 1
                self.ax.plot(x, y, 'ro')  
                self.fig.canvas.draw_idle()


# Function to update the board based on the rules of the Game of Life
def update_board(board):
    new_board = np.zeros(board.shape)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
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

if __name__ == "__main__":
    N = 15
    drawing_app = DrawingApp(N)
    
    plt.xlim(0, N)
    plt.ylim(-N, 0)
    plt.show()

    fig, ax = plt.subplots()
    board = drawing_app.board
    img = ax.imshow(board, interpolation='nearest')

    ani = animation.FuncAnimation(fig, update_plot, frames=100, fargs=(img, board), interval=100)

    plt.show()
