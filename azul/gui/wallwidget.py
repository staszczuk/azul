import tkinter as tk
import ttkbootstrap as ttk

from azul.gui.tilewidget import TileWidget
from azul.wall import Wall


class WallWidget(ttk.Frame):
    def __init__(self, master: tk.Misc, wall: Wall) -> None:
        super().__init__(master=master, padding=8)

        self._tilewidgets: list[TileWidget] = []

        for i, row in enumerate(wall.rows):
            for j, tile in enumerate(row):
                self._tilewidgets.append(TileWidget(self, tile=tile))
                self._tilewidgets[-1].grid(column=i, row=j)
