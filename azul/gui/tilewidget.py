import tkinter as tk

from azul.tile import Tile
from azul.tilecolor import TileColor

WIDTH = HEIGHT = 64


class TileWidget(tk.Canvas):
    def __init__(self, master: tk.Misc, tile: Tile = None) -> None:
        super().__init__(master=master, width=WIDTH, height=HEIGHT, background="black")

        background_color: str = "#dfdfdf"

        if tile:
            background_color = _get_background_color(tile.color)

        self.create_rectangle(
            1, 1, 62, 62, fill=background_color, outline="#000000", width=1
        )


def _get_background_color(tilecolor: TileColor) -> str:
    match (tilecolor):
        case TileColor.BLUE:
            return "#007fff"
        case TileColor.YELLLOW:
            return "#ffbf00"
        case TileColor.RED:
            return "#bf1f00"
        case TileColor.BLACK:
            return "#000000"
        case TileColor.WHITE:
            return "#ffffff"
        case _:
            raise RuntimeError("Invalid tile color")
