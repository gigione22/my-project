import tkinter as tk
import random

# Constants
WIDTH = 200
HEIGHT = 400
CELL_SIZE = 20
COLUMNS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

# Define shapes and their rotations
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Colors for each shape
COLORS = [
    "cyan", "purple", "green", "red", "yellow", "orange", "blue"
]

class TeatrisGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Teatris Game")
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.bind("<Key>", self.key_pressed)

        self.current_shape = None
        self.current_color = None
        self.current_position = [0, 0]
        self.board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

        self.new_shape()
        self.update()

    def new_shape(self):
        shape_index = random.randint(0, len(SHAPES) - 1)
        self.current_shape = SHAPES[shape_index]
        self.current_color = COLORS[shape_index]
        self.current_position = [0, COLUMNS // 2 - len(self.current_shape[0]) // 2]

    def draw_shape(self):
        shape = self.current_shape
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    x = (self.current_position[1] + j) * CELL_SIZE
                    y = (self.current_position[0] + i) * CELL_SIZE
                    self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=self.current_color, outline="black")

    def key_pressed(self, event):
        if event.keysym == "Left":
            self.move(-1, 0)
        elif event.keysym == "Right":
            self.move(1, 0)
        elif event.keysym == "Down":
            self.move(0, 1)
        elif event.keysym == "Up":
            self.rotate()

    def move(self, dx, dy):
        new_position = [self.current_position[0] + dy, self.current_position[1] + dx]
        if self.valid_position(new_position):
            self.current_position = new_position
            self.update()

    def rotate(self):
        new_shape = list(zip(*self.current_shape[::-1]))
        old_shape = self.current_shape
        self.current_shape = new_shape
        if not self.valid_position(self.current_position):
            self.current_shape = old_shape
        else:
            self.update()

    def valid_position(self, position):
        for i, row in enumerate(self.current_shape):
            for j, cell in enumerate(row):
                if cell:
                    x = position[1] + j
                    y = position[0] + i
                    if x < 0 or x >= COLUMNS or y >= ROWS or self.board[y][x]:
                        return False
        return True

    def update(self):
        self.canvas.delete("all")
        self.draw_shape()
        self.after(500, self.update)

if __name__ == "__main__":
    game = TeatrisGame()
    game.mainloop()
