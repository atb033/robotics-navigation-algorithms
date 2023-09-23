import tkinter as tk
from enum import Enum

# Constants
CANVAS_SIZE_PIXELS = 400
PIXEL_SIZE = 10


class PixelType(Enum):
    FREE_SPACE = 0
    OBSTACLE = 1
    START_LOCATION = 2
    GOAL_LOCATION = 3


def GetPixelColourForType(type: PixelType):
    if type == PixelType.FREE_SPACE:
        return "white"
    elif type == PixelType.START_LOCATION:
        return "blue"
    elif type == PixelType.GOAL_LOCATION:
        return "green"
    return "red"


class PixelElement:
    def __init__(self, canvas: tk.Canvas, index: list) -> None:
        [i, j] = index
        self.state = PixelType.FREE_SPACE

        self.pixel = canvas.create_rectangle(
            j * PIXEL_SIZE,
            i * PIXEL_SIZE,
            (j + 1) * PIXEL_SIZE,
            (i + 1) * PIXEL_SIZE,
            outline="gray",
            fill=GetPixelColourForType(self.state),
        )

    def add_point(self, type: PixelType):
        self.state = type
        canvas.itemconfig(self.pixel, fill=GetPixelColourForType(type))


class Pixels:
    button_type = PixelType.OBSTACLE
    current_start_location = []

    def __init__(self, canvas) -> None:
        self.num_rows = canvas.winfo_reqheight() // PIXEL_SIZE
        self.num_cols = canvas.winfo_reqwidth() // PIXEL_SIZE

        self.pixels = [
            [PixelElement(canvas, [i, j]) for j in range(self.num_cols)]
            for i in range(self.num_rows)
        ]

    def add_point(self, row, col, type: PixelType):
        canvas.itemconfig(
            self.pixels[row][col].add_point(type),
            fill=GetPixelColourForType(type),
        )

    def add_single_cell_point(self, row, col, type: PixelType):
        if self.current_start_location:
            old_row, old_col = self.current_start_location
            self.add_point(old_row, old_col, PixelType.FREE_SPACE)
        self.current_start_location = [row, col]
        self.add_point(row, col, PixelType.START_LOCATION)

    def add_point_from_pixels(self, x, y):
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE

        if self.button_type == PixelType.START_LOCATION:
            self.add_single_cell_point(row, col, self.button_type)
        else:
            self.add_point(row, col, self.button_type)

    def set_button_type(self, type: PixelType):
        self.button_type = type

    def set_free_space(self):
        self.set_button_type(PixelType.FREE_SPACE)

    def set_obstacle(self):
        self.set_button_type(PixelType.OBSTACLE)

    def set_start_location(self):
        self.button_type = PixelType.START_LOCATION

    def set_goal_location(self):
        self.button_type = PixelType.GOAL_LOCATION

    def clear_all(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.add_point(i, j, PixelType.FREE_SPACE)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("2D world")

    # Canvas
    canvas = tk.Canvas(
        window, width=CANVAS_SIZE_PIXELS, height=CANVAS_SIZE_PIXELS, bg="white"
    )
    pixels = Pixels(canvas)

    # Frame
    frame = tk.Frame(window)

    # Buttons
    obstacle = tk.Button(
        frame,
        text="Obstacle",
        fg="red",
        command=pixels.set_obstacle,
    )

    free_space = tk.Button(frame, text="Free Space", command=pixels.set_free_space)

    reset = tk.Button(frame, text="Reset", command=pixels.clear_all)

    start_location = tk.Button(
        frame, text="Start Location", fg="blue", command=pixels.set_start_location
    )

    goal_location = tk.Button(
        frame, text="Goal Location", fg="green", command=pixels.set_goal_location
    )

    # Add callbacks
    def on_canvas_click(event):
        pixels.add_point_from_pixels(event.x, event.y)

    def on_canvas_drag(event):
        pixels.add_point_from_pixels(event.x, event.y)

    canvas.bind("<Button-1>", on_canvas_click)
    canvas.bind("<B1-Motion>", on_canvas_drag)

    # Pack everything
    frame.pack()
    obstacle.pack(side=tk.LEFT)
    free_space.pack(side=tk.LEFT)
    reset.pack(side=tk.LEFT)
    start_location.pack(side=tk.LEFT)
    goal_location.pack(side=tk.LEFT)
    canvas.pack()

    window.mainloop()
