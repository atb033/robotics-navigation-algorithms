import tkinter as tk
from enum import Enum

# Constants
CANVAS_SIZE_PIXELS = 400
PIXEL_SIZE = 10


class PixelType(Enum):
    FREE_SPACE = 0
    OBSTACLE = 1


def GetPixelColourForType(type: PixelType):
    if type == PixelType.FREE_SPACE:
        return "white"
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

    def __init__(self, canvas) -> None:
        self.num_rows = canvas.winfo_reqheight() // PIXEL_SIZE
        self.num_cols = canvas.winfo_reqwidth() // PIXEL_SIZE

        self.pixels = [
            [PixelElement(canvas, [i, j]) for j in range(self.num_cols)]
            for i in range(self.num_rows)
        ]

    def add_point(self, row, col):
        canvas.itemconfig(
            self.pixels[row][col].add_point(self.button_type),
            fill=GetPixelColourForType(self.button_type),
        )

    def add_point_from_pixels(self, x, y):
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE
        self.add_point(row, col)

    def set_button_type(self, type: PixelType):
        self.button_type = type

    def set_free_space(self):
        self.set_button_type(PixelType.FREE_SPACE)

    def set_obstacle(self):
        self.set_button_type(PixelType.OBSTACLE)

    def clear_all(self):
        old_button_type = self.button_type
        self.button_type = PixelType.FREE_SPACE
        print(self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.add_point(i, j)
        self.button_type = old_button_type


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

    def write_slogan():
        print("Tkinter is easy to use!")

    free_space = tk.Button(frame, text="Free Space", command=pixels.set_free_space)

    reset = tk.Button(frame, text="Reset", command=pixels.clear_all)

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
    canvas.pack()

    window.mainloop()
