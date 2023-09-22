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

    def add_point(self, index: list, type: PixelType):
        self.state = type
        canvas.itemconfig(self.pixel, fill=GetPixelColourForType(type))


class Pixels:
    button_type = PixelType.OBSTACLE

    def __init__(self, canvas) -> None:
        num_rows = canvas.winfo_reqheight() // PIXEL_SIZE
        num_cols = canvas.winfo_reqwidth() // PIXEL_SIZE

        self.pixels = [
            [PixelElement(canvas, [i, j]) for j in range(num_cols)]
            for i in range(num_rows)
        ]

    def add_point(self, x, y):
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE
        canvas.itemconfig(
            self.pixels[row][col].add_point([row, col], self.button_type),
            fill=GetPixelColourForType(self.button_type),
        )

    def set_button_type(self, type: PixelType):
        print(type)
        self.button_type = type

    def set_free_space(self):
        self.set_button_type(PixelType.FREE_SPACE)

    def set_obstacle(self):
        self.set_button_type(PixelType.OBSTACLE)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("2D world")

    frame = tk.Frame(window)
    frame.pack()

    # Create a canvas widget for drawing
    canvas = tk.Canvas(
        window, width=CANVAS_SIZE_PIXELS, height=CANVAS_SIZE_PIXELS, bg="white"
    )
    canvas.pack()
    pixels = Pixels(canvas)

    def on_canvas_click(event):
        pixels.add_point(event.x, event.y)

    def on_canvas_drag(event):
        pixels.add_point(event.x, event.y)

    obstacle = tk.Button(
        frame,
        text="Obstacle",
        fg="red",
        command=pixels.set_obstacle,
    )
    obstacle.pack(side=tk.LEFT)

    def write_slogan():
        print("Tkinter is easy to use!")

    free_space = tk.Button(frame, text="Free Space", command=pixels.set_free_space)
    free_space.pack(side=tk.LEFT)

    canvas.bind("<Button-1>", on_canvas_click)
    canvas.bind("<B1-Motion>", on_canvas_drag)

    window.mainloop()
