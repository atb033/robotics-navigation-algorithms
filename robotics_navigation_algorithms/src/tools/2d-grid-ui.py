# This is a simple UI to make a 2D grid world that could generate an input to the path planners

import tkinter as tk
from tkinter.filedialog import asksaveasfile, askopenfilename
from enum import Enum
import yaml

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


def GetPixelTypeName(type: PixelType):
    if type == PixelType.FREE_SPACE:
        return "free_space"
    elif type == PixelType.START_LOCATION:
        return "start_location"
    elif type == PixelType.GOAL_LOCATION:
        return "goal_location"
    elif type == PixelType.OBSTACLE:
        return "obstacle"


def GetPixelTypeFromName(name: str):
    if name == "free_space":
        return PixelType.FREE_SPACE
    elif name == "start_location":
        return PixelType.START_LOCATION
    elif name == "goal_location":
        return PixelType.GOAL_LOCATION
    elif name == "obstacle":
        return PixelType.OBSTACLE


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
    single_pixel_locations = {PixelType.START_LOCATION: [], PixelType.GOAL_LOCATION: []}

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
        if self.single_pixel_locations[type]:
            old_row, old_col = self.single_pixel_locations[type]
            self.add_point(old_row, old_col, PixelType.FREE_SPACE)
        self.single_pixel_locations[type] = [row, col]
        self.add_point(row, col, type)

    def add_point_from_pixels(self, x, y):
        row = y // PIXEL_SIZE
        col = x // PIXEL_SIZE

        if self.button_type in [PixelType.START_LOCATION, PixelType.GOAL_LOCATION]:
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

    def save_grid_to_file(self):
        data = {GetPixelTypeName(type): [] for type in PixelType}
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                pixel = pixels.pixels[row][col]
                if pixel.state == PixelType.FREE_SPACE:
                    continue
                data[GetPixelTypeName(pixel.state)].append([row, col])

        f = asksaveasfile(
            initialfile="2D-Grid.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
        )
        yaml.dump(data, f)
        print(f"Saving as {f}")

    def load_grid_from_file(self):
        f = askopenfilename()
        print(f"Loading {f}")
        with open(f, "r") as file:
            dic = yaml.safe_load(file)
        pixels.clear_all()
        for key, val in dic.items():
            pixel_type = GetPixelTypeFromName(key)
            for index in val:
                [row, col] = index
                pixels.add_point(row, col, pixel_type)


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
    frame2 = tk.Frame(window)

    # Buttons
    obstacle = tk.Button(
        frame,
        text="Obstacle",
        fg="red",
        command=pixels.set_obstacle,
    )

    free_space = tk.Button(frame, text="Free Space", command=pixels.set_free_space)

    reset = tk.Button(frame2, text="Reset", command=pixels.clear_all)

    start_location = tk.Button(
        frame, text="Start Location", fg="blue", command=pixels.set_start_location
    )

    goal_location = tk.Button(
        frame, text="Goal Location", fg="green", command=pixels.set_goal_location
    )

    save = tk.Button(frame2, text="Save Grid", command=pixels.save_grid_to_file)
    load = tk.Button(frame2, text="Load Grid", command=pixels.load_grid_from_file)

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
    start_location.pack(side=tk.LEFT)
    goal_location.pack(side=tk.LEFT)
    frame2.pack()
    reset.pack(side=tk.LEFT)
    save.pack(side=tk.LEFT)
    load.pack(side=tk.LEFT)
    canvas.pack()

    window.mainloop()
