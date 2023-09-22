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
    return "black"


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
    def __init__(self, canvas) -> None:
        num_rows = canvas.winfo_reqheight() // PIXEL_SIZE
        num_cols = canvas.winfo_reqwidth() // PIXEL_SIZE

        self.pixels = [
            [PixelElement(canvas, [i, j]) for j in range(num_cols)]
            for i in range(num_rows)
        ]

    def add_point(self, x, y, type: PixelType):
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE
        canvas.itemconfig(
            self.pixels[row][col].add_point([row, col], type),
            fill=GetPixelColourForType(type),
        )


if __name__ == "__main__":
    window = tk.Tk()
    window.title("2D world")

    # Create a canvas widget for drawing
    canvas = tk.Canvas(
        window, width=CANVAS_SIZE_PIXELS, height=CANVAS_SIZE_PIXELS, bg="white"
    )
    canvas.pack()
    pixels = Pixels(canvas)

    def on_canvas_click(event):
        pixels.add_point(event.x, event.y, PixelType.OBSTACLE)

    def on_canvas_drag(event):
        pixels.add_point(event.x, event.y, PixelType.OBSTACLE)

    canvas.bind("<Button-1>", on_canvas_click)
    canvas.bind("<B1-Motion>", on_canvas_drag)

    window.mainloop()
