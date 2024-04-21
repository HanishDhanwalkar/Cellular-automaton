import matplotlib.pyplot as plt

class DrawingApp:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Click on the canvas to draw')
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def on_click(self, event):
        if event.button == 1:  # Left-click to draw
            x, y = event.xdata, event.ydata
            if x is not None and y is not None:
                print(f"Clicked at: ({x:.2f}, {y:.2f})")
                self.ax.plot(x, y, 'ro')  # Plot a red point
                self.fig.canvas.draw_idle()

if __name__ == "__main__":
    drawing_app = DrawingApp()
    N = 100
    plt.xlim(0, N)
    plt.ylim(0, N)
    plt.show()
